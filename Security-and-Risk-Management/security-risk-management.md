# Security and Risk Management

[Back to the e-Portfolio homepage](index.md)

## Module Overview

This module examines how organisations identify, analyse, evaluate and treat security risks. It compares qualitative and quantitative assessments, introduces threat-modelling methods and considers security standards, business continuity and disaster recovery.

## Learning Outcomes

By completing this module, I aim to be able to:

1. Select appropriately between qualitative and quantitative risk assessments.
2. Create and evaluate threat models for different scenarios.
3. Develop quantitative risk models using justified data and assumptions.
4. Design and explain disaster-recovery strategies and solutions.

## Unit Learning and Artefacts

### Unit 1 – Introduction to Security and Risk Management

Unit 1 established the relationship between assets, threats, vulnerabilities, likelihood and consequences. I compared qualitative and quantitative assessment and considered how organisational context affects the selection of standards and controls.

**Evidence retained:** Knowledge-check results, Collaborative Learning Discussion 1 initial post and team-project communication.

### Unit 2 – Users, Assessments and the Risk Management Process

Unit 2 demonstrated that risk assessment is not purely technical. Qualitative ratings can support accessible prioritisation but may conceal subjective judgements. Quantitative analysis can improve decisions when its data and assumptions are defensible. User participation can also reveal operational practices and unintended consequences that might otherwise be missed.

**Evidence retained:** Collaborative Learning Discussion 1 initial post, peer responses and reflective commentary.

### Unit 3 – Introduction to Threat Modelling and Management

Unit 3 distinguished a threat from the vulnerability that enables it. I examined STRIDE, DREAD, attack trees and PASTA, recognising that each serves a different purpose. STRIDE supports systematic threat identification, attack trees explore alternative attack paths, and PASTA connects technical scenarios with business impact.

**Evidence retained:** Knowledge-check results, threat-method comparison and collaborative discussion material.

### Unit 4 – Application of Threat Modelling and Management Techniques

Unit 4 applied threat modelling using the Threat Modeling Manifesto, OWASP guidance and MITRE ATT&CK. The seminar preparation considered cyber-physical systems, attack entry points, operational dependencies and the use of scenario-specific metrics to prioritise vulnerabilities.

**Evidence retained:** Seminar answers based on Jbair et al. (2022) and risk-prioritisation notes.

### Unit 5 – Security and Risk Standards

Unit 5 examined how general and sector-specific standards support risk management. I compared ISO/IEC 27001, the NIST Cybersecurity Framework, GDPR, PCI-DSS and sector-specific frameworks, recognising that compliance provides a baseline rather than proof that risks are effectively controlled.

**Evidence retained:** Submitted security-framework Wiki contribution and the GDPR case-study analysis below. Two peer responses will be added after suitable contributions are available.

#### GDPR Case Study: Transmission of Visa Data Through WhatsApp

##### Case overview

The case concerned a complaint against Ireland’s Department of Foreign Affairs and Trade (DFAT). Its Cairo mission transmitted a visa applicant’s supporting document through WhatsApp to the applicant’s employer after concerns arose about the document’s authenticity. The employer lacked an official email account and identified WhatsApp as the only available transmission method. DFAT completed a local risk assessment, relied on WhatsApp’s end-to-end encryption and deleted the document from the staff member’s device after sending it. The employer subsequently identified the document as fraudulent, and the visa application was refused (Data Protection Commission, 2019, pp. 19–20).

##### Specific aspect of GDPR addressed

The complaint was formally assessed under Ireland’s Data Protection Acts 1988 and 2003 because the processing pre-dated the GDPR. Nevertheless, the case illustrates several GDPR principles: lawfulness, fairness and transparency; purpose limitation; data minimisation; integrity and confidentiality; and accountability under Articles 5(1) and 5(2) (European Parliament and Council of the European Union, 2016).

Under the GDPR, DFAT would need to document an Article 6 lawful basis, plausibly the performance of a public task where supported by applicable law. Consent would not necessarily be required merely because information was disclosed to a third party. The decisive questions would be whether verification was legally authorised, necessary for determining visa eligibility and adequately explained to the applicant.

