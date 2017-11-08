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
import os
import os.path
import logging

import tkinter
from tkinter import Tk
from tkinter import ttk

from pprint import pformat

# ----------------------------------------------------------------------------
# External Third Party Python Module Imports (one per line)
# ----------------------------------------------------------------------------
import click

# ----------------------------------------------------------------------------
# Project Specific Module Imports (one per line)
# ----------------------------------------------------------------------------
import loggingsetup

from userhomepath import UserHomePath as Home


import config.configjson as cfg_module
#import config.configyaml as cfg_module

# ----------------------------------------------------------------------------
__author__ = '{{cookiecutter.author_name}} ({{cookiecutter.author_email}})'
__license__ = '{{cookiecutter.project_license}} - See LICENSE file in project root'
__copyright__ = "Copyright (C) {% now 'local', ' %Y' %} " \
                "by {{cookiecutter.author_name}}"

# ----------------------------------------------------------------------------
# Module Global & Constant Definitions
# ----------------------------------------------------------------------------
APP_NAME = 'tempAppName'  # <<------ cookiecutter.VARIABLE????
APP_CFG_DIR = '.' + APP_NAME
USER_HOME_PATH = Home()

CONFIG_FILE_NAME = 'tempAppName.cfg'
CFG_APP_PATH = os.path.join(USER_HOME_PATH, APP_CFG_DIR)
CFG_FILE_PATH = os.path.join(CFG_APP_PATH, CONFIG_FILE_NAME)

LOG_FILENAME = APP_NAME + '.log'
LOG_FULL_PATH = os.path.join(os.path.join(USER_HOME_PATH, APP_CFG_DIR), LOG_FILENAME)

default_config = dict()
default_config['App.Title'] = 'Application Title - Whatever - V' + __version__
default_config['Logger.Name'] = APP_NAME
default_config['Consle.LogLevl'] = 'INFO'
default_config['File.LogLevel'] = 'DEBUG'

#-----------------------------------------------------------------------------
# Should be in its own module


class App(object):
    """
    Sample class provides a sample. This is the class docstring.
    """

    def __init__(self):
        # Read Configuration File or write one from default config structure if
        # there is no configuration file to read
        self.cfgObj = cfg_module.Config(cfgdict=default_config, cfgfile=CFG_FILE_PATH)
        self.cfgD = self.cfgObj.cfg

        self.setupLogging()
        self.ui = MainUI(self.cfgD)

        self.logger.info("App Configuration '%s':" % CFG_FILE_PATH)
        self.logger.info(pformat(self.cfgD, indent=4))

    def setupLogging(self):
        self.log = loggingsetup.Setup(apploggername=self.cfgD["Logger.Name"], log_path=LOG_FULL_PATH)
        self.logger = self.log.Logger()
        #rootlogger = log.RootLogger()
        self.log.SetFileHandlerLoggingLevel(logging.DEBUG)

    def run(self):
        self.ui.run()

#-------------------------------------------------------------------------------
# Should be in its own module


class TopLevelWidget(ttk.Frame):
    """
    """

    def __init__(self, root, parent, cfg=None):
        """
        root - the Top Level widget in the Tk widget tree.
        parent - the widget the QuilburWidget is descended from.
        cfg - an application specific configuration dictionary.
        """
        super().__init__()

        if cfg is None:
            raise ValueError("Missing configuration dictionary!!")

        self.Cfg_Dict = cfg

        self.root = root
        self.parent = parent

        self.loggerName = self.Cfg_Dict["Logger.Name"]
        self.logger = logging.getLogger(self.loggerName)

        self.ExitButton = ttk.Button(self.parent, text="EXIT", command=self._OnExitButtonPressed)
        self.ExitButton.pack()

    def _OnExitButtonPressed(self):
        self.root.AppShuttingDown()

#-------------------------------------------------------------------------------
# Should be in its own module


class MainUI(Tk):
    """
    """

    def __init__(self, cfg_dict):
        """
        cfg_dict is the Configuration Dictionary
        """
        self.loggerName = cfg_dict["Logger.Name"]
        self.logger = logging.getLogger(self.loggerName)
        self.logger.info("Initalizing Graphical User Interface...")

        # invoke the Tk constructor
        super().__init__()

        # hook the Window Manager X icon close event
        self.protocol("WM_DELETE_WINDOW", self.AppShuttingDown)

        self.title(cfg_dict['App.Title'])

        w = 550
        h = 450
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        self.logger.info("Screen Width: %d  Screen Height: %d" % (sw, sh))
        x = (sw / 2) - (w / 2)
        y = (sh / 2) - (h / 2)
        # self.geometry('%dx%d+%d+%d' % (w, h, 12, 12))

        # Open App geometry at specic x,y screen location
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # toplevel is superfluous, self is the toplevel since it is sub-classed
        # from Tk itself
        #self.minsize(width=w, height=h)

        # allow width re-sizing, but not height re-sizing
        self.resizable(width=1, height=1)

        # config file contents
        self.Cfg_Dict = cfg_dict

        #-------------------------------------------------------------------------------------------
        # top frame
        self.topframe = ttk.Frame(self)
        self.topframe.pack(expand=True, fill='both')
        self.topwidget = TopLevelWidget(root=self, parent=self.topframe, cfg=self.Cfg_Dict)
        self.topwidget.pack(expand=True, fill='both')

        # Retrieve toplevel widget and set a minimum size for toplevel window
        #self.toplevel = self.topframe.winfo_toplevel()
        #self.toplevel.minsize(width=750, height=660)
        self.AppStartingUp()

    # ---- BELOW HERE STAYS.

    #-----------------------------------------------------------------------------------------------
    #----------------------------- Startup / Shutdown Methods --------------------------------------
    #-----------------------------------------------------------------------------------------------
    def run(self):
        """
        Calls the Tk mainloop() method to start the User Interface
        """
        self.mainloop()

    def AppStartingUp(self):
        """
        Put in application specific startup code herein
        """
        self.logger.info("Application startup code goes here...")

    def AppShuttingDown(self):
        """
        User selected the Window Manager X widget to close the app
        """
        self.logger.info("Window Manager Shutting Down Application...")

        # Put cleanup code here!!!!!!!!

        self.destroy()

#-------------------------------------------------------------------------------


class ClassThatPassesLogger():
    """
    """

    def __init__(self, logger=None):
        """
        """
        logger_name = __name__ + '.' + self.__class__.__name__
        if logger:
            # Use provided logger
            self._logr = logger.getChild(logger_name)
        else:
            # configure own logger
            logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(module)s:%(funcName)s:%(lineno)d:%(message)s')
            self._logr = logging.getLogger(logger_name)


#-------------------------------------------------------------------------------
class ClassThatDoesNotPassLogger():
    """
    """

    def __init__(self):
        """
        """
        logger_name = __name__ + '.' + self.__class__.__name__

        # configure own logger
        logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(module)s:%(funcName)s:%(lineno)d:%(message)s')
        self._logr = logging.getLogger(logger_name)


#-------------------------------------------------------------------------------
def test():
    pass

#-----------------------------------------------------------------------------


@click.command()
@click.option('--verbose', is_flag=True, help="Increase verbosity of output")
#-----------------------------------------------------------------------------
def main(verbose):
    if verbose:
        pass

    app = App()
    app.run()

    return 0


# ----------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(main())
