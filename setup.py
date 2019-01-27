#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

setup_requirements = [
    'bumpversion>=0.5.3',
    'Sphinx>=1.4.8',
    'watchdog>=0.8.3',
    'wheel>=0.29.0',
    # TODO(moodule): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'coverage>=4.1',
    'flake8>=2.6.0',
    'pytest>=2.9.2',
    'pytest-runner>=2.11.1',
    'tox>=2.3.1'
    # TODO: put package test requirements here
]

setup(
    name='dod',
    version='0.0.0',
    description="Instead of writting soon-to-be forgotten todo commentaries in the code, this tool makes them spring back at you. You not only write what what o be done but also when. This is inspired by the gem [todo_or_die](https://github.com/searls/todo_or_die).",
    long_description=readme + '\n\n' + history,
    author="David Mougeolle",
    author_email='david.mougeolle@moodule.net',
    url='https://github.com/moodule/todo-or-die',
    packages=find_packages(include=['dod']),
    entry_points={
        'console_scripts': [
            'dod=dod.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='dod',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
