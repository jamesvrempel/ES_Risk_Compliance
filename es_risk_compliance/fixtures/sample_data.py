#!/usr/bin/env python3
"""
Sample Data Fixtures for ES Risk and Compliance Management
Load sample risk categories, frameworks, and controls for demonstration
"""

import frappe
from frappe import _

def load_risk_categories():
    """Load sample risk categories"""
    categories = [
        {
            "category_name": "Strategic Risk",
            "description": "Risks related to business strategy and objectives",
            "risk_appetite_default": "Cautious",
            "is_group": 1
        },
        {
            "category_name": "Business Planning",
            "parent_category": "Strategic Risk",
            "description": "Risks in strategic planning and execution",
            "is_group": 0
        },
        {
            "category_name": "Operational Risk",
            "description": "Risks arising from internal processes and systems",
            "risk_appetite_default": "Minimal",
            "is_group": 1
        },
        {
            "category_name": "Information Security",
            "parent_category": "Operational Risk",
            "description": "Cybersecurity and information protection risks",
            "is_group": 0
        },
        {
            "category_name": "Data Privacy",
            "parent_category": "Operational Risk",
            "description": "Personal data protection and privacy risks",
            "is_group": 0
        },
        {
            "category_name": "Financial Risk",
            "description": "Risks related to financial management",
            "risk_appetite_default": "Averse",
            "is_group": 1
        },
        {
            "category_name": "Compliance Risk",
            "description": "Regulatory and compliance-related risks",
            "risk_appetite_default": "Averse",
            "is_group": 1
        },
        {
            "category_name": "Third Party Risk",
            "description": "Risks from vendors and third parties",
            "risk_appetite_default": "Cautious",
            "is_group": 1
        }
    ]
    
    for cat_data in categories:
        if not frappe.db.exists("Risk Category", cat_data["category_name"]):
            cat = frappe.get_doc({
                "doctype": "Risk Category",
                **cat_data
            })
            cat.insert(ignore_permissions=True)
            print(f"Created Risk Category: {cat.category_name}")
    
    frappe.db.commit()
    return True

def load_compliance_frameworks():
    """Load popular compliance frameworks"""
    frameworks = [
        {
            "framework_name": "ISO 27001:2022",
            "framework_code": "ISO27001",
            "framework_type": "Standard",
            "status": "Active",
            "version": "2022",
            "description": "<p>International standard for information security management systems</p>",
            "issuing_authority": "International Organization for Standardization",
            "industry_sector": "All Sectors",
            "mandatory": 0,
            "framework_url": "https://www.iso.org/standard/27001"
        },
        {
            "framework_name": "SOC 2 Type II",
            "framework_code": "SOC2",
            "framework_type": "Standard",
            "status": "Active",
            "description": "<p>Service Organization Control 2 for service providers</p>",
            "issuing_authority": "AICPA",
            "industry_sector": "Technology",
            "mandatory": 0
        },
        {
            "framework_name": "NIST Cybersecurity Framework",
            "framework_code": "NIST-CSF",
            "framework_type": "Best Practice",
            "status": "Active",
            "version": "1.1",
            "description": "<p>Framework for improving critical infrastructure cybersecurity</p>",
            "issuing_authority": "NIST",
            "industry_sector": "All Sectors",
            "mandatory": 0,
            "framework_url": "https://www.nist.gov/cyberframework"
        },
        {
            "framework_name": "GDPR",
            "framework_code": "GDPR",
            "framework_type": "Regulatory",
            "status": "Active",
            "description": "<p>General Data Protection Regulation for EU data protection</p>",
            "issuing_authority": "European Union",
            "regulatory_body": "European Commission",
            "jurisdiction": "European Union",
            "industry_sector": "All Sectors",
            "mandatory": 1
        },
        {
            "framework_name": "PCI DSS v4.0",
            "framework_code": "PCIDSS",
            "framework_type": "Standard",
            "status": "Active",
            "version": "4.0",
            "description": "<p>Payment Card Industry Data Security Standard</p>",
            "issuing_authority": "PCI Security Standards Council",
            "industry_sector": "Financial Services",
            "mandatory": 1
        }
    ]
    
    for fw_data in frameworks:
        if not frappe.db.exists("Compliance Framework", fw_data["framework_name"]):
            fw = frappe.get_doc({
                "doctype": "Compliance Framework",
                **fw_data
            })
            fw.insert(ignore_permissions=True)
            print(f"Created Framework: {fw.framework_name}")
    
    frappe.db.commit()
    return True

