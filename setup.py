from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
   name='uugai_python_kerberos_vault',
   version='1.2.0',
   description='Kerberos Vault Python library for interacting with the Kerberos Vault.', 
   author='uug.ai',
   author_email='support@uug.ai',
   long_description=open('README.md').read(),
   long_description_content_type='text/markdown',
   packages=find_packages(),
   install_requires=requirements
)