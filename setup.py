from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="es_risk_compliance",
    version="2.0.0",
    description="ES Risk and Compliance Management System",
    author="ES Australia",
    author_email="support@es-au.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
