#!/usr/bin/env python
import codecs

from setuptools import setup, find_packages

dependencies = ['ruamel.yaml==0.15.97']

def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()


setup(
    name='ytool',
    version=open('VERSION').read(),
    description='A simple tool to set values in yaml files preserving format and comments',
    long_description=open('README.rst').read(),
    url='https://github.com/codacy/ytool',
    author='Codacy',
    author_email='team@codacy.com',
    scripts=['bin/ytool'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(),
    install_requires=dependencies,
    include_package_data=True
)
