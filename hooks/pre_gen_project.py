# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
hook file executed prior to cookiecutter generating the skeleton project

"""
import re

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

package_name = '{{cookiecutter.project_pkg}}'

if not re.match(MODULE_REGEX, package_name):
    print('ERROR: The package_name [%s] in the cookiecutter.json file is not\n'
          'a valid Python module or package name. There should be no spaces,\n'
          'no dashes, and it cannot start with a numeral; however,\n'
          'underscores are permitted.' % package_name)