Article 32 requires security appropriate to the nature, context and risk of processing rather than prescribing or prohibiting a particular application (European Parliament and Council of the European Union, 2016). Consequently, WhatsApp’s consumer status does not automatically establish non-compliance. Equally, end-to-end encryption alone is insufficient: device security, recipient verification, retention, access and governance also affect risk. This reflects Aven and Thekdi’s (2025) argument that risk decisions must consider context and the strength of available knowledge.

A contemporary assessment would also examine whether sending data to a recipient in Egypt constituted a restricted third-country transfer under Chapter V GDPR. Any reliance on an Article 49 derogation would require careful documentation because such derogations should remain exceptional rather than become routine transfer mechanisms (European Data Protection Board, 2018).

##### Resolution

The Data Protection Commission found no contravention. Verification was necessary because the employer was identified in the application and was best placed to authenticate the document. The relevant privacy information notified applicants that supporting material could be disclosed for immigration verification. The Commission also accepted DFAT’s documented conclusion that WhatsApp was the most secure method available in the circumstances (Data Protection Commission, 2019, pp. 19–20).

This was a narrow, context-dependent finding—not general approval for transmitting official documents through WhatsApp. The Commission stated that the outcome might have differed if a secure official channel had been available. The decision therefore demonstrates proportionality: an exceptional method may be defensible when its necessity, alternatives and controls are evidenced.

##### Mitigation as Information Security Manager

I would establish a controlled exception process containing:

- A documented lawful basis, purpose, necessity assessment and comparison of available channels.
- Data minimisation and redaction of information unnecessary for verification.
- Independent recipient verification before transmission.
- Organisation-managed devices protected by MFA, encryption, mobile-device management, remote wiping and security updates (NCSC, 2021).
- Prohibition of automatic personal-cloud backups or personal-device storage for official documents.
- Recorded deletion from the transmitting device and retention of an auditable organisational record.
- A Chapter V transfer assessment before transmitting data outside the EEA.
- Management or data-protection approval for high-risk exceptional transfers.
- Periodic review of exceptions to identify where an approved secure file-transfer service is required.

The principal lesson is that risk assessment must demonstrate why a method was necessary and proportionate. Encryption is one control, not evidence that the entire processing activity is compliant.

### Unit 6 – Practical Implications of Security and Risk Standards

Unit 6 applies GDPR, PCI-DSS and other standards to practical organisational scenarios. The Pampered Pets team project demonstrates that standards must be incorporated into risk treatment without allowing compliance to replace critical evaluation. For example, using a PCI-DSS-compliant payment provider may reduce the business’s exposure to card data, but supplier assurance, service availability and residual third-party risk still require management.

**Evidence retained:** Submitted team contract, shared-document version history, communication records and my digital-transformation risk assessment. The final report, peer assessment and submission evidence will be added after completion.

## Collaborative Learning Discussion 1

The discussion examined how data and technology may undermine fairness and accountability in human-rights investigations. My initial contribution considered incomplete data, surveillance, unequal technological visibility and the exclusion of community knowledge. My peer responses developed this position by proposing human-rights impact assessments, evidence triangulation, data provenance, community governance and accessible mechanisms for correction and redress.

This activity changed my understanding of participation in risk management. I initially viewed participation mainly as a way to improve system requirements. Through the discussion, I recognised that meaningful participation must also give affected communities influence over acceptable harms, data use and whether deployment should proceed.

## Development Team Project – Risk Identification Report

**Status:** Drafting and integration in progress  
**Deadline:** 7 September 2026  
**Team:** Group 3

The project evaluates the risks of maintaining the current Pampered Pets business model against a proposed digital transformation. My allocated contribution assesses the proposed transformation, its digital, operational and supply-chain risks, and proportionate mitigations. As project lead, I am also responsible for compiling, editing, referencing and submitting the final report.

My analysis recommends a phased transformation beginning with click-and-collect, digital inventory and batch records, and online product information. It prioritises the integrity of ingredient, allergen, expiry and batch data because inaccurate records could affect product safety and recall effectiveness. It also considers cloud dependency, ransomware, limited staff capacity and the strategic risks of replacing local suppliers with an international supply chain.

### Team Meeting and Communication Notes

