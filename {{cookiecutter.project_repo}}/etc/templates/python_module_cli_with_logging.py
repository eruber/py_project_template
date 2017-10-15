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
import os.path

# ----------------------------------------------------------------------------
# External Third Party Python Module Imports (one per line)
# ----------------------------------------------------------------------------
import click

# ----------------------------------------------------------------------------
# Project Specific Module Imports (one per line)
# ----------------------------------------------------------------------------
import loggingsetup

# ----------------------------------------------------------------------------
__author__ = '{{cookiecutter.author_name}} ({{cookiecutter.author_email}})'
__license__ = '{{cookiecutter.license}} - See LICENSE file in project root'
__copyright__ = "Copyright (C) {% now 'local', ' % Y' %} " \
                "by {{cookiecutter.author_name}}"

# ----------------------------------------------------------------------------
# Module Global & Constant Definitions
# ----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
@click.command()
@click.option('--verbose', is_flag=True, help="Increase verbosity of output")
#-----------------------------------------------------------------------------
def main(verbose):
    log = loggingsetup.Setup(apploggername=sys.argv[0],
                             log_path=os.path.join(os.path.dirname(__file__),
                            'logfile.log'), log_file_backup_count=5)
    logger = log.logger()
    #rootlogger = log.RootLogger()
    log.set_file_handler_logging_level(logging.DEBUG)

    #logger.info("This is a sample info log entry -- goes to both log file and log console")
    #logger.debug("This is a sample debug log entry -- goes only to log file, not log console")

    if verbose:
        # To increase verbosity of logs to the console
        log.set_console_handler_logging_level(logging.DEBUG)

    # Your Code Starts Here

    return 0


# ----------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(main())
