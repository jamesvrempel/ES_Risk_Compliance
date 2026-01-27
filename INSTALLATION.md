# Installation Guide - ES Risk and Compliance Management

## Prerequisites

Before installing ES Risk and Compliance Management, ensure you have:

- **ERPNext** version 14.x or 15.x installed and running
- **Frappe Framework** latest stable version
- **Bench** command-line tool
- **Git** for version control
- **System Administrator** access to your ERPNext instance

## Installation Methods

### Method 1: Install from Git Repository (Recommended)

```bash
# Navigate to your bench directory
cd /path/to/frappe-bench

# Get the app from repository
bench get-app https://github.com/yourusername/es_risk_compliance

# Install the app on your site
bench --site yoursite.com install-app es_risk_compliance

# Run migrations
bench --site yoursite.com migrate

# Clear cache and rebuild
bench --site yoursite.com clear-cache
bench --site yoursite.com clear-website-cache
bench build --app es_risk_compliance

# Restart bench
bench restart
```

### Method 2: Install from Local Directory

```bash
# Navigate to your bench directory
cd /path/to/frappe-bench/apps

# Clone or copy the module
git clone /path/to/es_risk_compliance
# OR
cp -r /path/to/es_risk_compliance .

# Install on site
cd ..
bench --site yoursite.com install-app es_risk_compliance
bench --site yoursite.com migrate
bench restart
```

### Method 3: Install from Downloaded Archive

```bash
# Extract the downloaded archive
cd /path/to/frappe-bench/apps
tar -xzf es_risk_compliance-1.0.0.tar.gz

# Install on site
cd ..
bench --site yoursite.com install-app es_risk_compliance
bench --site yoursite.com migrate
bench restart
```

## Post-Installation Setup

### 1. Create Required Roles

```bash
# Access your site
bench --site yoursite.com console
```

```python
# In the Frappe console, create roles
roles = [
    "Risk Manager",
    "Compliance Manager", 
    "Auditor",
    "Security Officer",
    "Policy Manager"
]

for role_name in roles:
    if not frappe.db.exists("Role", role_name):
        role = frappe.get_doc({
            "doctype": "Role",
            "role_name": role_name,
            "desk_access": 1
        })
        role.insert()
        print(f"Created role: {role_name}")
    else:
        print(f"Role already exists: {role_name}")

frappe.db.commit()
```

### 2. Assign Permissions

The module comes with pre-configured permissions. To review or customize:

1. Go to **Setup > Permissions > Role Permissions Manager**
2. Select the relevant DocType (e.g., "Risk Register")
3. Review and adjust permissions for each role

### 3. Load Sample Data (Optional)

```bash
# Load sample risk categories
bench --site yoursite.com execute es_risk_compliance.fixtures.sample_data.load_risk_categories

# Load sample compliance frameworks
bench --site yoursite.com execute es_risk_compliance.fixtures.sample_data.load_compliance_frameworks

# Load sample controls
bench --site yoursite.com execute es_risk_compliance.fixtures.sample_data.load_controls
```

### 4. Configure Module Settings

Navigate to **ES Risk and Compliance Management** module and configure:

#### Risk Management Settings
- Default risk appetite
- Risk matrix thresholds
- Review frequency defaults
- Notification settings

#### Compliance Settings
- Active frameworks
- Assessment schedules
- Control testing frequency
- Compliance thresholds

#### Audit Settings
- Audit cycles
- Finding severity definitions
- Remediation SLAs

## Verification

### Check Installation Status

```bash
# Verify app is installed
bench --site yoursite.com list-apps

# Check for errors
bench --site yoursite.com doctor
```

### Access the Module

1. Log in to your ERPNext instance
2. In the main menu, look for **ES Risk and Compliance Management**
3. Click to see the module workspace

### Test Basic Functionality

1. **Create a Risk Category**
   - Go to: Risk Register > Risk Category
   - Create a new category: "Information Security"

2. **Create a Risk**
   - Go to: Risk Register > Risk Register
   - Create a sample risk entry
   - Verify it saves and calculates risk rating

3. **Create a Compliance Framework**
   - Go to: Compliance > Compliance Framework
   - Create "ISO 27001:2022"
   - Add control sets

## Configuration Options

### Email Notifications

Configure email notifications for:
- Risk review reminders
- Treatment plan due dates
- Compliance assessment schedules
- Audit finding assignments
- Incident alerts

Edit in: **Automation > Notification**

### Workflows

