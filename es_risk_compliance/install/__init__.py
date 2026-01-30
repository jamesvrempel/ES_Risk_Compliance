# -*- coding: utf-8 -*-
# Copyright (c) 2026, ES Australia and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.sync import sync_for

def after_install():
    """
    Post-installation setup
    CRITICAL: Creates all child table database schemas
    """
    print("\n" + "="*70)
    print("ES RISK & COMPLIANCE v2.0.0 - POST-INSTALL SETUP")
    print("="*70)
    
    # Create module def
    create_module_def()
    
    # Create custom roles  
    create_roles()
    
    # CRITICAL: Create all child table schemas
    create_child_table_schemas()
    
    print("\n" + "="*70)
    print("✅ Installation Complete!")
    print("="*70)
    print("\nIMPORTANT: Run these commands:")
    print("  bench restart")
    print("  Then refresh your browser")
    print("="*70 + "\n")


def create_module_def():
    """Create ES Risk and Compliance module"""
    module_name = "ES Risk and Compliance"
    
    if not frappe.db.exists("Module Def", module_name):
        try:
            module = frappe.get_doc({
                "doctype": "Module Def",
                "module_name": module_name,
                "app_name": "es_risk_compliance",
                "custom": 0
            })
            module.insert(ignore_permissions=True)
            frappe.db.commit()
            print(f"✓ Created Module: {module_name}")
        except Exception as e:
            print(f"⚠ Module creation: {e}")
    else:
        print(f"✓ Module already exists: {module_name}")


def create_roles():
    """Create custom roles for risk management"""
    roles = [
        "Risk Manager",
        "Compliance Manager", 
        "Auditor"
    ]
    
    created = 0
    for role_name in roles:
        if not frappe.db.exists("Role", role_name):
            try:
                role = frappe.get_doc({
                    "doctype": "Role",
                    "role_name": role_name,
                    "desk_access": 1
                })
                role.insert(ignore_permissions=True)
                created += 1
            except Exception as e:
                print(f"⚠ Role {role_name}: {e}")
    
    frappe.db.commit()
    if created > 0:
        print(f"✓ Created {created} roles")
    else:
        print(f"✓ Roles already exist")


def create_child_table_schemas():
    """
    CRITICAL FUNCTION: Force creation of child table database schemas
    This ensures all child tables have proper parent/parentfield/parenttype columns
    """
    print("\n" + "-"*70)
    print("CREATING CHILD TABLE SCHEMAS (CRITICAL)")
    print("-"*70)
    
    # List of ALL child table DocTypes
    child_tables = [
        "Risk Control",
        "Risk Treatment Item"
    ]
    
    success = 0
    failed = 0
    
    for doctype_name in child_tables:
        try:
            # Check if DocType exists
            if not frappe.db.exists("DocType", doctype_name):
                print(f"⚠ {doctype_name}: DocType not found (will be created later)")
                continue
            
            # Get DocType
            doc = frappe.get_doc("DocType", doctype_name)
            
            # Ensure istable is set
            if not doc.istable:
                doc.istable = 1
                doc.save(ignore_permissions=True)
                frappe.db.commit()
            
            # Check if table exists
            table_name = f"tab{doctype_name}"
            result = frappe.db.sql(f"SHOW TABLES LIKE '{table_name}'")
            
            if result:
                # Table exists - check structure
                columns = frappe.db.sql(f"DESCRIBE `{table_name}`", as_dict=True)
                col_names = [c['Field'] for c in columns]
                
                if all(c in col_names for c in ['parent', 'parentfield', 'parenttype']):
                    print(f"✓ {doctype_name}: Schema correct")
                    success += 1
                    continue
                else:
                    # Missing parent columns - recreate
                    print(f"⚠ {doctype_name}: Missing parent columns, recreating...")
                    frappe.db.sql(f"DROP TABLE `{table_name}`")
            
            # Create table with sync_for
            print(f"→ {doctype_name}: Creating schema...")
            sync_for(doctype_name, force=True, reset_permissions=False)
            frappe.db.commit()
            
            # Verify
            result = frappe.db.sql(f"SHOW TABLES LIKE '{table_name}'")
            if result:
                columns = frappe.db.sql(f"DESCRIBE `{table_name}`", as_dict=True)
                col_names = [c['Field'] for c in columns]
                
                if all(c in col_names for c in ['parent', 'parentfield', 'parenttype']):
                    print(f"✅ {doctype_name}: Schema created successfully!")
                    success += 1
                else:
                    print(f"❌ {doctype_name}: Created but missing parent columns")
                    failed += 1
            else:
                print(f"❌ {doctype_name}: Failed to create table")
                failed += 1
                
        except Exception as e:
            print(f"❌ {doctype_name}: ERROR - {e}")
            failed += 1
    
    print(f"\n📊 Child Table Results: {success} success, {failed} failed")
    print("-"*70)
    
    if failed > 0:
        print(f"\n⚠️ WARNING: {failed} child table(s) failed to create")
        print("You may need to run the post-install fix script")
