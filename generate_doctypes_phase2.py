#!/usr/bin/env python3
"""
ES Risk and Compliance Management - Phase 2: Compliance Management DocTypes
"""

import json
import os

BASE_DIR = "/home/claude/es_risk_compliance/es_risk_compliance/es_risk_compliance/doctype"

def create_doctype_files(doctype_name, doctype_json, python_code=""):
    """Create all files for a DocType"""
    folder_name = doctype_name.lower().replace(" ", "_")
    folder_path = os.path.join(BASE_DIR, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    json_path = os.path.join(folder_path, f"{folder_name}.json")
    with open(json_path, 'w') as f:
        json.dump(doctype_json, f, indent=1)
    
    py_path = os.path.join(folder_path, f"{folder_name}.py")
    if not python_code:
        python_code = f"""# Copyright (c) 2024, ES Australia and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class {doctype_name.replace(' ', '')}(Document):
\tpass
"""
    with open(py_path, 'w') as f:
        f.write(python_code)
    
    init_path = os.path.join(folder_path, "__init__.py")
    with open(init_path, 'w') as f:
        f.write("")
    
    print(f"Created DocType: {doctype_name}")

# Compliance Framework
compliance_framework = {
    "actions": [],
    "allow_rename": 1,
    "autoname": "field:framework_name",
    "creation": "2024-01-01 00:00:00",
    "doctype": "DocType",
    "engine": "InnoDB",
    "field_order": [
        "framework_name",
        "framework_code",
        "framework_type",
        "column_break_4",
        "status",
        "version",
        "effective_date",
        "section_break_8",
        "description",
        "section_break_10",
        "issuing_authority",
        "regulatory_body",
        "jurisdiction",
        "column_break_14",
        "industry_sector",
        "applicability",
        "mandatory",
        "section_break_18",
        "control_sets",
        "section_break_20",
        "framework_url",
        "documentation_link",
        "section_break_23",
        "related_frameworks"
    ],
    "fields": [
        {"fieldname": "framework_name", "fieldtype": "Data", "in_list_view": 1, "label": "Framework Name", "reqd": 1, "unique": 1},
        {"fieldname": "framework_code", "fieldtype": "Data", "label": "Framework Code"},
        {"fieldname": "framework_type", "fieldtype": "Select", "in_list_view": 1, "label": "Framework Type", 
         "options": "\nRegulatory\nStandard\nBest Practice\nInternal Policy\nContractual"},
        {"fieldname": "column_break_4", "fieldtype": "Column Break"},
        {"fieldname": "status", "fieldtype": "Select", "label": "Status", 
         "options": "\nActive\nDraft\nUnder Review\nDeprecated\nSuperseded"},
        {"fieldname": "version", "fieldtype": "Data", "label": "Version"},
        {"fieldname": "effective_date", "fieldtype": "Date", "label": "Effective Date"},
        {"fieldname": "section_break_8", "fieldtype": "Section Break", "label": "Framework Details"},
        {"fieldname": "description", "fieldtype": "Text Editor", "label": "Description"},
        {"fieldname": "section_break_10", "fieldtype": "Section Break", "label": "Regulatory Information"},
        {"fieldname": "issuing_authority", "fieldtype": "Data", "label": "Issuing Authority"},
        {"fieldname": "regulatory_body", "fieldtype": "Data", "label": "Regulatory Body"},
        {"fieldname": "jurisdiction", "fieldtype": "Data", "label": "Jurisdiction"},
        {"fieldname": "column_break_14", "fieldtype": "Column Break"},
        {"fieldname": "industry_sector", "fieldtype": "Select", "label": "Industry Sector",
         "options": "\nFinancial Services\nHealthcare\nTechnology\nManufacturing\nRetail\nGovernment\nEducation\nAll Sectors"},
        {"fieldname": "applicability", "fieldtype": "Small Text", "label": "Applicability"},
        {"fieldname": "mandatory", "fieldtype": "Check", "label": "Mandatory Compliance"},
        {"fieldname": "section_break_18", "fieldtype": "Section Break", "label": "Control Sets"},
        {"fieldname": "control_sets", "fieldtype": "Table", "label": "Control Sets", "options": "Framework Control Set"},
        {"fieldname": "section_break_20", "fieldtype": "Section Break", "label": "References"},
        {"fieldname": "framework_url", "fieldtype": "Data", "label": "Framework URL"},
        {"fieldname": "documentation_link", "fieldtype": "Data", "label": "Documentation Link"},
        {"fieldname": "section_break_23", "fieldtype": "Section Break", "label": "Related Frameworks"},
        {"fieldname": "related_frameworks", "fieldtype": "Table", "label": "Related Frameworks", "options": "Related Framework Item"}
    ],
    "index_web_pages_for_search": 1,
    "links": [],
    "modified": "2024-01-01 00:00:00",
    "modified_by": "Administrator",
    "module": "ES Risk and Compliance Management",
    "name": "Compliance Framework",
    "naming_rule": "By fieldname",
    "owner": "Administrator",
    "permissions": [
        {"create": 1, "delete": 1, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1, 
         "role": "System Manager", "share": 1, "write": 1},
        {"create": 1, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1,
         "role": "Compliance Manager", "share": 1, "write": 1}
    ],
    "sort_field": "modified",
    "sort_order": "DESC"
}

# Framework Control Set (Child Table)
framework_control_set = {
    "actions": [],
    "creation": "2024-01-01 00:00:00",
    "doctype": "DocType",
    "engine": "InnoDB",
    "field_order": ["control_set", "control_domain", "requirement_level"],
    "fields": [
        {"fieldname": "control_set", "fieldtype": "Link", "in_list_view": 1, "label": "Control Set", 
         "options": "Control Set", "reqd": 1},
        {"fieldname": "control_domain", "fieldtype": "Data", "label": "Control Domain"},
        {"fieldname": "requirement_level", "fieldtype": "Select", "in_list_view": 1, "label": "Requirement Level",
         "options": "\nMandatory\nRecommended\nOptional"}
    ],
    "index_web_pages_for_search": 1,
    "istable": 1,
    "links": [],
    "modified": "2024-01-01 00:00:00",
    "modified_by": "Administrator",
    "module": "ES Risk and Compliance Management",
    "name": "Framework Control Set",
    "owner": "Administrator",
    "permissions": [],
    "sort_field": "modified",
    "sort_order": "DESC"
}

# Related Framework Item (Child Table)
related_framework_item = {
    "actions": [],
    "creation": "2024-01-01 00:00:00",
    "doctype": "DocType",
    "engine": "InnoDB",
    "field_order": ["related_framework", "relationship_type", "overlap_percentage"],
    "fields": [
        {"fieldname": "related_framework", "fieldtype": "Link", "in_list_view": 1, "label": "Related Framework",
         "options": "Compliance Framework", "reqd": 1},
        {"fieldname": "relationship_type", "fieldtype": "Select", "label": "Relationship Type",
         "options": "\nSupersedes\nSuperseded By\nSupplements\nAligns With\nConflicts With"},
        {"fieldname": "overlap_percentage", "fieldtype": "Percent", "label": "Overlap Percentage"}
    ],
    "index_web_pages_for_search": 1,
    "istable": 1,
    "links": [],
    "modified": "2024-01-01 00:00:00",
    "modified_by": "Administrator",
    "module": "ES Risk and Compliance Management",
    "name": "Related Framework Item",
    "owner": "Administrator",
    "permissions": [],
    "sort_field": "modified",
    "sort_order": "DESC"
}

# Control Set
control_set = {
    "actions": [],
    "allow_rename": 1,
    "autoname": "format:CTRL-{#####}",
    "creation": "2024-01-01 00:00:00",
    "doctype": "DocType",
    "engine": "InnoDB",
    "field_order": [
        "control_id",
        "control_title",
        "control_domain",
        "column_break_4",
        "control_type",
        "control_status",
        "priority",
        "section_break_8",
        "control_objective",
        "control_description",
        "implementation_guidance",
        "section_break_12",
        "control_owner",
        "responsible_team",
        "column_break_15",
        "implementation_date",
        "last_review_date",
        "next_review_date",
        "section_break_19",
        "control_effectiveness",
        "testing_frequency",
        "last_test_date",
        "column_break_23",
        "test_result",
        "test_evidence",
        "section_break_26",
        "related_frameworks",
        "section_break_28",
        "related_risks",
        "related_assets"
    ],
    "fields": [
        {"fieldname": "control_id", "fieldtype": "Data", "label": "Control ID", "reqd": 1, "unique": 1},
        {"fieldname": "control_title", "fieldtype": "Data", "in_list_view": 1, "label": "Control Title", "reqd": 1},
        {"fieldname": "control_domain", "fieldtype": "Select", "label": "Control Domain",
         "options": "\nAccess Control\nAsset Management\nCryptography\nPhysical Security\nOperations Security\nCommunications Security\nSystem Development\nSupplier Relationships\nIncident Management\nBusiness Continuity\nCompliance\nHuman Resources"},
        {"fieldname": "column_break_4", "fieldtype": "Column Break"},
        {"fieldname": "control_type", "fieldtype": "Select", "in_list_view": 1, "label": "Control Type",
         "options": "\nPreventive\nDetective\nCorrective\nDirective\nCompensating"},
        {"fieldname": "control_status", "fieldtype": "Select", "in_list_view": 1, "label": "Control Status",
         "options": "\nPlanned\nPartially Implemented\nImplemented\nTested\nOperational\nNeeds Improvement\nIneffective"},
        {"fieldname": "priority", "fieldtype": "Select", "label": "Priority",
         "options": "\nCritical\nHigh\nMedium\nLow"},
        {"fieldname": "section_break_8", "fieldtype": "Section Break", "label": "Control Details"},
        {"fieldname": "control_objective", "fieldtype": "Small Text", "label": "Control Objective"},
        {"fieldname": "control_description", "fieldtype": "Text Editor", "label": "Control Description"},
        {"fieldname": "implementation_guidance", "fieldtype": "Text Editor", "label": "Implementation Guidance"},
        {"fieldname": "section_break_12", "fieldtype": "Section Break", "label": "Responsibility"},
        {"fieldname": "control_owner", "fieldtype": "Link", "label": "Control Owner", "options": "User", "reqd": 1},
        {"fieldname": "responsible_team", "fieldtype": "Link", "label": "Responsible Team", "options": "Department"},
        {"fieldname": "column_break_15", "fieldtype": "Column Break"},
        {"fieldname": "implementation_date", "fieldtype": "Date", "label": "Implementation Date"},
        {"fieldname": "last_review_date", "fieldtype": "Date", "label": "Last Review Date"},
        {"fieldname": "next_review_date", "fieldtype": "Date", "label": "Next Review Date"},
        {"fieldname": "section_break_19", "fieldtype": "Section Break", "label": "Control Testing"},
        {"fieldname": "control_effectiveness", "fieldtype": "Select", "label": "Control Effectiveness",
         "options": "\nNot Tested\nNot Effective\nPartially Effective\nEffective\nHighly Effective"},
        {"fieldname": "testing_frequency", "fieldtype": "Select", "label": "Testing Frequency",
         "options": "\nDaily\nWeekly\nMonthly\nQuarterly\nBi-Annually\nAnnually\nAs Needed"},
        {"fieldname": "last_test_date", "fieldtype": "Date", "label": "Last Test Date"},
        {"fieldname": "column_break_23", "fieldtype": "Column Break"},
        {"fieldname": "test_result", "fieldtype": "Select", "label": "Test Result",
         "options": "\nPassed\nPassed with Exceptions\nFailed\nNot Tested"},
        {"fieldname": "test_evidence", "fieldtype": "Attach", "label": "Test Evidence"},
        {"fieldname": "section_break_26", "fieldtype": "Section Break", "label": "Framework Mapping"},
        {"fieldname": "related_frameworks", "fieldtype": "Table", "label": "Related Frameworks", 
         "options": "Control Framework Mapping"},
        {"fieldname": "section_break_28", "fieldtype": "Section Break", "label": "Related Items"},
        {"fieldname": "related_risks", "fieldtype": "Table MultiSelect", "label": "Related Risks", 
         "options": "Risk Register"},
        {"fieldname": "related_assets", "fieldtype": "Table MultiSelect", "label": "Related Assets",
         "options": "Asset Register"}
    ],
    "index_web_pages_for_search": 1,
    "links": [],
    "modified": "2024-01-01 00:00:00",
    "modified_by": "Administrator",
    "module": "ES Risk and Compliance Management",
    "name": "Control Set",
    "naming_rule": "Expression",
    "owner": "Administrator",
    "permissions": [
        {"create": 1, "delete": 1, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1,
         "role": "System Manager", "share": 1, "write": 1},
        {"create": 1, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1,
         "role": "Compliance Manager", "share": 1, "write": 1}
    ],
    "sort_field": "modified",
    "sort_order": "DESC",
    "track_changes": 1
}

# Control Framework Mapping (Child Table)
control_framework_mapping = {
    "actions": [],
    "creation": "2024-01-01 00:00:00",
    "doctype": "DocType",
    "engine": "InnoDB",
    "field_order": ["framework", "framework_control_id", "requirement_level"],
    "fields": [
        {"fieldname": "framework", "fieldtype": "Link", "in_list_view": 1, "label": "Framework",
         "options": "Compliance Framework", "reqd": 1},
        {"fieldname": "framework_control_id", "fieldtype": "Data", "in_list_view": 1, "label": "Framework Control ID"},
        {"fieldname": "requirement_level", "fieldtype": "Select", "label": "Requirement Level",
         "options": "\nMandatory\nRecommended\nOptional"}
    ],
    "index_web_pages_for_search": 1,
    "istable": 1,
    "links": [],
    "modified": "2024-01-01 00:00:00",
    "modified_by": "Administrator",
    "module": "ES Risk and Compliance Management",
    "name": "Control Framework Mapping",
    "owner": "Administrator",
    "permissions": [],
    "sort_field": "modified",
    "sort_order": "DESC"
}

# Compliance Assessment
compliance_assessment = {
    "actions": [],
    "allow_rename": 1,
    "autoname": "format:CA-{#####}",
    "creation": "2024-01-01 00:00:00",
    "doctype": "DocType",
    "engine": "InnoDB",
    "field_order": [
        "assessment_title",
        "framework",
        "assessment_type",
        "column_break_4",
        "assessment_status",
        "assessment_date",
        "due_date",
        "section_break_8",
        "scope",
        "section_break_10",
        "lead_assessor",
        "assessment_team",
        "column_break_13",
        "entity_assessed",
        "department",
        "section_break_16",
        "controls_assessed",
        "section_break_18",
        "overall_score",
        "compliance_percentage",
        "column_break_21",
        "compliant_controls",
        "non_compliant_controls",
        "partially_compliant_controls",
        "section_break_25",
        "findings",
        "section_break_27",
        "executive_summary",
        "recommendations",
        "section_break_30",
        "next_assessment_date",
        "amended_from"
    ],
    "fields": [
        {"fieldname": "assessment_title", "fieldtype": "Data", "in_list_view": 1, "label": "Assessment Title", "reqd": 1},
        {"fieldname": "framework", "fieldtype": "Link", "in_list_view": 1, "label": "Framework",
         "options": "Compliance Framework", "reqd": 1},
        {"fieldname": "assessment_type", "fieldtype": "Select", "label": "Assessment Type",
         "options": "\nSelf Assessment\nInternal Audit\nExternal Audit\nPenetration Test\nVulnerability Assessment\nGap Analysis"},
        {"fieldname": "column_break_4", "fieldtype": "Column Break"},
        {"fieldname": "assessment_status", "fieldtype": "Select", "in_list_view": 1, "label": "Assessment Status",
         "options": "\nPlanned\nIn Progress\nUnder Review\nCompleted\nCancelled", "reqd": 1},
        {"fieldname": "assessment_date", "fieldtype": "Date", "label": "Assessment Date", "reqd": 1},
        {"fieldname": "due_date", "fieldtype": "Date", "label": "Due Date"},
        {"fieldname": "section_break_8", "fieldtype": "Section Break", "label": "Scope"},
        {"fieldname": "scope", "fieldtype": "Text Editor", "label": "Scope"},
        {"fieldname": "section_break_10", "fieldtype": "Section Break", "label": "Assessment Team"},
        {"fieldname": "lead_assessor", "fieldtype": "Link", "label": "Lead Assessor", "options": "User", "reqd": 1},
        {"fieldname": "assessment_team", "fieldtype": "Table", "label": "Assessment Team", "options": "Assessment Team Member"},
        {"fieldname": "column_break_13", "fieldtype": "Column Break"},
        {"fieldname": "entity_assessed", "fieldtype": "Link", "label": "Entity Assessed", "options": "Company"},
        {"fieldname": "department", "fieldtype": "Link", "label": "Department", "options": "Department"},
        {"fieldname": "section_break_16", "fieldtype": "Section Break", "label": "Controls Assessed"},
        {"fieldname": "controls_assessed", "fieldtype": "Table", "label": "Controls Assessed", 
         "options": "Assessment Control Result"},
        {"fieldname": "section_break_18", "fieldtype": "Section Break", "label": "Assessment Results"},
        {"fieldname": "overall_score", "fieldtype": "Float", "label": "Overall Score", "precision": "2"},
        {"fieldname": "compliance_percentage", "fieldtype": "Percent", "label": "Compliance Percentage"},
        {"fieldname": "column_break_21", "fieldtype": "Column Break"},
        {"fieldname": "compliant_controls", "fieldtype": "Int", "label": "Compliant Controls", "read_only": 1},
        {"fieldname": "non_compliant_controls", "fieldtype": "Int", "label": "Non-Compliant Controls", "read_only": 1},
        {"fieldname": "partially_compliant_controls", "fieldtype": "Int", "label": "Partially Compliant Controls", "read_only": 1},
        {"fieldname": "section_break_25", "fieldtype": "Section Break", "label": "Findings"},
        {"fieldname": "findings", "fieldtype": "Table", "label": "Findings", "options": "Assessment Finding"},
        {"fieldname": "section_break_27", "fieldtype": "Section Break", "label": "Summary & Recommendations"},
        {"fieldname": "executive_summary", "fieldtype": "Text Editor", "label": "Executive Summary"},
        {"fieldname": "recommendations", "fieldtype": "Text Editor", "label": "Recommendations"},
        {"fieldname": "section_break_30", "fieldtype": "Section Break", "label": "Follow-up"},
        {"fieldname": "next_assessment_date", "fieldtype": "Date", "label": "Next Assessment Date"},
        {"fieldname": "amended_from", "fieldtype": "Link", "label": "Amended From", "no_copy": 1,
         "options": "Compliance Assessment", "print_hide": 1, "read_only": 1}
    ],
    "index_web_pages_for_search": 1,
    "is_submittable": 1,
    "links": [],
    "modified": "2024-01-01 00:00:00",
    "modified_by": "Administrator",
    "module": "ES Risk and Compliance Management",
    "name": "Compliance Assessment",
    "naming_rule": "Expression",
    "owner": "Administrator",
    "permissions": [
        {"create": 1, "delete": 1, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1,
         "role": "System Manager", "share": 1, "submit": 1, "write": 1},
        {"create": 1, "email": 1, "export": 1, "print": 1, "read": 1, "report": 1,
         "role": "Compliance Manager", "share": 1, "submit": 1, "write": 1}
    ],
    "sort_field": "modified",
    "sort_order": "DESC",
    "track_changes": 1
}

# Child tables for Compliance Assessment
assessment_team_member = {
    "actions": [],
    "creation": "2024-01-01 00:00:00",
    "doctype": "DocType",
    "engine": "InnoDB",
    "field_order": ["team_member", "role"],
    "fields": [
        {"fieldname": "team_member", "fieldtype": "Link", "in_list_view": 1, "label": "Team Member",
         "options": "User", "reqd": 1},
        {"fieldname": "role", "fieldtype": "Data", "in_list_view": 1, "label": "Role"}
    ],
    "index_web_pages_for_search": 1,
    "istable": 1,
    "links": [],
    "modified": "2024-01-01 00:00:00",
    "modified_by": "Administrator",
    "module": "ES Risk and Compliance Management",
    "name": "Assessment Team Member",
    "owner": "Administrator",
    "permissions": [],
    "sort_field": "modified",
    "sort_order": "DESC"
}

assessment_control_result = {
    "actions": [],
    "creation": "2024-01-01 00:00:00",
    "doctype": "DocType",
    "engine": "InnoDB",
    "field_order": ["control", "compliance_status", "score", "notes"],
    "fields": [
        {"fieldname": "control", "fieldtype": "Link", "in_list_view": 1, "label": "Control",
         "options": "Control Set", "reqd": 1},
        {"fieldname": "compliance_status", "fieldtype": "Select", "in_list_view": 1, "label": "Compliance Status",
         "options": "\nCompliant\nPartially Compliant\nNon-Compliant\nNot Applicable\nNot Tested"},
        {"fieldname": "score", "fieldtype": "Float", "in_list_view": 1, "label": "Score", "precision": "2"},
        {"fieldname": "notes", "fieldtype": "Small Text", "label": "Notes"}
    ],
    "index_web_pages_for_search": 1,
    "istable": 1,
    "links": [],
    "modified": "2024-01-01 00:00:00",
    "modified_by": "Administrator",
    "module": "ES Risk and Compliance Management",
    "name": "Assessment Control Result",
    "owner": "Administrator",
    "permissions": [],
    "sort_field": "modified",
    "sort_order": "DESC"
}

assessment_finding = {
    "actions": [],
    "creation": "2024-01-01 00:00:00",
    "doctype": "DocType",
    "engine": "InnoDB",
    "field_order": ["finding_title", "severity", "finding_description", "recommendation", "responsible_party", "target_resolution_date"],
    "fields": [
        {"fieldname": "finding_title", "fieldtype": "Data", "in_list_view": 1, "label": "Finding Title", "reqd": 1},
        {"fieldname": "severity", "fieldtype": "Select", "in_list_view": 1, "label": "Severity",
         "options": "\nCritical\nHigh\nMedium\nLow"},
        {"fieldname": "finding_description", "fieldtype": "Small Text", "label": "Finding Description"},
        {"fieldname": "recommendation", "fieldtype": "Small Text", "label": "Recommendation"},
        {"fieldname": "responsible_party", "fieldtype": "Link", "in_list_view": 1, "label": "Responsible Party", "options": "User"},
        {"fieldname": "target_resolution_date", "fieldtype": "Date", "in_list_view": 1, "label": "Target Resolution Date"}
    ],
    "index_web_pages_for_search": 1,
    "istable": 1,
    "links": [],
    "modified": "2024-01-01 00:00:00",
    "modified_by": "Administrator",
    "module": "ES Risk and Compliance Management",
    "name": "Assessment Finding",
    "owner": "Administrator",
    "permissions": [],
    "sort_field": "modified",
    "sort_order": "DESC"
}

print("Generating Phase 2: Compliance Management DocTypes...")
print("=" * 60)

create_doctype_files("Compliance Framework", compliance_framework)
create_doctype_files("Framework Control Set", framework_control_set)
create_doctype_files("Related Framework Item", related_framework_item)
create_doctype_files("Control Set", control_set)
create_doctype_files("Control Framework Mapping", control_framework_mapping)
create_doctype_files("Compliance Assessment", compliance_assessment)
create_doctype_files("Assessment Team Member", assessment_team_member)
create_doctype_files("Assessment Control Result", assessment_control_result)
create_doctype_files("Assessment Finding", assessment_finding)

print("=" * 60)
print("Phase 2 DocTypes created successfully!")
