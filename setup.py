from setuptools import setup, find_packages

setup(
    name='django-urchin',
    version='0.1',
    description='Google Analytics integration for Django',
    author='Inueni Ltd.',
    author_email='info@inueni.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
)
