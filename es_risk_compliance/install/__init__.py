# Copyright (c) 2024, ES Australia and contributors
# For license information, please see license.txt

import frappe
import os
import json

def after_install():
    """
    Hook that runs after app installation
    Creates Module Def, roles, and installs all DocTypes in correct order
    """
    print("ES Risk and Compliance Management: Installing...")
    
    app_name = 'es_risk_compliance'
    module_name = 'ES Risk and Compliance Management'
    
    try:
        # First, create the Module Def if it doesn't exist
        if not frappe.db.exists('Module Def', module_name):
            module_def = frappe.get_doc({
                'doctype': 'Module Def',
                'module_name': module_name,
                'app_name': app_name,
                'custom': 0
            })
            module_def.insert(ignore_permissions=True)
            print(f"  ✓ Created Module Def: {module_name}")
        
        frappe.db.commit()
        
        # Create roles BEFORE installing DocTypes
        create_default_roles()
        frappe.db.commit()
        
        # Now install DocTypes in correct order (parents before children)
        app_path = frappe.get_app_path(app_name)
        doctype_path = os.path.join(app_path, 'doctype')
        
        if not os.path.exists(doctype_path):
            frappe.throw(f"DocType directory not found at {doctype_path}")
        
        # Define installation order - install in multiple passes to handle circular dependencies
        
        # Pass 1: Simple parent DocTypes with no child table dependencies
        pass1_doctypes = [
            'risk_category',
            'vendor_risk_assessment',
            'issue_tracker',
            'incident_report',
            'policy_document',
            'asset_register'
        ]
        
        # Pass 2: Parent DocTypes with child tables
        pass2_doctypes = [
            'compliance_framework',
            'control_set',
            'risk_register',
            'risk_treatment_plan',
            'compliance_assessment',
            'audit_plan',
            'audit_finding'
        ]
        
        # Pass 3: Child table DocTypes
        pass3_doctypes = [
            'risk_control',
            'risk_treatment_item',
            'treatment_action_item',
            'framework_control_set',
            'related_framework_item',
            'control_framework_mapping',
            'assessment_team_member',
            'assessment_control_result',
            'assessment_finding'
        ]
        
        installed_count = 0
        
        # Install Pass 1 - Simple parents
        print("  Installing simple DocTypes...")
        for doctype_folder in pass1_doctypes:
            if install_doctype(doctype_path, doctype_folder):
                installed_count += 1
        
        frappe.db.commit()
        
        # Install Pass 2 - Complex parents (disable validation for circular deps)
        print("  Installing parent DocTypes...")
        for doctype_folder in pass2_doctypes:
            if install_doctype(doctype_path, doctype_folder, ignore_validate=True):
                installed_count += 1
        
        frappe.db.commit()
        
        # Install Pass 3 - Child tables
        print("  Installing child table DocTypes...")
        for doctype_folder in pass3_doctypes:
            if install_doctype(doctype_path, doctype_folder):
                installed_count += 1
        
        frappe.db.commit()
        
        # Pass 4: Reload and sync all DocTypes to fix relationships
        print("  Syncing DocTypes...")
        for doctype_folder in pass2_doctypes:
            try:
                doctype_name = doctype_folder.replace('_', ' ').title()
                if frappe.db.exists('DocType', doctype_name):
                    frappe.reload_doctype(doctype_name, force=True)
            except Exception as e:
                pass
        
        frappe.db.commit()
        
        print(f"ES Risk and Compliance Management: {installed_count} DocTypes installed")
        
    except Exception as e:
        frappe.log_error(f"Error in after_install: {str(e)}")
        print(f"Error: {str(e)}")


def install_doctype(doctype_path, folder_name, ignore_validate=False):
    """Install a single DocType from its JSON file"""
    folder_path = os.path.join(doctype_path, folder_name)
    json_file = os.path.join(folder_path, f"{folder_name}.json")
    
    if not os.path.exists(json_file):
        print(f"  ⚠ Warning: JSON file not found for {folder_name}")
        return False
    
    try:
        # Read the DocType JSON
        with open(json_file, 'r') as f:
            doctype_dict = json.load(f)
        
        doctype_name = doctype_dict.get('name')
        
        # Check if DocType already exists
        if frappe.db.exists('DocType', doctype_name):
            print(f"  ⏭ {doctype_name}: Already exists")
            return False
        
        # Create the DocType
        doc = frappe.get_doc(doctype_dict)
        
        # For circular dependencies, skip validation during insert
        if ignore_validate:
            doc.flags.ignore_validate = True
        
        doc.insert(ignore_permissions=True)
        
        print(f"  ✓ Installed: {doctype_name}")
        return True
        
    except Exception as e:
        print(f"  ✗ Error installing {folder_name}: {str(e)}")
        return False


def create_default_roles():
    """Create default roles for the module"""
    roles = [
        "Risk Manager",
        "Compliance Manager",
        "Auditor",
        "Security Officer",
        "Policy Manager"
    ]
    
    for role_name in roles:
        if not frappe.db.exists("Role", role_name):
            try:
                role = frappe.get_doc({
                    "doctype": "Role",
                    "role_name": role_name,
                    "desk_access": 1
                })
                role.insert(ignore_permissions=True)
                print(f"  ✓ Created role: {role_name}")
            except Exception as e:
                print(f"  ✗ Error creating role {role_name}: {str(e)}")