def load_sample_controls():
    """Load sample control sets"""
    controls = [
        {
            "control_id": "AC-001",
            "control_title": "Access Control Policy",
            "control_domain": "Access Control",
            "control_type": "Preventive",
            "control_status": "Implemented",
            "priority": "High",
            "control_objective": "Ensure appropriate access controls are established",
            "control_description": "<p>Establish and maintain access control policy</p>",
            "control_owner": "Administrator",
            "control_effectiveness": "Effective",
            "testing_frequency": "Annually"
        },
        {
            "control_id": "AC-002",
            "control_title": "User Access Review",
            "control_domain": "Access Control",
            "control_type": "Detective",
            "control_status": "Implemented",
            "priority": "High",
            "control_objective": "Regularly review user access rights",
            "control_description": "<p>Conduct periodic review of user access permissions</p>",
            "control_owner": "Administrator",
            "control_effectiveness": "Effective",
            "testing_frequency": "Quarterly"
        },
        {
            "control_id": "IS-001",
            "control_title": "Incident Response Plan",
            "control_domain": "Incident Management",
            "control_type": "Corrective",
            "control_status": "Implemented",
            "priority": "Critical",
            "control_objective": "Respond effectively to security incidents",
            "control_description": "<p>Maintain incident response procedures</p>",
            "control_owner": "Administrator",
            "control_effectiveness": "Effective",
            "testing_frequency": "Quarterly"
        },
        {
            "control_id": "BC-001",
            "control_title": "Business Continuity Plan",
            "control_domain": "Business Continuity",
            "control_type": "Corrective",
            "control_status": "Implemented",
            "priority": "Critical",
            "control_objective": "Ensure business operations continuity",
            "control_description": "<p>Maintain and test business continuity plans</p>",
            "control_owner": "Administrator",
            "control_effectiveness": "Effective",
            "testing_frequency": "Annually"
        },
        {
            "control_id": "DG-001",
            "control_title": "Data Classification",
            "control_domain": "Asset Management",
            "control_type": "Directive",
            "control_status": "Implemented",
            "priority": "High",
            "control_objective": "Classify data according to sensitivity",
            "control_description": "<p>Establish data classification scheme</p>",
            "control_owner": "Administrator",
            "control_effectiveness": "Effective",
            "testing_frequency": "Annually"
        }
    ]
    
    for ctrl_data in controls:
        if not frappe.db.exists("Control Set", {"control_id": ctrl_data["control_id"]}):
            ctrl = frappe.get_doc({
                "doctype": "Control Set",
                **ctrl_data
            })
            ctrl.insert(ignore_permissions=True)
            print(f"Created Control: {ctrl.control_id} - {ctrl.control_title}")
    
    frappe.db.commit()
    return True

def load_all_sample_data():
    """Load all sample data"""
    print("Loading sample data for ES Risk and Compliance Management...")
    print("=" * 70)
    
    try:
        load_risk_categories()
        print("\n✓ Risk categories loaded")
        
        load_compliance_frameworks()
        print("✓ Compliance frameworks loaded")
        
        load_sample_controls()
        print("✓ Sample controls loaded")
        
        print("=" * 70)
        print("Sample data loaded successfully!")
        return True
    except Exception as e:
        print(f"Error loading sample data: {str(e)}")
        frappe.db.rollback()
        return False

if __name__ == "__main__":
    load_all_sample_data()
