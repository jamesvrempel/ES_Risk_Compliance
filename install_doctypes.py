#!/usr/bin/env python3
"""
Manual DocType Installation Script
Run this to install all ES Risk and Compliance Management DocTypes
"""

import frappe
import os
import json

def install_doctypes():
    """Install all DocTypes from the module"""
    
    app_name = 'es_risk_compliance'
    module_name = 'ES Risk and Compliance Management'
    
    # Get the app path
    try:
        app_path = frappe.get_app_path(app_name)
    except Exception as e:
        print(f"Error: App '{app_name}' not found. Is it installed?")
        print(f"Error details: {str(e)}")
        return False
    
    doctype_path = os.path.join(app_path, 'doctype')
    
    if not os.path.exists(doctype_path):
        print(f"Error: DocType directory not found at {doctype_path}")
        return False
    
    print(f"Installing DocTypes from: {doctype_path}")
    print("=" * 70)
    
    # Get all doctype folders
    doctype_folders = [d for d in os.listdir(doctype_path) 
                       if os.path.isdir(os.path.join(doctype_path, d))]
    
    print(f"Found {len(doctype_folders)} potential DocTypes")
    
    installed_count = 0
    skipped_count = 0
    error_count = 0
    
    for folder_name in sorted(doctype_folders):
        folder_path = os.path.join(doctype_path, folder_name)
        json_file = os.path.join(folder_path, f"{folder_name}.json")
        
        if not os.path.exists(json_file):
            print(f"⚠ Skipping {folder_name}: No JSON file found")
            skipped_count += 1
            continue
        
        try:
            # Read the DocType JSON
            with open(json_file, 'r') as f:
                doctype_dict = json.load(f)
            
            doctype_name = doctype_dict.get('name')
            
            # Check if DocType already exists
            if frappe.db.exists('DocType', doctype_name):
                print(f"⏭ {doctype_name}: Already exists, skipping")
                skipped_count += 1
                continue
            
            # Create the DocType
            doc = frappe.get_doc(doctype_dict)
            doc.insert(ignore_permissions=True)
            
            print(f"✓ {doctype_name}: Installed successfully")
            installed_count += 1
            
        except Exception as e:
            print(f"✗ {folder_name}: Error - {str(e)}")
            error_count += 1
    
    print("=" * 70)
    print(f"Installation Summary:")
    print(f"  ✓ Installed: {installed_count}")
    print(f"  ⏭ Skipped: {skipped_count}")
    print(f"  ✗ Errors: {error_count}")
    
    if installed_count > 0:
        print("\nCommitting changes to database...")
        frappe.db.commit()
        print("✓ Database committed")
        
        print("\nClearing cache...")
        frappe.clear_cache()
        print("✓ Cache cleared")
    
    return True

if __name__ == "__main__":
    install_doctypes()
