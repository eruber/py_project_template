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


# [LOC1]
def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies"""
    project_path = str(result.project)
    project_slug = os.path.split(project_path)[-1]
    project_dir = os.path.join(project_path, project_slug)
    return project_path, project_slug, project_dir

# ----------------------------------------------------------------------------
# Tests...
# ----------------------------------------------------------------------------


# [LOC1]
def test_year_compute_in_license_file(cookies):
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project.join('LICENSE')
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read()


# [LOC1]
# ["MIT", "BSD3", "ISC", "Apache2", "GNU-GPL-v3", "Not open source"]
def test_bake_selecting_license(cookies):
    license_strings = {
        'MIT': 'MIT License',
        'BSD3': 'Redistributions of source code must retain the above copyright notice, this',
        'ISC': 'ISC License',
        'Apache2': 'Licensed under the Apache License, Version 2.0',
        'GNU-GPL-v3': 'GNU GENERAL PUBLIC LICENSE',
    }
    for license, target_string in license_strings.items():
        with bake_in_temp_dir(cookies, extra_context={'license': license}) as result:
            assert target_string in result.project.join('LICENSE').read()

            # NEED TO ADD a project setup.py file for this to pass
            # already have a template setup.py file, but this one is for
            # the project
            assert license in result.project.join('setup.py').read()


def test_bake_project(cookies):
    result = cookies.bake(extra_context={'project_name': 'TestProject'})

    # p, s, d = project_info(result)
    # print(f"Project Path: {p}")
    # print(f"Project Slug: {s}")
    # print(f" Project Dir: {d}")

    if result.trace_back:
        print(result.trace_back_stack)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'python-testproject'
    assert result.project.isdir()


# ----------------------------------------------------------------------------
if __name__ == "__main__":
    pass
