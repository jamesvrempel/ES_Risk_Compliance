#!/usr/bin/env python3
"""
ES Risk and Compliance Management - DocType Generator
Generates all required DocTypes for the module
"""

import json
import os

# Base directory
BASE_DIR = "/home/claude/es_risk_compliance/es_risk_compliance/es_risk_compliance/doctype"

def create_doctype_files(doctype_name, doctype_json, python_code="", js_code=""):
    """Create all files for a DocType"""
    # Convert DocType Name to folder name (lowercase with underscores)
    folder_name = doctype_name.lower().replace(" ", "_")
    folder_path = os.path.join(BASE_DIR, folder_name)
    
    # Create folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)
    
    # Create JSON file
    json_path = os.path.join(folder_path, f"{folder_name}.json")
    with open(json_path, 'w') as f:
        json.dump(doctype_json, f, indent=1)
    
    # Create Python file
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
    
    # Create __init__.py
    init_path = os.path.join(folder_path, "__init__.py")
    with open(init_path, 'w') as f:
        f.write("")
    
    print(f"Created DocType: {doctype_name}")

# Risk Category DocType
risk_category = {
    "actions": [],
    "allow_rename": 1,
    "autoname": "field:category_name",
    "creation": "2024-01-01 00:00:00",
    "doctype": "DocType",
    "engine": "InnoDB",
    "field_order": [
        "category_name",
        "parent_category",
        "description",
        "risk_appetite_default",
        "is_group"
    ],
    "fields": [
        {
            "fieldname": "category_name",
            "fieldtype": "Data",
            "in_list_view": 1,
            "label": "Category Name",
            "reqd": 1,
            "unique": 1
        },
        {
            "fieldname": "parent_category",
            "fieldtype": "Link",
            "label": "Parent Category",
            "options": "Risk Category"
        },
        {
            "fieldname": "description",
            "fieldtype": "Small Text",
            "label": "Description"
        },
        {
            "fieldname": "risk_appetite_default",
            "fieldtype": "Select",
            "label": "Default Risk Appetite",
            "options": "\nAverse\nMinimal\nCautious\nOpen\nHungry"
        },
        {
            "fieldname": "is_group",
            "fieldtype": "Check",
            "label": "Is Group"
        }
    ],
    "index_web_pages_for_search": 1,
    "is_tree": 1,
    "links": [],
    "modified": "2024-01-01 00:00:00",
    "modified_by": "Administrator",
    "module": "ES Risk and Compliance Management",
    "name": "Risk Category",
    "naming_rule": "By fieldname",
    "owner": "Administrator",
    "permissions": [
        {
            "create": 1,
            "delete": 1,
            "email": 1,
            "export": 1,
            "print": 1,
            "read": 1,
            "report": 1,
            "role": "System Manager",
            "share": 1,
            "write": 1
        }
    ],
    "sort_field": "modified",
    "sort_order": "DESC"
}

# Risk Control (Child Table)
risk_control = {
    "actions": [],
    "creation": "2024-01-01 00:00:00",
    "doctype": "DocType",
    "engine": "InnoDB",
    "field_order": [
        "control_name",
        "control_type",
        "control_effectiveness",
        "implementation_date",
        "responsible_person",
        "control_description"
    ],
    "fields": [
        {
            "fieldname": "control_name",
            "fieldtype": "Data",
            "in_list_view": 1,
            "label": "Control Name",
            "reqd": 1
        },
        {
            "fieldname": "control_type",
            "fieldtype": "Select",
            "in_list_view": 1,
            "label": "Control Type",
            "options": "\nPreventive\nDetective\nCorrective\nDirective"
        },
        {
            "fieldname": "control_effectiveness",
            "fieldtype": "Select",
            "in_list_view": 1,
            "label": "Control Effectiveness",
            "options": "\nNot Effective\nPartially Effective\nEffective\nHighly Effective"
        },
        {
            "fieldname": "implementation_date",
            "fieldtype": "Date",
            "label": "Implementation Date"
        },
        {
            "fieldname": "responsible_person",
            "fieldtype": "Link",
            "label": "Responsible Person",
            "options": "User"
        },
        {
            "fieldname": "control_description",
            "fieldtype": "Small Text",
            "label": "Control Description"
        }
    ],
    "index_web_pages_for_search": 1,
    "istable": 1,
    "links": [],
    "modified": "2024-01-01 00:00:00",
    "modified_by": "Administrator",
    "module": "ES Risk and Compliance Management",
    "name": "Risk Control",
    "owner": "Administrator",
    "permissions": [],
    "sort_field": "modified",
    "sort_order": "DESC"
}

