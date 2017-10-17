#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test Project Template

The code below is derived from several locations:

    REFERENCES:
        REF1: https://docs.pytest.org/en/latest/contents.html
        REF2: https://github.com/hackebrot/pytest-cookies

    LOCATIONS
        LOC1: https://github.com/audreyr/cookiecutter-pypackage
        LOC2: https://github.com/mdklatt/cookiecutter-python-app
        LOC3: https://github.com/Springerle/py-generic-project

"""
# ----------------------------------------------------------------------------
# Python Standard Library Imports (one per line)
# ----------------------------------------------------------------------------
import sys
import shlex
import os
import sys
import subprocess
# import yaml
import datetime
from contextlib import contextmanager

if sys.version_info > (3, 2):
    import io
    import os
else:
    raise "Use Python 3.3 or higher"

# ----------------------------------------------------------------------------
# External Third Party Python Module Imports (one per line)
# ----------------------------------------------------------------------------
from cookiecutter.utils import rmtree
# from click.testing import CliRunner


# ----------------------------------------------------------------------------
# Project Specific Module Imports (one per line)
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
__author__ = 'E.R. Uber (eruber@gmail.com)'
__license__ = 'MIT'
__copyright__ = "Copyright (C) 2017 by E.R. Uber"

# ----------------------------------------------------------------------------
# Module Global & Constant Definitions
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# Test Support...
# ----------------------------------------------------------------------------


# [LOC1]
@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


# [LOC1]
@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies, cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


# [LOC1]
def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


# [LOC1]
def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))

# ----------------------------------------------------------------------------
# Tests...
# ----------------------------------------------------------------------------


# [LOC1]
def test_year_compute_in_license_file(cookies):
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project.join('LICENSE')
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read()


# ----------------------------------------------------------------------------
if __name__ == "__main__":
    pass