- **22 August 2026:** Proposed dividing the assessment into four substantive analytical sections so that every member contributes to the report.
- **24 August 2026:** Selected the digital-transformation risk section and proposed internal deadlines for drafting, integration and review.
- **Team contract:** Coordinated completion of the signed contract and submitted it to the module tutor.
- **29 August 2026:** Reminded the team that individual sections and references were due on 30 August.
- **30 August 2026:** Completed my allocated section, followed up after receiving no drafts or acknowledgements, and created a shared live document to record and integrate contributions.
- **Next action:** Review every contribution for coverage, overlap, methodology, evidence and consistency before combining the report.

## Professional Skills Matrix

| Skill | Evidence | Current development |
|---|---|---|
| Risk identification | Pampered Pets assessment and unit exercises | Identifying technical, operational, strategic and supply-chain risks |
| Critical analysis | Evaluation of digitalisation trade-offs | Considering second-order consequences and residual risk rather than listing generic controls |
| Research | Module readings and external security guidance | Selecting authoritative sources and connecting evidence to recommendations |
| Communication | Initial post, peer responses and team coordination | Expressing complex risks concisely for academic and business audiences |
| Teamwork and leadership | Group 3 planning and report integration | Setting internal deadlines, coordinating contributions and maintaining consistency |
| Digital literacy | GitHub e-portfolio and threat-modelling resources | Organising evidence and presenting development progressively |

## Development Action Plan

- Apply a consistent likelihood-and-impact scale across the team report and justify all ratings.
- Record assumptions and residual risk instead of presenting controls as complete solutions.
- Preserve drafts, group decisions and feedback to demonstrate development rather than only the final outcome.
- Strengthen quantitative-risk skills in later units by documenting data sources and uncertainty.
- Add the final report, peer-assessment outcome and a critical reflection after submission.

## References

AIRMIC, Alarm and IRM (2010) *A structured approach to enterprise risk management and the requirements of ISO 31000*. London: Association of Insurance and Risk Managers in Industry, Alarm and Institute of Risk Management.

Aven, T. and Thekdi, S. (2025) *Risk Science*. 3rd edn. Abingdon: Routledge.

Data Protection Commission (2019) *Annual Report: 25 May–31 December 2018*. Dublin: Data Protection Commission, pp. 19–20. Available at: https://www.dataprotection.ie/sites/default/files/uploads/2019-03/DPC%20Annual%20Report%2025%20May%20-%2031%20December%202018.pdf (Accessed: 30 August 2026).

European Data Protection Board (2018) *Guidelines 2/2018 on derogations of Article 49 under Regulation 2016/679*. Brussels: European Data Protection Board. Available at: https://www.edpb.europa.eu/documents/guideline/guidelines-22018-on-derogations-of-article-49-under-regulation-2016679_en (Accessed: 30 August 2026).

European Parliament and Council of the European Union (2016) ‘Regulation (EU) 2016/679 of 27 April 2016’, *Official Journal of the European Union*, L119, pp. 1–88. Available at: https://eur-lex.europa.eu/eli/reg/2016/679/oj (Accessed: 30 August 2026).

Jbair, M., Ahmad, B., Maple, C. and Harrison, R. (2022) ‘Threat modelling for industrial cyber physical systems in the era of smart manufacturing’, *Computers in Industry*, 137, 103611. Available at: https://doi.org/10.1016/j.compind.2022.103611.

National Cyber Security Centre (NCSC) (2021) *Mobile Device Management*. Available at: https://www.ncsc.gov.uk/collection/device-security-guidance/getting-ready/mobile-device-management (Accessed: 30 August 2026).

Renn, O., Beier, G. and Schweizer, P.J. (2021) ‘The opportunities and risks of digitalisation for sustainable development: a systemic perspective’, *GAIA – Ecological Perspectives for Science and Society*, 30(1), pp. 23–28. Available at: https://doi.org/10.14512/gaia.30.1.6.

Shevchenko, N., Chick, T.A., O’Riordan, P., Scanlon, T.P. and Woody, C. (2018) *Threat modeling: a summary of available methods*. Pittsburgh, PA: Carnegie Mellon University Software Engineering Institute.
