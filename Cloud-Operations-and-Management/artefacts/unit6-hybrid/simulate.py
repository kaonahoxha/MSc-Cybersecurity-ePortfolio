"""Discrete-event teaching model; no OpenStack/Azure connections or real sensors."""
import argparse
import json
from pathlib import Path


def run(config, output):
    output.mkdir(parents=True, exist_ok=True)
    raw, alerts, received, queue, trace = [], [], [], [], []
    seen = set()
    peak = 0
    for tick in range(config['ticks']):
        online = tick not in config['wan_outage_ticks']
        # Edge devices generate readings; fog evaluates every reading locally.
        for device, readings in config['devices'].items():
            event = {'id': f'{device}-{tick}', 'tick': tick,
                     'device': device, 'temperature_c': readings[tick]}
            raw.append(event)
            if event['temperature_c'] >= config['alert_threshold_c']:
                alert = dict(event, kind='alert', local_action='raise_cooling_alarm')
                alerts.append(alert)
                queue.append(alert)
                trace.append(f't={tick}: LOCAL ALERT {device} {event["temperature_c"]}C; WAN={online}')
        # One aggregate per device per window; individual records stay on premises.
        window = config['window_ticks']
        if (tick + 1) % window == 0:
            for device in config['devices']:
                sample = [e['temperature_c'] for e in raw
                          if e['device'] == device and tick-window < e['tick'] <= tick]
                queue.append({'id': f'summary-{device}-{tick}', 'kind': 'summary',
                              'device': device, 'tick': tick, 'count': len(sample),
                              'mean_c': round(sum(sample)/len(sample), 2)})
        peak = max(peak, len(queue))
        # Logical cloud adapter: replay buffered records after WAN recovery.
        if online:
            for item in queue:
                if item['id'] not in seen:
                    received.append(dict(item, received_tick=tick))
                    seen.add(item['id'])
            if queue:
                trace.append(f't={tick}: cloud accepted {len(queue)} queued records')
            queue.clear()
        else:
            trace.append(f't={tick}: WAN unavailable; buffer={len(queue)}')
    cloud_ids = {e['id'] for e in received}
    outage_alerts = [e for e in alerts if e['tick'] in config['wan_outage_ticks']]
    raw_bytes = sum(len(json.dumps(e, sort_keys=True).encode()) for e in raw)
    sent_bytes = sum(len(json.dumps({k:v for k,v in e.items() if k != 'received_tick'}, sort_keys=True).encode()) for e in received)
    metrics = {
        'scope': 'logical simulation; no deployed clouds, networking or measured latency',
        'raw_readings': len(raw), 'local_alerts': len(alerts),
        'alerts_during_wan_outage': len(outage_alerts),
        'cloud_records': len(received),
        'summaries': sum(e['kind'] == 'summary' for e in received),
        'record_count_reduction_percent': round(100*(1-len(received)/len(raw)), 2),
        'raw_json_payload_bytes': raw_bytes, 'forwarded_json_payload_bytes': sent_bytes,
        'payload_byte_reduction_percent': round(100*(1-sent_bytes/raw_bytes), 2),
        'peak_buffer_records': peak, 'remaining_buffer_records': len(queue),
        'duplicate_cloud_records': len(received)-len(cloud_ids),
        'max_alert_cloud_delay_ticks': max((e['received_tick']-e['tick'] for e in received if e['kind']=='alert'), default=0),
        'checks': {
            'all_raw_readings_retained_locally': len(raw)==config['ticks']*len(config['devices']),
            'local_alerts_continue_during_outage': len(outage_alerts)>0,
            'all_alerts_reach_cloud': all(e['id'] in cloud_ids for e in alerts),
            'buffer_drained': not queue,
            'no_duplicate_deliveries': len(cloud_ids)==len(received)
        }
    }
    for name, rows in [('on_prem_raw',raw),('fog_alerts',alerts),('cloud_received',received),('pending',queue)]:
        (output/f'{name}.jsonl').write_text(''.join(json.dumps(e,sort_keys=True)+'\n' for e in rows))
    (output/'metrics.json').write_text(json.dumps(metrics,indent=2)+'\n')
    (output/'execution.log').write_text('\n'.join(trace)+'\n')
    print(json.dumps(metrics,indent=2))
    return metrics


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config',type=Path,default=Path(__file__).with_name('config.json'))
    parser.add_argument('--output',type=Path,default=Path('results'))
    args = parser.parse_args()
    config = json.loads(args.config.read_text())
    if config['ticks'] % config['window_ticks']:
        parser.error('ticks must be divisible by window_ticks')
    if any(len(values)!=config['ticks'] for values in config['devices'].values()):
        parser.error('each device must have one reading per tick')
    run(config,args.output)