# Risk Treatment Item (Child Table)
risk_treatment_item = {
    "actions": [],
    "creation": "2024-01-01 00:00:00",
    "doctype": "DocType",
    "engine": "InnoDB",
    "field_order": [
        "treatment_plan",
        "treatment_strategy",
        "assigned_to",
        "target_completion_date",
        "status",
        "cost_estimate"
    ],
    "fields": [
        {
            "fieldname": "treatment_plan",
            "fieldtype": "Link",
            "in_list_view": 1,
            "label": "Treatment Plan",
            "options": "Risk Treatment Plan",
            "reqd": 1
        },
        {
            "fieldname": "treatment_strategy",
            "fieldtype": "Select",
            "label": "Treatment Strategy",
            "options": "\nAvoid\nMitigate\nTransfer\nAccept"
        },
        {
            "fieldname": "assigned_to",
            "fieldtype": "Link",
            "in_list_view": 1,
            "label": "Assigned To",
            "options": "User"
        },
        {
            "fieldname": "target_completion_date",
            "fieldtype": "Date",
            "in_list_view": 1,
            "label": "Target Completion Date"
        },
        {
            "fieldname": "status",
            "fieldtype": "Select",
            "in_list_view": 1,
            "label": "Status",
            "options": "\nPlanned\nIn Progress\nCompleted\nOn Hold\nCancelled"
        },
        {
            "fieldname": "cost_estimate",
            "fieldtype": "Currency",
            "label": "Cost Estimate"
        }
    ],
    "index_web_pages_for_search": 1,
    "istable": 1,
    "links": [],
    "modified": "2024-01-01 00:00:00",
    "modified_by": "Administrator",
    "module": "ES Risk and Compliance Management",
    "name": "Risk Treatment Item",
    "owner": "Administrator",
    "permissions": [],
    "sort_field": "modified",
    "sort_order": "DESC"
}

# Risk Treatment Plan
risk_treatment_plan = {
    "actions": [],
    "allow_rename": 1,
    "autoname": "format:RTP-{####}",
    "creation": "2024-01-01 00:00:00",
    "doctype": "DocType",
    "engine": "InnoDB",
    "field_order": [
        "plan_title",
        "related_risk",
        "treatment_strategy",
        "column_break_4",
        "status",
        "priority",
        "created_date",
        "section_break_8",
        "plan_description",
        "section_break_10",
        "assigned_to",
        "approver",
        "column_break_13",
        "target_start_date",
        "target_completion_date",
        "actual_completion_date",
        "section_break_17",
        "estimated_cost",
        "actual_cost",
        "budget_approved",
        "section_break_21",
        "action_items",
        "section_break_23",
        "success_criteria",
        "monitoring_plan",
        "amended_from"
    ],
    "fields": [
        {
            "fieldname": "plan_title",
            "fieldtype": "Data",
            "in_list_view": 1,
            "label": "Plan Title",
            "reqd": 1
        },
        {
            "fieldname": "related_risk",
            "fieldtype": "Link",
            "label": "Related Risk",
            "options": "Risk Register"
        },
        {
            "fieldname": "treatment_strategy",
            "fieldtype": "Select",
            "in_list_view": 1,
            "label": "Treatment Strategy",
            "options": "\nAvoid\nMitigate\nTransfer\nAccept",
            "reqd": 1
        },
        {
            "fieldname": "column_break_4",
            "fieldtype": "Column Break"
        },
        {
            "fieldname": "status",
            "fieldtype": "Select",
            "in_list_view": 1,
            "label": "Status",
            "options": "\nDraft\nPlanned\nIn Progress\nUnder Review\nCompleted\nOn Hold\nCancelled",
            "reqd": 1
        },
        {
            "fieldname": "priority",
            "fieldtype": "Select",
            "label": "Priority",
            "options": "\nCritical\nHigh\nMedium\nLow"
        },
        {
            "fieldname": "created_date",
            "fieldtype": "Date",
            "label": "Created Date",
            "reqd": 1
        },
        {
            "fieldname": "section_break_8",
            "fieldtype": "Section Break",
            "label": "Plan Details"
        },
        {
            "fieldname": "plan_description",
            "fieldtype": "Text Editor",
            "label": "Plan Description"
        },
        {
            "fieldname": "section_break_10",
            "fieldtype": "Section Break",
            "label": "Responsibility & Timeline"
        },
        {
            "fieldname": "assigned_to",
            "fieldtype": "Link",
            "label": "Assigned To",
            "options": "User",
            "reqd": 1
        },
        {
            "fieldname": "approver",
            "fieldtype": "Link",
            "label": "Approver",
            "options": "User"
        },
        {
            "fieldname": "column_break_13",
            "fieldtype": "Column Break"
        },
        {
            "fieldname": "target_start_date",
            "fieldtype": "Date",
            "label": "Target Start Date"
        },
        {
            "fieldname": "target_completion_date",
            "fieldtype": "Date",
            "label": "Target Completion Date"
        },
        {
            "fieldname": "actual_completion_date",
            "fieldtype": "Date",
            "label": "Actual Completion Date",
            "read_only": 1
        },
        {
            "fieldname": "section_break_17",
            "fieldtype": "Section Break",
            "label": "Budget"
        },
        {
            "fieldname": "estimated_cost",
            "fieldtype": "Currency",
            "label": "Estimated Cost"
        },
        {
            "fieldname": "actual_cost",
            "fieldtype": "Currency",
            "label": "Actual Cost"
        },
        {
            "fieldname": "budget_approved",
            "fieldtype": "Check",
            "label": "Budget Approved"
        },
        {
            "fieldname": "section_break_21",
            "fieldtype": "Section Break",
            "label": "Action Items"
        },
        {
            "fieldname": "action_items",
            "fieldtype": "Table",
            "label": "Action Items",
            "options": "Treatment Action Item"
        },
        {
            "fieldname": "section_break_23",
            "fieldtype": "Section Break",
            "label": "Success Criteria & Monitoring"
        },
        {
            "fieldname": "success_criteria",
            "fieldtype": "Small Text",
            "label": "Success Criteria"
        },
        {
            "fieldname": "monitoring_plan",
            "fieldtype": "Small Text",
            "label": "Monitoring Plan"
        },
        {
            "fieldname": "amended_from",
            "fieldtype": "Link",
            "label": "Amended From",
            "no_copy": 1,
            "options": "Risk Treatment Plan",
            "print_hide": 1,
            "read_only": 1
        }
    ],
    "index_web_pages_for_search": 1,
    "is_submittable": 1,
    "links": [],
    "modified": "2024-01-01 00:00:00",
    "modified_by": "Administrator",
    "module": "ES Risk and Compliance Management",
    "name": "Risk Treatment Plan",
    "naming_rule": "Expression",
    "owner": "Administrator",
    "permissions": [
        {
            "create": 1,
            "delete": 1,
            "email": 1,
            "export": 1,
            "print": 1,
            "read": 1,
            "report": 1,
            "role": "System Manager",
            "share": 1,
            "submit": 1,
            "write": 1
        },
        {
            "create": 1,
            "email": 1,
            "export": 1,
            "print": 1,
            "read": 1,
            "report": 1,
            "role": "Risk Manager",
            "share": 1,
            "submit": 1,
            "write": 1
        }
    ],
    "sort_field": "modified",
    "sort_order": "DESC",
    "track_changes": 1
}

