#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Name

Description....

"""

# ----------------------------------------------------------------------------
# Python Standard Library Imports (one per line)
# ----------------------------------------------------------------------------
import sys

# ----------------------------------------------------------------------------
# External Third Party Python Module Imports (one per line)
# ----------------------------------------------------------------------------
import click

# ----------------------------------------------------------------------------
# Project Specific Module Imports (one per line)
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
__author__ = '{{cookiecutter.author_name}} ({{cookiecutter.author_email}})'
__license__ = '{{cookiecutter.license}} - See LICENSE file in project root'
__copyright__ = "Copyright (C) {% now 'local', ' %Y' %} " \
                "by {{cookiecutter.author_name}}"

# ----------------------------------------------------------------------------
# Module Global & Constant Definitions
# ----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
@click.command()
@click.option('--verbose', is_flag=True, help="Increase verbosity of output")
#-----------------------------------------------------------------------------
def main(verbose):
    if verbose:
        pass

    return 0


# ----------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(main())
