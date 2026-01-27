# User Guide - ES Risk and Compliance Management

## Table of Contents
1. [Getting Started](#getting-started)
2. [Risk Management](#risk-management)
3. [Compliance Management](#compliance-management)
4. [Audit Management](#audit-management)
5. [Vendor Risk Management](#vendor-risk-management)
6. [Issue & Incident Management](#issue--incident-management)
7. [Reporting & Analytics](#reporting--analytics)

## Getting Started

### Accessing the Module

1. Log in to your ERPNext instance
2. Click on the **ES Risk and Compliance Management** module icon
3. You'll see the module workspace with quick access to all features

### Module Workspace

The workspace is organized into functional areas:
- **Risk Management** - Risk register, categories, treatment plans
- **Compliance** - Frameworks, controls, assessments
- **Audit** - Audit plans and findings
- **Vendor Risk** - Third-party assessments
- **Operations** - Issues and incidents
- **Governance** - Policies and assets

## Risk Management

### Creating a Risk

1. Navigate to **Risk Register > Risk Register**
2. Click **New**
3. Fill in required fields:
   - **Risk Title**: Clear description of the risk
   - **Risk Category**: Select from predefined categories
   - **Risk Owner**: Person responsible for the risk
   - **Risk Status**: Current state (Identified, Assessed, etc.)
   - **Priority**: Critical, High, Medium, or Low
   - **Date Identified**: When risk was discovered

4. Complete the risk analysis:
   - **Threat Description**: What could go wrong
   - **Vulnerability**: Weaknesses that could be exploited
   - **Impact Description**: Consequences if risk occurs

5. Assess the risk:
   - **Likelihood Score**: 1-5 (Rare to Almost Certain)
   - **Impact Score**: 1-5 (Insignificant to Catastrophic)
   - System automatically calculates **Inherent Risk Rating**

6. Add existing controls (if any)
7. Link related items (assets, compliance requirements, vendors)
8. Set review schedule
9. Save and Submit

### Risk Assessment Matrix

The system uses a 5x5 risk matrix:

| Likelihood | Impact | Risk Level |
|-----------|---------|------------|
| 5 x 5 | 25 | Critical |
| 4 x 5, 5 x 4 | 20 | Critical |
| 3 x 5, 4 x 4, 5 x 3 | 15 | High |
| 3 x 4, 4 x 3 | 12 | High |
| 2 x 5, 3 x 3, 5 x 2 | 10 | High |
| 2 x 4, 4 x 2 | 8 | Medium |
| 2 x 3, 3 x 2 | 6 | Medium |
| 1 x 5, 5 x 1 | 5 | Medium |
| 1 x 4, 2 x 2, 4 x 1 | 4 | Low |
| 1 x 3, 3 x 1 | 3 | Low |
| 1 x 2, 2 x 1 | 2 | Low |
| 1 x 1 | 1 | Low |

### Creating Risk Treatment Plans

1. From a Risk Register entry, scroll to **Treatment Plans** section
2. Or create standalone: **Risk Management > Risk Treatment Plan**
3. Select **Treatment Strategy**:
   - **Avoid**: Eliminate the risk
   - **Mitigate**: Reduce likelihood or impact
   - **Transfer**: Share with third party (insurance, outsourcing)
   - **Accept**: Acknowledge and monitor

4. Assign responsibility and timeline
5. Add action items with owners and due dates
6. Track progress through statuses
7. Submit when complete

### Risk Appetite & Tolerance

Define organizational risk appetite at category level:
- **Averse**: Avoid all risks
- **Minimal**: Only accept minimal risks
- **Cautious**: Accept some risks with controls
- **Open**: Accept risks for strategic benefit
- **Hungry**: Actively seek opportunities with risks

## Compliance Management

### Setting Up Compliance Frameworks

1. Navigate to **Compliance > Compliance Framework**
2. Click **New**
3. Enter framework details:
   - **Framework Name**: e.g., "ISO 27001:2022"
   - **Framework Type**: Regulatory, Standard, Best Practice
   - **Status**: Active, Draft, Deprecated
   - **Effective Date**: When it takes effect

4. Add control sets that apply to this framework
5. Link related frameworks (overlaps, supersessions)
6. Save

### Managing Control Sets

1. Navigate to **Compliance > Control Set**
2. Create controls with:
   - **Control ID**: Unique identifier (e.g., AC-001)
   - **Control Title**: Clear name
   - **Control Domain**: Category (Access Control, etc.)
   - **Control Type**: Preventive, Detective, Corrective, Directive
   - **Control Owner**: Responsible person

3. Define implementation details:
   - Control objective and description
   - Implementation guidance
   - Testing frequency

4. Map to frameworks (one control can map to multiple frameworks)
5. Link to risks and assets
6. Track effectiveness through testing

### Conducting Compliance Assessments

1. Navigate to **Compliance > Compliance Assessment**
2. Click **New**
3. Configure assessment:
   - Select framework to assess against
   - Choose assessment type
   - Assign lead assessor and team
   - Define scope

4. Add controls to assess
5. For each control, record:
   - Compliance status (Compliant, Partial, Non-Compliant)
   - Score
   - Evidence and notes

6. System automatically calculates:
   - Overall compliance percentage
   - Count by status
   - Compliance score

7. Document findings with:
   - Finding title and severity
   - Description and recommendation
   - Responsible party and target date

8. Write executive summary
9. Submit assessment

## Audit Management

### Planning an Audit

1. Navigate to **Audit > Audit Plan**
2. Click **New**
3. Define audit parameters:
   - **Audit Title**: Clear identifier
   - **Audit Type**: Internal, External, Compliance, Security
   - **Framework**: Which standard/regulation
   - **Timeline**: Start and end dates

4. Define scope and objectives
5. Assign lead auditor and team
6. Specify entity and department
7. Save and submit when planning complete

### Recording Audit Findings

1. Navigate to **Audit > Audit Finding**
2. Create findings using the 4C methodology:
   - **Condition**: What was found (current state)
   - **Criteria**: What should be (expected state)
   - **Cause**: Why the gap exists
   - **Effect**: Impact of the gap

3. Assign severity (Critical, High, Medium, Low)
4. Provide recommendation
5. Get management response
6. Assign remediation owner and target date
7. Track to resolution

## Vendor Risk Management

### Assessing Vendor Risk

1. Navigate to **Vendor Risk > Vendor Risk Assessment**
2. Select vendor from ERPNext Supplier list
3. Choose assessment type:
   - Initial Assessment (new vendor)
   - Annual Review (periodic)
   - Incident-Driven (after issues)
   - Re-Assessment (follow-up)

4. Document:
   - Services provided
   - Data access level (critical for security)
   - Assessment findings

5. Score vendor across dimensions:
   - Security score
   - Compliance score
   - Overall risk score

6. Determine risk level and required actions
7. Schedule next assessment
8. Submit for approval

## Issue & Incident Management

### Tracking Issues

1. Navigate to **Operations > Issue Tracker**
2. Create issue with:
   - **Issue Type**: Security, Compliance, Policy Violation, etc.
   - **Severity**: Critical to Low
   - **Description**: Detailed explanation

3. Assign to responsible person
4. Set due date based on severity
5. Track status through workflow:
   - Open → In Progress → Under Review → Resolved → Closed

6. Document resolution when complete

### Managing Incidents

1. Navigate to **Operations > Incident Report**
2. Create incident with:
   - **Incident Type**: Security Breach, Data Leak, Outage, etc.
   - **Incident Date**: When it occurred
   - **Detected Date**: When it was discovered
   - **Severity**: Impact level

3. Assign incident commander
4. Document:
   - What happened (description)
   - Impact (who/what affected)
   - Response actions taken

5. Conduct root cause analysis
6. Document lessons learned
7. Create follow-up actions
8. Submit when incident closed

## Reporting & Analytics

### Built-in Reports

Access reports via **Reports** menu:

#### Risk Reports
- **Risk Heat Map**: Visual matrix of all risks
- **Risk by Category**: Breakdown by type
- **Risk Treatment Status**: Progress tracking
- **Risks by Owner**: Accountability view

#### Compliance Reports
- **Compliance Status Dashboard**: Overall compliance posture
- **Control Effectiveness**: Testing results
- **Gap Analysis**: Non-compliant items
- **Framework Coverage**: Multi-framework view

#### Audit Reports
- **Audit Findings Summary**: All findings by severity
- **Finding Status**: Remediation progress
- **Audit Schedule**: Upcoming audits

#### Operational Reports
- **Issue Aging**: Open issues by age
- **Incident Trends**: Patterns over time
- **Vendor Risk Summary**: Third-party overview

### Creating Custom Reports

1. Navigate to **Report Builder**
2. Select DocType (e.g., Risk Register)
3. Choose fields to include
4. Add filters
5. Set sorting
6. Save and share

### Dashboards

Create custom dashboards:
1. Navigate to **Dashboard**
2. Click **New Dashboard**
3. Add charts:
   - Risk trends
   - Compliance scores
   - Finding status
   - Incident counts

4. Configure refresh intervals
5. Share with teams

## Best Practices

### Risk Management
- Review risks quarterly minimum
- Update risk ratings when controls change
- Link risks to business objectives
- Document risk appetite decisions
- Regular risk committee meetings

### Compliance
- Map controls across frameworks (avoid duplication)
- Schedule control testing in advance
- Maintain evidence repository
- Update for regulatory changes
- Annual framework reviews

### Audit
- Plan audits based on risk assessment
- Use sampling for large populations
- Document audit trails
- Follow up findings promptly
- Track remediation commitments

### Data Quality
- Use consistent terminology
- Complete all required fields
- Attach supporting documentation
- Regular data cleanup
- Validate cross-references

## Keyboard Shortcuts

- `Ctrl + K`: Quick search
- `Ctrl + G`: Go to DocType
- `Ctrl + S`: Save document
- `Ctrl + H`: Show shortcuts help

## Getting Help

- **In-app Help**: Click `?` icon in any form
- **Documentation**: [Wiki](https://github.com/yourusername/es_risk_compliance/wiki)
- **Support Email**: support@es-au.com
- **GitHub Issues**: Report bugs and request features

---

**ES Risk and Compliance Management**
Version 1.0.0 | © 2024 ES Australia
