# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import versioneer

requires = open('requirements.txt').read().strip().split('\n')

setup(
    name='intake_rolling_zarr',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='S3 manifests plugin for rolling Zarr',
    url='https://github.com/informatics-lab/intake-rolling_zarr',
    maintainer='Theo McCaie',
    maintainer_email='theo.mccaie@informaticslab.co.uk',
    license='BSD',
    py_modules=['intake_rolling_zarr'],
    packages=find_packages(),
    package_data={'': ['*.csv', '*.yml', '*.html']},
    include_package_data=True,
    install_requires=requires,
    long_description=open('README.md').read(),
    zip_safe=False, )
