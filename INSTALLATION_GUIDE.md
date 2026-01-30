# ES Risk & Compliance v2.0.0 - Complete Build & Installation Guide

## 📦 What's Included

This is a **complete, clean-build** Frappe/ERPNext module with:

### DocTypes (4 total)
1. **Risk Register** (Parent, Submittable) - Main risk management DocType
2. **Risk Category** (Parent) - Risk categorization
3. **Risk Control** (Child Table) - Existing controls for risks
4. **Risk Treatment Item** (Child Table) - Treatment actions for risks

### Features
- ✅ Automatic risk rating calculation (Inherent & Residual)
- ✅ Child table schema creation guaranteed via `after_install` hook
- ✅ Role-based permissions (Risk Manager, Auditor, System Manager)
- ✅ Submittable workflow for Risk Register
- ✅ Proper module navigation and desktop icons

---

## 🚀 Installation Methods

### Method 1: From GitHub (Recommended for Development)

```bash
# 1. Clone repository
cd /home/enterprise/frappe-bench
bench get-app https://github.com/jamesvrempel/es_risk_compliance

# 2. Install on site
bench --site demo2.es-au.com install-app es_risk_compliance

# 3. Restart
bench restart
```

### Method 2: From Tarball (Recommended for Production)

```bash
# 1. Extract tarball
cd /home/enterprise/frappe-bench/apps
tar -xzf es_risk_compliance_v2.0.0.tar.gz

# 2. Install on site
cd /home/enterprise/frappe-bench
bench --site demo2.es-au.com install-app es_risk_compliance

# 3. Restart
bench restart
```

---

## ✅ Post-Installation Verification

### 1. Check App Installation

```bash
bench --site demo2.es-au.com list-apps
```

Should show: `es_risk_compliance`

### 2. Verify Child Table Schemas

```bash
bench --site demo2.es-au.com mariadb
```

```sql
-- Check Risk Control table structure
DESCRIBE `tabRisk Control`;

-- Check Risk Treatment Item table structure  
DESCRIBE `tabRisk Treatment Item`;

-- Both should show these columns:
-- name, creation, modified, modified_by, owner, docstatus, parent, parentfield, parenttype, idx
-- Plus the custom fields defined in the DocType
```

### 3. Test Risk Register Creation

1. Open browser: http://demo2.es-au.com
2. Navigate to: **ES Risk and Compliance** module
3. Open: **Risk Register**
4. Click: **New**
5. Fill in required fields:
   - Risk Title: "Test Risk"
   - Risk Owner: Select a user
   - Date Identified: Today
   - Likelihood Score: "3 - Possible"
   - Impact Score: "3 - Moderate"
6. Add a control in "Existing Controls" section
7. Add a treatment item in "Treatment Plans" section
8. **Save**
9. **Submit**

✅ If this works without errors, installation is successful!

---

## 🔧 Troubleshooting

### Issue: "Unknown column 'parent'" Error

**Symptom:** Error when saving Risk Register with child table data

**Cause:** Child table database schemas weren't created during installation

**Solution:**

```bash
bench --site demo2.es-au.com console
```

```python
from es_risk_compliance.install import create_child_table_schemas
create_child_table_schemas()
exit()
```

Then:
```bash
bench restart
```

### Issue: yarn install fails with JSON error

**Symptom:** `error An unexpected error occurred: "package.json: Expected ',' or '}'"`