The module includes default workflows for:
- Risk approval workflow
- Assessment approval workflow
- Audit finding resolution workflow

Customize in: **Automation > Workflow**

### Custom Fields

Add custom fields to extend functionality:

```bash
bench --site yoursite.com console
```

```python
# Example: Add custom field to Risk Register
custom_field = frappe.get_doc({
    "doctype": "Custom Field",
    "dt": "Risk Register",
    "label": "Business Unit",
    "fieldname": "custom_business_unit",
    "fieldtype": "Link",
    "options": "Department",
    "insert_after": "risk_owner"
})
custom_field.insert()
frappe.db.commit()
```

## Upgrading

### From Previous Version

```bash
# Pull latest changes
cd /path/to/frappe-bench/apps/es_risk_compliance
git pull origin main

# Migrate
cd ../..
bench --site yoursite.com migrate
bench restart
```

### Backup Before Upgrade

```bash
# Backup database
bench --site yoursite.com backup

# Backup files
bench --site yoursite.com backup --with-files
```

## Troubleshooting

### Common Issues

#### 1. Module Not Appearing
```bash
# Clear cache
bench --site yoursite.com clear-cache
bench restart

# Rebuild
bench build --app es_risk_compliance
```

#### 2. Permission Errors
```bash
# Reset permissions
bench --site yoursite.com execute frappe.clear_cache
bench --site yoursite.com migrate
```

#### 3. Migration Failures
```bash
# Check error log
bench --site yoursite.com console

# View recent error logs
tail -f /path/to/frappe-bench/sites/yoursite.com/logs/web.error.log
```

#### 4. DocType Not Found
```bash
# Reload DocTypes
bench --site yoursite.com reload-doc es_risk_compliance es_risk_compliance risk_register
```

### Getting Help

- **Error Logs**: Check `sites/yoursite.com/logs/`
- **Bench Console**: `bench --site yoursite.com console`
- **GitHub Issues**: Submit issues at repository
- **Email Support**: support@es-au.com

## Uninstallation

If you need to remove the module:

```bash
# Uninstall from site
bench --site yoursite.com uninstall-app es_risk_compliance

# Remove from apps directory (optional)
cd /path/to/frappe-bench/apps
rm -rf es_risk_compliance
```

**Warning**: Uninstalling will remove all data. Backup first!

## Production Deployment

### Performance Optimization

```bash
# Enable production mode
bench --site yoursite.com set-config maintenance_mode 0
bench --site yoursite.com enable-scheduler

# Optimize database
bench --site yoursite.com mariadb
OPTIMIZE TABLE `tabRisk Register`, `tabCompliance Assessment`;
```

### Security Hardening

1. **Enable Two-Factor Authentication**
   - Setup > System Settings > Enable Two Factor Auth

2. **Configure HTTPS**
   ```bash
   bench setup lets-encrypt yoursite.com
   ```

3. **Set Session Timeout**
   - Setup > System Settings > Session Expiry

4. **Enable Audit Trail**
   - Already enabled for critical DocTypes

### Backup Strategy

```bash
# Setup automated backups
bench --site yoursite.com set-config backup_schedule "0 2 * * *"

# Configure backup retention
bench --site yoursite.com set-config backup_retention 30
```

## Multi-Site Installation

Install on multiple sites in same bench:

```bash
# Install on first site
bench --site site1.com install-app es_risk_compliance

# Install on second site  
bench --site site2.com install-app es_risk_compliance

# Migrate all
bench migrate
```

## Docker Installation

If using Frappe Docker:

```dockerfile
# Add to apps.json
{
  "url": "https://github.com/yourusername/es_risk_compliance",
  "branch": "main"
}
```

```bash
# Rebuild images
docker-compose build
docker-compose up -d

# Install app
docker-compose exec backend bench --site yoursite.com install-app es_risk_compliance
```

## Next Steps

After successful installation:

1. **Review Documentation** - Read the user guide
2. **Configure Settings** - Set up organizational preferences
3. **Import Data** - Import existing risk and compliance data
4. **Train Users** - Conduct training sessions
5. **Start Using** - Begin managing risks and compliance

## Support Matrix

| ERPNext Version | ES Risk Compliance Version | Status |
|----------------|---------------------------|---------|
| 15.x | 1.0.0+ | ✅ Supported |
| 14.x | 1.0.0+ | ✅ Supported |
| 13.x | - | ❌ Not Supported |

---

**Installation Support**: support@es-au.com
**Documentation**: https://github.com/yourusername/es_risk_compliance/wiki
