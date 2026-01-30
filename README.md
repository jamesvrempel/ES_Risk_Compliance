# ES Risk & Compliance v2.0.0 - Clean Build

**A clean, working Risk and Compliance Management module for ERPNext/Frappe**

## 🎯 What's Different in v2.0.0

This is a **complete rebuild** from scratch with:
- ✅ Simplified, focused feature set
- ✅ Guaranteed child table schema creation
- ✅ Proper installation process
- ✅ Clean, validated code structure
- ✅ GitHub-ready repository

## 📦 Features

### Core Modules
1. **Risk Register** - Central risk tracking
2. **Risk Controls** (Child Table) - Controls for each risk
3. **Risk Treatment Plans** (Child Table) - Treatment actions
4. **Risk Categories** - Risk classification

### Key Capabilities
- Risk identification and assessment
- Likelihood and impact scoring (1-5 scale)
- Inherent vs residual risk calculation
- Risk owner assignment
- Control documentation
- Treatment plan tracking

## 🚀 Installation

### Method 1: From GitHub (Recommended)

```bash
# 1. Get the app
bench get-app https://github.com/jamesvrempel/es_risk_compliance

# 2. Install on site
bench --site your-site.com install-app es_risk_compliance

# 3. Restart
bench restart
```

### Method 2: Manual Build

See [MANUAL_BUILD.md](MANUAL_BUILD.md) for complete instructions on building from source.

## ⚠️ CRITICAL: Post-Installation

After installation, the `after_install` hook should create all child table schemas automatically.

**To verify installation worked:**

```bash
bench --site your-site.com mariadb
```

```sql
-- Check child tables exist with parent columns
DESCRIBE `tabRisk Control`;
DESCRIBE `tabRisk Treatment Item`;

-- Both should show: parent, parentfield, parenttype columns
```

**If child tables are missing parent columns**, run the post-install fix:

```bash
bench --site your-site.com console
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

## 📖 Usage

1. Navigate to **ES Risk and Compliance** module
2. Open **Risk Register**
3. Create a new risk
4. Add controls in the **Risk Controls** section
5. Add treatment plans in the **Risk Treatment Plans** section
6. Save

## 🔧 Troubleshooting

### Issue: "Unknown column 'parent'" Error

**Cause:** Child table schemas weren't created during installation.

**Solution:**
```bash
bench --site your-site.com console
```
```python
from es_risk_compliance.install import create_child_table_schemas
create_child_table_schemas()
```

### Issue: yarn install fails

**Cause:** Invalid package.json

**Solution:** The package.json in v2.0.0 is validated and should work. If it fails, check:
```bash
cd apps/es_risk_compliance
python3 -m json.tool package.json
```

## 📝 Version History

### v2.0.0 (2026-01-30)
- Complete rebuild from scratch
- Simplified to core features only
- Guaranteed child table creation
- Clean code structure
- GitHub-ready repository

### v1.x (Deprecated)
- Previous versions had child table schema issues
- Not recommended for new installations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) file

## 🆘 Support

- GitHub Issues: https://github.com/jamesvrempel/es_risk_compliance/issues
- Email: support@es-au.com

## ✅ Verified Working On

- Frappe v15.98+
- ERPNext v15.95+
- Python 3.12
- MariaDB 10.11+

---

**Built by ES Australia** 🇦🇺
