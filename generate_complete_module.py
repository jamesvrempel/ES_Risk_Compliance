#!/usr/bin/env python3
"""
Complete Module Generator for ES Risk and Compliance Management
Creates remaining DocTypes and packages everything
"""

import json
import os
import subprocess

BASE_DIR = "/home/claude/es_risk_compliance/es_risk_compliance/es_risk_compliance/doctype"

def create_simple_doctype(name, autoname_format, fields, is_submittable=False, istable=False):
    """Helper to create DocType JSON structure"""
    folder_name = name.lower().replace(" ", "_")
    
    doctype = {
        "actions": [],
        "creation": "2024-01-01 00:00:00",
        "doctype": "DocType",
        "engine": "InnoDB",
        "field_order": [f["fieldname"] for f in fields],
        "fields": fields,
        "index_web_pages_for_search": 1,
        "links": [],
        "modified": "2024-01-01 00:00:00",
        "modified_by": "Administrator",
        "module": "ES Risk and Compliance Management",
        "name": name,
        "owner": "Administrator",
        "sort_field": "modified",
        "sort_order": "DESC"
    }
    
    if not istable:
        doctype["allow_rename"] = 1
        if autoname_format.startswith("format:"):
            doctype["autoname"] = autoname_format
            doctype["naming_rule"] = "Expression"
        elif autoname_format.startswith("field:"):
            doctype["autoname"] = autoname_format
            doctype["naming_rule"] = "By fieldname"
    else:
        doctype["istable"] = 1
        doctype["permissions"] = []
        return doctype
    
    if is_submittable:
        doctype["is_submittable"] = 1
    
    doctype["permissions"] = [
        {"create": 1, "delete": 1, "email": 1, "export": 1, "print": 1, "read": 1, 
         "report": 1, "role": "System Manager", "share": 1, "write": 1}
    ]
    
    if is_submittable:
        doctype["permissions"][0]["submit"] = 1
    
    return doctype

