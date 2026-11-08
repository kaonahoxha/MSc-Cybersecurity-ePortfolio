#!/usr/bin/env bash
set -euo pipefail

subscription="Azure for Students"
region="francecentral"
group="unit4-aci-$(date -u +%Y%m%d%H%M%S)-${RANDOM}"
instance="unit4-automation"

az account set --subscription "$subscription"

echo "Registering Azure Container Instances..."
az provider register --namespace Microsoft.ContainerInstance --wait

echo "Creating temporary resource group: $group"
az group create --name "$group" --location "$region" --output none

cleanup() {
  echo "Requesting deletion of temporary resource group: $group"
  az group delete --name "$group" --yes --no-wait ||
    echo "Cleanup request failed. Check resource group $group in Azure."
}
trap cleanup EXIT

echo "Deploying $instance in $region..."
az container create \
  --resource-group "$group" \
  --name "$instance" \
  --location "$region" \
  --image mcr.microsoft.com/azurelinux/base/core:3.0 \
  --os-type Linux \
  --cpu 1 \
  --memory 1 \
  --restart-policy Never \
  --command-line "/bin/sh -c 'set -e; echo Unit 4 Azure automation; cat /etc/os-release; echo UNIT4_COMMANDS_OK'" \
  --output none

for attempt in {1..12}; do
  logs=$(az container logs --resource-group "$group" --name "$instance" 2>/dev/null) || logs=""
  if [[ "$logs" == *UNIT4_COMMANDS_OK* ]]; then
    printf '%s\n' "$logs"
    exit 0
  fi
  sleep 5
done

echo "Could not verify command execution. Last container output:"
printf '%s\n' "$logs"
exit 1