# Treatment Action Item (Child Table)
treatment_action_item = {
    "actions": [],
    "creation": "2024-01-01 00:00:00",
    "doctype": "DocType",
    "engine": "InnoDB",
    "field_order": [
        "action_description",
        "responsible_person",
        "due_date",
        "status",
        "completion_date"
    ],
    "fields": [
        {
            "fieldname": "action_description",
            "fieldtype": "Small Text",
            "in_list_view": 1,
            "label": "Action Description",
            "reqd": 1
        },
        {
            "fieldname": "responsible_person",
            "fieldtype": "Link",
            "in_list_view": 1,
            "label": "Responsible Person",
            "options": "User"
        },
        {
            "fieldname": "due_date",
            "fieldtype": "Date",
            "in_list_view": 1,
            "label": "Due Date"
        },
        {
            "fieldname": "status",
            "fieldtype": "Select",
            "in_list_view": 1,
            "label": "Status",
            "options": "\nPending\nIn Progress\nCompleted\nBlocked"
        },
        {
            "fieldname": "completion_date",
            "fieldtype": "Date",
            "label": "Completion Date"
        }
    ],
    "index_web_pages_for_search": 1,
    "istable": 1,
    "links": [],
    "modified": "2024-01-01 00:00:00",
    "modified_by": "Administrator",
    "module": "ES Risk and Compliance Management",
    "name": "Treatment Action Item",
    "owner": "Administrator",
    "permissions": [],
    "sort_field": "modified",
    "sort_order": "DESC"
}

# Generate all DocTypes
print("Generating ES Risk and Compliance Management DocTypes...")
print("=" * 60)

create_doctype_files("Risk Category", risk_category)
create_doctype_files("Risk Control", risk_control)
create_doctype_files("Risk Treatment Item", risk_treatment_item)
create_doctype_files("Risk Treatment Plan", risk_treatment_plan)
create_doctype_files("Treatment Action Item", treatment_action_item)

print("=" * 60)
print("Phase 1 DocTypes created successfully!")
print("\nNext phase will include:")
print("- Compliance Framework")
print("- Control Set")
print("- Compliance Assessment")
print("- Audit Plan & Findings")
print("- Vendor Risk Assessment")
print("- Issue & Incident Management")
print("- Asset & Policy Registers")
