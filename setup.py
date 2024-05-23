from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
   name='python_kerberos_vault_integrator',
   version='1.0.0',
   description='Queue reader with integrated kerberos vault support', 
   author='uug.ai',
   author_email='support@uug.ai',
   long_description=open('README.md').read(),
   long_description_content_type='text/markdown',
   packages=find_packages(),
   install_requires=requirements
)