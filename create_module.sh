#!/bin/bash

# ES Risk and Compliance Management Module Creator
# Inspired by 6clicks.com functionality

echo "Creating ES Risk and Compliance Management module structure..."

# Create main module directories
mkdir -p es_risk_compliance/es_risk_compliance
mkdir -p es_risk_compliance/es_risk_compliance/{config,public,templates,www}
mkdir -p es_risk_compliance/es_risk_compliance/fixtures
mkdir -p es_risk_compliance/es_risk_compliance/risk_management
mkdir -p es_risk_compliance/es_risk_compliance/compliance_management
mkdir -p es_risk_compliance/es_risk_compliance/audit_management
mkdir -p es_risk_compliance/es_risk_compliance/vendor_management
mkdir -p es_risk_compliance/es_risk_compliance/incident_management
mkdir -p es_risk_compliance/es_risk_compliance/custom_registers

# Initialize git repository
cd es_risk_compliance
git init

echo "Module structure created successfully!"
