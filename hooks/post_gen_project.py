# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
hook file executed after cookiecutter generates the skeleton project

"""
import os


# Is this really true, or should we use __file__ and go up
# one level in the file system tree??
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    pass

    # if '{{ cookiecutter.use_pypi_deployment_with_travis }}' != 'y':
    #     remove_file('travis_pypi_setup.py')

    # if '{{ cookiecutter.create_author_file }}' != 'y':
    #     remove_file('AUTHORS.rst')
    #     remove_file('docs/authors.rst')

    # if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
    #     cli_file = os.path.join('{{ cookiecutter.project.slug }}', 'cli.py')
    #     remove_file(cli_file)

    # if 'Not open source' == '{{ cookiecutter.open_source_license }}':
    #     remove_file('LICENSE')
