#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='django-vali',
    version='0.1.1',
    description=(
        'a django admin theme using vali-admin'
    ),
    long_description=open('README.rst').read(),
    author='cnanyi',
    author_email='cnanyi@gmail.com',
    maintainer='cnanyi',
    maintainer_email='cnanyi@gmail.com',
    license='MIT License',
    packages=['vali'],
    include_package_data=True, 
    platforms=["all"],
    url='https://github.com/cnanyi/django-vali',
    py_modules=['vali'],
    classifiers=[
        'Development Status :: 3 - Alpha',

        # Supported versions of Django
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',

        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',

        # Supported versions of Python
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)