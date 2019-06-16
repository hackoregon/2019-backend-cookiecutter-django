#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys
import setuptools

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def get_version(*file_paths):
    """Retrieves the version from {{cookiecutter.python_package_namespace}}/VERSION"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')

version = get_version("VERSION")

if sys.argv[-1] == 'publish':
    try:
        import wheel
        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.md').read()
history = open('CHANGELOG.md').read()

setup(
    name='{{cookiecutter.python_package_namespace}}',
    version=version,
    description="{{cookiecutter.project_short_description}}",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.fullemail_name}}',
    url='https://github.com/hackoregon/{{cookiecutter.github_repo}}',
    packages=setuptools.find_packages(),
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    keywords='{{cookiecutter.github_repo}}',
    install_requires=[
        'djangorestframework',
        'djangorestframework-gis'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
)
