from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="es_risk_compliance",
    version="1.0.0",
    author="ES Australia",
    author_email="support@es-au.com",
    description="Comprehensive Risk and Compliance Management for ERPNext",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/es_risk_compliance",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Enterprises",
        "Topic :: Office/Business :: Enterprise Resource Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Framework :: Frappe",
    ],
    python_requires=">=3.10",
    install_requires=[
        # No additional requirements - Frappe/ERPNext provides all dependencies
    ],
    include_package_data=True,
    zip_safe=False,
)
