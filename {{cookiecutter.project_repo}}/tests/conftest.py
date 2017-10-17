#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=
"""
conftest

Add custom test fixtures to be used during testing of this Cookiecutter
Template with pytest.

For details about how to use pytest see:

    http://pythontesting.net/start-here/
    https://docs.pytest.org/en/latest/contents.html
    https://docs.pytest.org/en/latest/fixture.html#fixtures

These test fixtures will be used by the test code in the various
test_*.py files co-located with this file.

"""

# ----------------------------------------------------------------------------
# Python Standard Library Imports (one per line)
# ----------------------------------------------------------------------------
import os
import shutil
import logging
import subprocess

# ----------------------------------------------------------------------------
# External Third Party Python Module Imports (one per line)
# ----------------------------------------------------------------------------
import pytest

# ----------------------------------------------------------------------------
# Project Specific Module Imports (one per line)
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
__author__ = 'E.R. Uber (eruber@gmail.com)'
__license__ = 'MIT'
__copyright__ = "Copyright (C) 2917 by E.R. Uber"

# ----------------------------------------------------------------------------
# Module Global & Constant Definitions
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Globally available fixtures


# From:
# https://github.com/Springerle/py-generic-project/blob/master/tests/conftest.py
@pytest.fixture(scope='session')
def project():
    """Materialize cookiecutter template (once)."""
    new_project = 'new-project'

    if os.path.exists(new_project):
        shutil.rmtree(new_project)
    subprocess.check_call(['cookiecutter', '--no-input', '.'])

    return os.path.abspath(new_project)


# From:
# https://github.com/Springerle/py-generic-project/blob/master/tests/conftest.py
@pytest.fixture(scope='session')
def logger():
    """Test logger instance as a fixture."""
    logging.basicConfig(level=logging.DEBUG)
    return logging.getLogger('tests')


# ----------------------------------------------------------------------------
if __name__ == "__main__":
    pass