**Cause:** Invalid package.json (shouldn't happen in v2.0.0)

**Solution:**

```bash
cd /home/enterprise/frappe-bench/apps/es_risk_compliance

# Validate JSON
python3 -m json.tool package.json

# Should output formatted JSON without errors
# If it fails, the package.json is corrupted
```

### Issue: Module doesn't appear in desk

**Symptom:** Can't find "ES Risk and Compliance" module

**Solution:**

```bash
# Clear cache
bench --site demo2.es-au.com clear-cache

# Rebuild
bench build --app es_risk_compliance

# Restart
bench restart
```

Then refresh browser (Ctrl+Shift+R)

### Issue: DocTypes not found

**Symptom:** "DocType Risk Register not found"

**Cause:** Installation didn't complete

**Solution:**

```bash
# Run migrate
bench --site demo2.es-au.com migrate

# Check if DocTypes exist
bench --site demo2.es-au.com mariadb
```

```sql
SELECT name FROM `tabDocType` WHERE module='ES Risk and Compliance';

-- Should show:
-- Risk Register
-- Risk Category  
-- Risk Control
-- Risk Treatment Item
```

---

## 📖 User Guide

### Creating a Risk

1. Go to **ES Risk and Compliance** → **Risk Register** → **New**

2. **Basic Information:**
   - Series: RISK-.####  (auto-generated)
   - Risk Title: Brief description
   - Risk Category: Select or create category
   - Risk Owner: Assign responsible person
   - Status: Identified
   - Priority: Critical/High/Medium/Low
   - Date Identified: When risk was discovered

3. **Risk Description:**
   - Risk Description: Detailed explanation
   - Threat Description: What could go wrong
   - Vulnerability Description: What makes you vulnerable
   - Impact Description: Consequences if risk occurs

4. **Inherent Risk Assessment:**
   - Likelihood Score: 1-5 scale (how likely)
   - Impact Score: 1-5 scale (how severe)
   - Inherent Risk Rating: Auto-calculated

5. **Residual Risk Assessment:**
   - Residual Likelihood: After controls
   - Residual Impact: After controls
   - Residual Risk Rating: Auto-calculated

6. **Existing Controls:**
   - Click "Add Row"
   - Control Name: What control exists
   - Control Type: Preventive/Detective/Corrective
   - Effectiveness: How well it works
   - Responsible Person: Who manages it

7. **Treatment Plans:**
   - Click "Add Row"
   - Treatment Action: What to do
   - Treatment Type: Mitigate/Transfer/Accept/Avoid
   - Priority: Urgency
   - Responsible Person: Who will do it
   - Target Date: When it should be done
   - Status: Track progress

8. **Review Information:**
   - Review Frequency: How often to review
   - Next Review Date: When to review next

9. **Save** (Draft) or **Submit** (Final)

### Managing Risk Categories

1. Go to **ES Risk and Compliance** → **Risk Categories** → **New**

2. Fill in:
   - Category Name: e.g., "Operational Risk"
   - Description: What this category covers
   - Color: Visual identifier

3. **Save**

Now you can assign risks to this category.

---

## 🏗️ Manual Build from Source

If you want to build from source files:

### Prerequisites

- Frappe/ERPNext installed
- bench command available
- Python 3.12+
- Node.js 18+

### Build Steps

1. **Create app directory:**
```bash
cd /home/enterprise/frappe-bench/apps
mkdir es_risk_compliance
```

2. **Copy all source files** to `apps/es_risk_compliance/`
   - package.json
   - setup.py
   - requirements.txt
   - MANIFEST.in
   - LICENSE
   - README.md
   - es_risk_compliance/ (entire directory)

3. **Install dependencies:**
```bash
cd /home/enterprise/frappe-bench
bench setup requirements --python
```

4. **Build assets:**
```bash
bench build --app es_risk_compliance
```

5. **Install on site:**
```bash
bench --site demo2.es-au.com install-app es_risk_compliance
```

6. **Restart:**
```bash
bench restart
```

---

## 📊 Database Schema

### Risk Register (tabRisk Register)
- name (PK)
- risk_title
- risk_category → Risk Category
- risk_owner → User
- risk_status
- priority
- date_identified
- likelihood_score, impact_score
- inherent_risk_rating (calculated)
- residual_likelihood, residual_impact
- residual_risk_rating (calculated)
- docstatus (0=Draft, 1=Submitted, 2=Cancelled)

### Risk Control (tabRisk Control) - Child Table
- name (PK)
- parent → Risk Register
- parentfield = 'existing_controls'
- parenttype = 'Risk Register'
- control_name
- control_type
- control_effectiveness
- implementation_date
- responsible_person → User

### Risk Treatment Item (tabRisk Treatment Item) - Child Table
- name (PK)
- parent → Risk Register
- parentfield = 'treatment_plans'
- parenttype = 'Risk Register'
- treatment_action
- treatment_type
- priority
- responsible_person → User
- target_date
- status
- completion_date

### Risk Category (tabRisk Category)
- name (PK) = category_name
- category_name
- description
- color

---

## 🎯 Risk Rating Matrix

### Likelihood Scale
- 1 - Rare: May occur only in exceptional circumstances
- 2 - Unlikely: Could occur at some time
- 3 - Possible: Might occur at some time
- 4 - Likely: Will probably occur in most circumstances
- 5 - Almost Certain: Expected to occur in most circumstances

### Impact Scale
- 1 - Insignificant: Minimal impact
- 2 - Minor: Some impact, manageable
- 3 - Moderate: Moderate impact, requires management attention
- 4 - Major: Major impact, requires senior management attention
- 5 - Catastrophic: Severe impact, threatens viability

### Risk Rating Calculation
**Rating = Likelihood × Impact**

- **Critical:** 20-25 (Immediate action required)
- **High:** 12-19 (Urgent action required)
- **Medium:** 6-11 (Action plan required)
- **Low:** 1-5 (Monitor and review)

---

## 🔐 Permissions

### Risk Manager
- Full access to all Risk DocTypes
- Can create, edit, delete, submit risks
- Can manage categories

### Auditor
- Read-only access to Risk Register
- Can view all risks and reports
- Cannot modify

### System Manager
- Full administrative access
- Can manage all DocTypes and settings

---

## 📝 Development Notes

### File Structure
```
es_risk_compliance/
├── package.json
├── setup.py
├── requirements.txt
├── MANIFEST.in
├── LICENSE
├── README.md
└── es_risk_compliance/
    ├── __init__.py
    ├── hooks.py
    ├── modules.txt
    ├── config/
    │   ├── desktop.py
    │   └── es_risk_and_compliance.py
    ├── install/
    │   └── __init__.py
    ├── doctype/
    │   ├── risk_register/
    │   │   ├── __init__.py
    │   │   ├── risk_register.json
    │   │   └── risk_register.py
    │   ├── risk_category/
    │   │   ├── __init__.py
    │   │   ├── risk_category.json
    │   │   └── risk_category.py
    │   ├── risk_control/
    │   │   ├── __init__.py
    │   │   ├── risk_control.json
    │   │   └── risk_control.py
    │   └── risk_treatment_item/
    │       ├── __init__.py
    │       ├── risk_treatment_item.json
    │       └── risk_treatment_item.py
    └── public/
```

### Key Design Decisions

1. **Child Tables:** Use `istable=1` flag in JSON to mark as child table
2. **Auto-calculation:** Risk ratings calculated in Python controller `validate()` method
3. **Submittable:** Risk Register uses `is_submittable=1` for workflow
4. **Installation:** `after_install` hook forces child table schema creation

---

## 🆘 Support

- **GitHub Issues:** https://github.com/jamesvrempel/es_risk_compliance/issues
- **Email:** support@es-au.com

---

## ✅ Quality Checklist

Before deploying to production:

- [ ] All 4 DocTypes created successfully
- [ ] Child tables have `parent`, `parentfield`, `parenttype` columns
- [ ] Can create and save Risk Register without errors
- [ ] Risk ratings calculate correctly
- [ ] Child table rows save properly
- [ ] Can submit Risk Register
- [ ] Permissions work as expected
- [ ] Module appears in desk
- [ ] No console errors in browser

---

**Version:** 2.0.0  
**Last Updated:** 2026-01-30  
**Status:** Production Ready ✅
