#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='django-vali',
    version='0.2.0',
    description="a django admin theme using vali-admin with bootstrap4",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author='cnanyi',
    author_email='cnanyi@gmail.com',
    maintainer='cnanyi',
    maintainer_email='cnanyi@gmail.com',
    license='MIT License',
    # include_package_data=True,
    platforms=["all"],
    url='https://github.com/cnanyi/django-vali',
    packages=['vali'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Supported versions of Django
        'Framework :: Django :: 2.0',

        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',

        # Supported versions of Python
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)