from setuptools import setup, find_packages
from distutils.core import setup, Extension

setup(
    name='data-db',
    description='',
    packages=['data_db','data_db.tables','data_db.commands'],
    include_package_data=True,
    entry_points = {
        'console_scripts': ['data-db = data_db.main:main'],
        },
    ext_modules = [],
    platforms='any'
)
