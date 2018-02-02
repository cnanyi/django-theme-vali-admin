#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='django-vali',
    version='0.0.1',
    description=(
        'a django admin theme using vali-admin'
    ),
    long_description=open('README.rst').read(),
    author='cnanyi',
    author_email='cnanyi@gmail.com',
    maintainer='cnanyi',
    maintainer_email='cnanyi@gmail.com',
    license='MIT License',
    packages=find_packages('vali'),
    platforms=["all"],
    url='https://github.com/cnanyi/django-vali',
    classifiers=[
        'Development Status :: 0 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'Django >= 1.10'
    ]
)