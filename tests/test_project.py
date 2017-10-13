#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test Project Template

The code below is derived from several locations:

    1. https://github.com/audreyr/cookiecutter-pypackage
    2. https://github.com/mdklatt/cookiecutter-python-app
    3. https://github.com/Springerle/py-generic-project
    4. Original content

"""
# ----------------------------------------------------------------------------
# Python Standard Library Imports (one per line)
# ----------------------------------------------------------------------------
from contextlib import contextmanager
import shlex
import os
import sys
import subprocess
import yaml
import datetime

if sys.version_info > (3, 2):
    import importlib
else:
    raise "Use Python 3.3 or higher"

# ----------------------------------------------------------------------------
# External Third Party Python Module Imports (one per line)
# ----------------------------------------------------------------------------
from cookiecutter.utils import rmtree

from click.testing import CliRunner

# ----------------------------------------------------------------------------
# Project Specific Module Imports (one per line)
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
__author__ = '{{cookiecutter.author_name}} ({{cookiecutter.author_email}})'
__license__ = '{{cookiecutter.license}} - See LICENSE file in project root'
__copyright__ = "Copyright (C) {% now 'local', ' % Y' %} " \
                "by {{cookiecutter.author_name}}"

# ----------------------------------------------------------------------------
# Module Global & Constant Definitions
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# Test Support...
# ----------------------------------------------------------------------------


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


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))

# ----------------------------------------------------------------------------
# Tests...
# ----------------------------------------------------------------------------


def test_year_compute_in_license_file(cookies):
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project.join('LICENSE')
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read()


# ----------------------------------------------------------------------------
if __name__ == "__main__":
    pass