def save_doctype(name, doctype_json):
    """Save DocType files"""
    folder_name = name.lower().replace(" ", "_")
    folder_path = os.path.join(BASE_DIR, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    # JSON
    json_path = os.path.join(folder_path, f"{folder_name}.json")
    with open(json_path, 'w') as f:
        json.dump(doctype_json, f, indent=1)
    
    # Python
    py_path = os.path.join(folder_path, f"{folder_name}.py")
    python_code = f"""# Copyright (c) 2024, ES Australia and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class {name.replace(' ', '')}(Document):
\tpass
"""
    with open(py_path, 'w') as f:
        f.write(python_code)
    
    # __init__
    init_path = os.path.join(folder_path, "__init__.py")
    with open(init_path, 'w') as f:
        f.write("")
    
    print(f"Created: {name}")

print("Creating remaining DocTypes for ES Risk and Compliance Management...")
print("=" * 70)

# Asset Register
asset_register_fields = [
    {"fieldname": "asset_name", "fieldtype": "Data", "label": "Asset Name", "reqd": 1, "in_list_view": 1},
    {"fieldname": "asset_type", "fieldtype": "Select", "label": "Asset Type", "in_list_view": 1,
     "options": "\nInformation Asset\nPhysical Asset\nSoftware\nHardware\nNetwork\nFacility\nPeople"},
    {"fieldname": "asset_owner", "fieldtype": "Link", "label": "Asset Owner", "options": "User", "reqd": 1},
    {"fieldname": "column_break_4", "fieldtype": "Column Break"},
    {"fieldname": "criticality", "fieldtype": "Select", "label": "Criticality", "in_list_view": 1,
     "options": "\nCritical\nHigh\nMedium\nLow"},
    {"fieldname": "status", "fieldtype": "Select", "label": "Status",
     "options": "\nActive\nInactive\nRetired\nUnder Review"},
    {"fieldname": "section_break_7", "fieldtype": "Section Break", "label": "Asset Details"},
    {"fieldname": "description", "fieldtype": "Text", "label": "Description"},
    {"fieldname": "location", "fieldtype": "Data", "label": "Location"},
    {"fieldname": "custodian", "fieldtype": "Link", "label": "Custodian", "options": "User"}
]
save_doctype("Asset Register", create_simple_doctype("Asset Register", "format:ASSET-{#####}", asset_register_fields))

# Issue Tracker
issue_fields = [
    {"fieldname": "issue_title", "fieldtype": "Data", "label": "Issue Title", "reqd": 1, "in_list_view": 1},
    {"fieldname": "issue_type", "fieldtype": "Select", "label": "Issue Type", "in_list_view": 1,
     "options": "\nSecurity Issue\nCompliance Gap\nPolicy Violation\nControl Deficiency\nOperational Issue"},
    {"fieldname": "severity", "fieldtype": "Select", "label": "Severity", "in_list_view": 1,
     "options": "\nCritical\nHigh\nMedium\nLow", "reqd": 1},
    {"fieldname": "column_break_4", "fieldtype": "Column Break"},
    {"fieldname": "status", "fieldtype": "Select", "label": "Status", "in_list_view": 1,
     "options": "\nOpen\nIn Progress\nUnder Review\nResolved\nClosed\nReopened", "reqd": 1},
    {"fieldname": "reported_date", "fieldtype": "Date", "label": "Reported Date", "reqd": 1},
    {"fieldname": "due_date", "fieldtype": "Date", "label": "Due Date"},
    {"fieldname": "section_break_8", "fieldtype": "Section Break", "label": "Issue Details"},
    {"fieldname": "description", "fieldtype": "Text Editor", "label": "Description"},
    {"fieldname": "section_break_10", "fieldtype": "Section Break", "label": "Assignment"},
    {"fieldname": "reported_by", "fieldtype": "Link", "label": "Reported By", "options": "User"},
    {"fieldname": "assigned_to", "fieldtype": "Link", "label": "Assigned To", "options": "User", "reqd": 1},
    {"fieldname": "resolution", "fieldtype": "Text", "label": "Resolution"},
    {"fieldname": "resolved_date", "fieldtype": "Date", "label": "Resolved Date"}
]
save_doctype("Issue Tracker", create_simple_doctype("Issue Tracker", "format:ISSUE-{#####}", issue_fields, is_submittable=True))

# Incident Report
incident_fields = [
    {"fieldname": "incident_title", "fieldtype": "Data", "label": "Incident Title", "reqd": 1, "in_list_view": 1},
    {"fieldname": "incident_type", "fieldtype": "Select", "label": "Incident Type", "in_list_view": 1,
     "options": "\nSecurity Breach\nData Leak\nSystem Outage\nPolicy Violation\nPhysical Security\nOther"},
    {"fieldname": "severity", "fieldtype": "Select", "label": "Severity", "in_list_view": 1,
     "options": "\nCritical\nHigh\nMedium\nLow", "reqd": 1},
    {"fieldname": "column_break_4", "fieldtype": "Column Break"},
    {"fieldname": "status", "fieldtype": "Select", "label": "Status", "in_list_view": 1,
     "options": "\nReported\nInvestigating\nContained\nResolved\nClosed", "reqd": 1},
    {"fieldname": "incident_date", "fieldtype": "Datetime", "label": "Incident Date", "reqd": 1},
    {"fieldname": "detected_date", "fieldtype": "Datetime", "label": "Detected Date"},
    {"fieldname": "section_break_8", "fieldtype": "Section Break", "label": "Incident Details"},
    {"fieldname": "description", "fieldtype": "Text Editor", "label": "Description"},
    {"fieldname": "impact_description", "fieldtype": "Text", "label": "Impact Description"},
    {"fieldname": "section_break_11", "fieldtype": "Section Break", "label": "Response Team"},
    {"fieldname": "incident_commander", "fieldtype": "Link", "label": "Incident Commander", "options": "User", "reqd": 1},
    {"fieldname": "reported_by", "fieldtype": "Link", "label": "Reported By", "options": "User"},
    {"fieldname": "section_break_14", "fieldtype": "Section Break", "label": "Resolution"},
    {"fieldname": "root_cause", "fieldtype": "Text", "label": "Root Cause"},
    {"fieldname": "resolution_summary", "fieldtype": "Text", "label": "Resolution Summary"},
    {"fieldname": "lessons_learned", "fieldtype": "Text", "label": "Lessons Learned"}
]
save_doctype("Incident Report", create_simple_doctype("Incident Report", "format:INC-{#####}", incident_fields, is_submittable=True))

# Policy Document
policy_fields = [
    {"fieldname": "policy_name", "fieldtype": "Data", "label": "Policy Name", "reqd": 1, "unique": 1},
    {"fieldname": "policy_code", "fieldtype": "Data", "label": "Policy Code"},
    {"fieldname": "policy_type", "fieldtype": "Select", "label": "Policy Type", "in_list_view": 1,
     "options": "\nSecurity Policy\nCompliance Policy\nHR Policy\nIT Policy\nOperational Policy\nGovernance Policy"},
    {"fieldname": "column_break_4", "fieldtype": "Column Break"},
    {"fieldname": "status", "fieldtype": "Select", "label": "Status", "in_list_view": 1,
     "options": "\nDraft\nUnder Review\nApproved\nPublished\nRetired", "reqd": 1},
    {"fieldname": "version", "fieldtype": "Data", "label": "Version"},
    {"fieldname": "effective_date", "fieldtype": "Date", "label": "Effective Date"},
    {"fieldname": "section_break_8", "fieldtype": "Section Break", "label": "Policy Details"},
    {"fieldname": "policy_purpose", "fieldtype": "Text", "label": "Policy Purpose"},
    {"fieldname": "policy_scope", "fieldtype": "Text", "label": "Policy Scope"},
    {"fieldname": "policy_content", "fieldtype": "Text Editor", "label": "Policy Content"},
    {"fieldname": "section_break_12", "fieldtype": "Section Break", "label": "Ownership & Review"},
    {"fieldname": "policy_owner", "fieldtype": "Link", "label": "Policy Owner", "options": "User", "reqd": 1},
    {"fieldname": "approved_by", "fieldtype": "Link", "label": "Approved By", "options": "User"},
    {"fieldname": "column_break_15", "fieldtype": "Column Break"},
    {"fieldname": "approval_date", "fieldtype": "Date", "label": "Approval Date"},
    {"fieldname": "review_frequency", "fieldtype": "Select", "label": "Review Frequency",
     "options": "\nQuarterly\nBi-Annually\nAnnually\nBiennially"},
    {"fieldname": "next_review_date", "fieldtype": "Date", "label": "Next Review Date"}
]
save_doctype("Policy Document", create_simple_doctype("Policy Document", "field:policy_name", policy_fields))

# Vendor Risk Assessment
vendor_fields = [
    {"fieldname": "vendor_name", "fieldtype": "Link", "label": "Vendor Name", "options": "Supplier", "reqd": 1, "in_list_view": 1},
    {"fieldname": "assessment_date", "fieldtype": "Date", "label": "Assessment Date", "reqd": 1},
    {"fieldname": "assessment_type", "fieldtype": "Select", "label": "Assessment Type", "in_list_view": 1,
     "options": "\nInitial Assessment\nAnnual Review\nIncident-Driven\nRe-Assessment"},
    {"fieldname": "column_break_4", "fieldtype": "Column Break"},
    {"fieldname": "risk_level", "fieldtype": "Select", "label": "Risk Level", "in_list_view": 1,
     "options": "\nCritical\nHigh\nMedium\nLow"},
    {"fieldname": "assessment_status", "fieldtype": "Select", "label": "Assessment Status", "in_list_view": 1,
     "options": "\nPlanned\nIn Progress\nCompleted\nApproved", "reqd": 1},
    {"fieldname": "section_break_7", "fieldtype": "Section Break", "label": "Assessment Details"},
    {"fieldname": "services_provided", "fieldtype": "Text", "label": "Services Provided"},
    {"fieldname": "data_access_level", "fieldtype": "Select", "label": "Data Access Level",
     "options": "\nNo Access\nPublic Data\nInternal Data\nConfidential Data\nHighly Confidential"},
    {"fieldname": "section_break_10", "fieldtype": "Section Break", "label": "Risk Assessment"},
    {"fieldname": "security_score", "fieldtype": "Float", "label": "Security Score", "precision": "2"},
    {"fieldname": "compliance_score", "fieldtype": "Float", "label": "Compliance Score", "precision": "2"},
    {"fieldname": "overall_risk_score", "fieldtype": "Float", "label": "Overall Risk Score", "precision": "2"},
    {"fieldname": "section_break_14", "fieldtype": "Section Break", "label": "Assessment Team"},
    {"fieldname": "assessor", "fieldtype": "Link", "label": "Assessor", "options": "User", "reqd": 1},
    {"fieldname": "approved_by", "fieldtype": "Link", "label": "Approved By", "options": "User"},
    {"fieldname": "section_break_17", "fieldtype": "Section Break", "label": "Findings & Recommendations"},
    {"fieldname": "findings", "fieldtype": "Text Editor", "label": "Findings"},
    {"fieldname": "recommendations", "fieldtype": "Text Editor", "label": "Recommendations"},
    {"fieldname": "next_assessment_date", "fieldtype": "Date", "label": "Next Assessment Date"}
]
save_doctype("Vendor Risk Assessment", create_simple_doctype("Vendor Risk Assessment", "format:VRA-{#####}", vendor_fields, is_submittable=True))

# Audit Plan
audit_plan_fields = [
    {"fieldname": "audit_title", "fieldtype": "Data", "label": "Audit Title", "reqd": 1, "in_list_view": 1},
    {"fieldname": "audit_type", "fieldtype": "Select", "label": "Audit Type", "in_list_view": 1,
     "options": "\nInternal Audit\nExternal Audit\nCompliance Audit\nSecurity Audit\nFinancial Audit\nOperational Audit"},
    {"fieldname": "audit_framework", "fieldtype": "Link", "label": "Audit Framework", "options": "Compliance Framework"},
    {"fieldname": "column_break_4", "fieldtype": "Column Break"},
    {"fieldname": "audit_status", "fieldtype": "Select", "label": "Audit Status", "in_list_view": 1,
     "options": "\nPlanned\nIn Progress\nFieldwork Complete\nReporting\nCompleted", "reqd": 1},
    {"fieldname": "planned_start_date", "fieldtype": "Date", "label": "Planned Start Date", "reqd": 1},
    {"fieldname": "planned_end_date", "fieldtype": "Date", "label": "Planned End Date"},
    {"fieldname": "section_break_8", "fieldtype": "Section Break", "label": "Audit Scope"},
    {"fieldname": "audit_scope", "fieldtype": "Text Editor", "label": "Audit Scope"},
    {"fieldname": "audit_objectives", "fieldtype": "Text", "label": "Audit Objectives"},
    {"fieldname": "section_break_11", "fieldtype": "Section Break", "label": "Audit Team"},
    {"fieldname": "lead_auditor", "fieldtype": "Link", "label": "Lead Auditor", "options": "User", "reqd": 1},
    {"fieldname": "entity_audited", "fieldtype": "Link", "label": "Entity Audited", "options": "Company"},
    {"fieldname": "department", "fieldtype": "Link", "label": "Department", "options": "Department"}
]
save_doctype("Audit Plan", create_simple_doctype("Audit Plan", "format:AUD-{#####}", audit_plan_fields, is_submittable=True))

# Audit Finding
audit_finding_fields = [
    {"fieldname": "finding_title", "fieldtype": "Data", "label": "Finding Title", "reqd": 1, "in_list_view": 1},
    {"fieldname": "audit_plan", "fieldtype": "Link", "label": "Audit Plan", "options": "Audit Plan"},
    {"fieldname": "finding_type", "fieldtype": "Select", "label": "Finding Type", "in_list_view": 1,
     "options": "\nControl Deficiency\nNon-Compliance\nProcess Gap\nDocumentation Issue\nObservation"},
    {"fieldname": "column_break_4", "fieldtype": "Column Break"},
    {"fieldname": "severity", "fieldtype": "Select", "label": "Severity", "in_list_view": 1,
     "options": "\nCritical\nHigh\nMedium\nLow", "reqd": 1},
    {"fieldname": "status", "fieldtype": "Select", "label": "Status", "in_list_view": 1,
     "options": "\nOpen\nIn Remediation\nManagement Review\nResolved\nClosed", "reqd": 1},
    {"fieldname": "finding_date", "fieldtype": "Date", "label": "Finding Date", "reqd": 1},
    {"fieldname": "section_break_8", "fieldtype": "Section Break", "label": "Finding Details"},
    {"fieldname": "condition", "fieldtype": "Text Editor", "label": "Condition (What was found)"},
    {"fieldname": "criteria", "fieldtype": "Text", "label": "Criteria (What should be)"},
    {"fieldname": "cause", "fieldtype": "Text", "label": "Cause (Why it happened)"},
    {"fieldname": "effect", "fieldtype": "Text", "label": "Effect (Impact)"},
    {"fieldname": "section_break_13", "fieldtype": "Section Break", "label": "Recommendation & Response"},
    {"fieldname": "recommendation", "fieldtype": "Text Editor", "label": "Recommendation"},
    {"fieldname": "management_response", "fieldtype": "Text Editor", "label": "Management Response"},
    {"fieldname": "section_break_16", "fieldtype": "Section Break", "label": "Remediation"},
    {"fieldname": "responsible_person", "fieldtype": "Link", "label": "Responsible Person", "options": "User", "reqd": 1},
    {"fieldname": "target_date", "fieldtype": "Date", "label": "Target Date"},
    {"fieldname": "actual_resolution_date", "fieldtype": "Date", "label": "Actual Resolution Date"}
]
save_doctype("Audit Finding", create_simple_doctype("Audit Finding", "format:AF-{#####}", audit_finding_fields, is_submittable=True))

print("=" * 70)
print("\nAll DocTypes created successfully!")
print("\nSummary of created DocTypes:")
print("  Risk Management: Risk Register, Risk Category, Risk Treatment Plan")
print("  Compliance: Compliance Framework, Control Set, Compliance Assessment") 
print("  Audit: Audit Plan, Audit Finding")
print("  Vendor: Vendor Risk Assessment")
print("  Operations: Issue Tracker, Incident Report")
print("  Governance: Policy Document, Asset Register")
