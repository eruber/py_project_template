# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup module
    - Configure project packaging
    - Support command line interface for running various packaging tasks

See:
    https://packaging.python.org/tutorials/distributing-packages/
    https://github.com/pypa/sampleproject/blob/master/setup.py
"""

# ----------------------------------------------------------------------------
__author__ = 'E.R. Uber (eruber@gmail.com)'
__license__ = 'MIT'
__copyright__ = "Copyright (C) 2917 by E.R. Uber"
# ----------------------------------------------------------------------------

import sys


# Always prefer setuptools over distutils
from setuptools import setup
# from distutils.core import setup

# ----------------------------------------------------------------------------
# Uncomment this section of code to read the long descrption from the README
# ----------------------------------------------------------------------------
"""
from setuptools import find_packages

# To use a consistent encoding
from codecs import open
from os import path

project_root = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(project_root, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

"""


# ----------------------------------------------------------------------------

# All preferred keyword directives are documented below,
# some may not be needed and are thus commented out, or empty.
setup(
    name='python-project-skeleton',
    packages=[],
    version='0.1.0',
    description='General purpose Python project template of optional scope',
    # long_description=long_description,
    author='E.R. Uber',
    author_email='eruber@gmail.com',
    license='MIT',
    url='https://github.com/eruber/python-project-skeleton',

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development',
    ],

    keywords='cookiecutter template project development skeleton',

    # Python 3.3 and up but not willing to commit to Python 4 support yet.
    # For more examples, see:
    # https://packaging.python.org/tutorials/distributing-packages/#python-requires
    python_requires='~=3.3',

    # Run-time Dependencies
    # Specify what dependencies are minimally needed to run. When the project
    # is installed by pip, this is the specification that is used to install
    # its dependencies. For more details, see:
    # https://packaging.python.org/tutorials/distributing-packages/#install-requires
    # https://packaging.python.org/discussions/install-requires-vs-requirements/
    install_requires=[],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        # 'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },

    # To install additional data files INTERNAL to a package, use this directive.
    # These files are often data that’s closely related to the package’s
    # implementation, or text files containing documentation that might be of
    # interest to programmers using the package. These files are called
    # “package data”.
    #
    # The value must be a mapping from package name to a list of relative path
    # names that should be copied into the package. The paths are interpreted
    # as relative to the directory containing the package.
    #
    # For more details, see:
    #  https://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files
    package_data={
        # 'sample': ['package_data.dat'],
    },

    # To install additonal data files OUTSIDE of a package, use this directive.
    # Although configuring package_data above is sufficient for most needs,
    # in some cases you may need to place data files OUTSIDE of the package.
    #
    # Each (directory, files) pair in the sequence specifies the installation
    # directory and the files to install there. If directory is a relative
    # path, it is interpreted relative to the installation prefix
    # (Python’s sys.prefix for pure-Python distributions, sys.exec_prefix for
    # distributions that contain extension modules). Each file name in files
    # is interpreted relative to the setup.py script at the top of the project
    # source distribution.
    #
    # For more details, see:
    # https://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    data_files=[
        # ('my_data', ['data/data_file'])
    ],

    # Use this keyword directive to specify any named entry points or plugins
    # that may be defined by the project or by other project dependencies.
    #
    # For more details, see:
    # https://setuptools.readthedocs.io/en/latest/setuptools.html#dynamic-discovery-of-services-and-plugins
    #
    # The preferred to achieve cross-platform compatibility is to use the
    # 'console_scripts' keyword to register entry points. The toolchain will
    # handling turning these interfaces into actual platform scripts during
    # installation of the package.
    #
    # For more detail, see:
    # https://setuptools.readthedocs.io/en/latest/setuptools.html#automatic-script-creation
    entry_points={
        'console_scripts': [
            # 'sample=sample:main',
        ],
    },
)
