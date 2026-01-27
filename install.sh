#!/bin/bash

# ES Risk and Compliance Management - Automated Installation Script
# This script installs the module on an ERPNext site

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Functions
print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_info() {
    echo -e "${YELLOW}ℹ $1${NC}"
}

# Header
echo "============================================================"
echo "  ES Risk and Compliance Management - Installation"
echo "  Version: 1.0.0"
echo "  (c) 2024 ES Australia"
echo "============================================================"
echo ""

# Check if running in bench directory
if [ ! -f "sites/common_site_config.json" ]; then
    print_error "This script must be run from the frappe-bench directory"
    exit 1
fi

# Get site name
if [ -z "$1" ]; then
    echo "Usage: ./install.sh <site-name>"
    echo "Example: ./install.sh mysite.local"
    exit 1
fi

SITE_NAME=$1

# Verify site exists
if [ ! -d "sites/$SITE_NAME" ]; then
    print_error "Site '$SITE_NAME' does not exist"
    exit 1
fi

print_success "Site '$SITE_NAME' found"

# Check if app already installed
APP_INSTALLED=$(bench --site $SITE_NAME list-apps | grep -c "es_risk_compliance" || true)
if [ $APP_INSTALLED -gt 0 ]; then
    print_info "App is already installed. This will update the existing installation."
    read -p "Continue? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 0
    fi
fi

# Install the app
print_info "Installing ES Risk and Compliance Management..."

if [ $APP_INSTALLED -eq 0 ]; then
    bench --site $SITE_NAME install-app es_risk_compliance
    print_success "App installed"
else
    print_info "App already installed, running migrations..."
fi

# Run migrations
print_info "Running database migrations..."
bench --site $SITE_NAME migrate
print_success "Migrations complete"

# Clear cache
print_info "Clearing cache..."
bench --site $SITE_NAME clear-cache
bench --site $SITE_NAME clear-website-cache
print_success "Cache cleared"

# Rebuild assets
print_info "Building assets..."
bench build --app es_risk_compliance
print_success "Assets built"

# Create roles
print_info "Creating user roles..."
bench --site $SITE_NAME console << 'PYTHON_EOF'
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
PYTHON_EOF
print_success "Roles configured"

# Load sample data
read -p "Load sample data (risk categories, frameworks, controls)? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    print_info "Loading sample data..."
    bench --site $SITE_NAME execute es_risk_compliance.fixtures.sample_data.load_all_sample_data
    print_success "Sample data loaded"
fi

# Restart bench
print_info "Restarting bench..."
bench restart
print_success "Bench restarted"

# Success message
echo ""
echo "============================================================"
print_success "Installation completed successfully!"
echo "============================================================"
echo ""
echo "Next steps:"
echo "  1. Log in to your ERPNext site: http://$SITE_NAME"
echo "  2. Navigate to 'ES Risk and Compliance Management' module"
echo "  3. Start by creating risk categories and frameworks"
echo ""
echo "Documentation: https://github.com/yourusername/es_risk_compliance"
echo "Support: support@es-au.com"
echo ""
