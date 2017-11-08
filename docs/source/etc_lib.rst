.. ###########################################################################
   This file contains reStructuredText, please do not edit it unless you are
   familar with reStructuredText markup as well as Sphinx specific markup.

   For information regarding reStructuredText markup see
      http://sphinx.pocoo.org/rest.html

   For information regarding Sphinx specific markup see
      http://sphinx.pocoo.org/markup/index.html

   ###########################################################################

.. ###########################################################################

   Copyright (C) {% now 'local', ' % Y' %} by {{cookiecutter.author_name}}

    Author: {{cookiecutter.author_name}} ({{cookiecutter.author_email}})
   License: {{cookiecutter.project_license}} - See LICENSE file in project root

   ###########################################################################

.. ########################## SECTION HEADING REMINDER #######################
   # with overline, for parts
   * with overline, for chapters
   =, for sections
   -, for subsections
   ^, for subsubsections
   ", for paragraphs

.. ---------------------------------------------------------------------------

*****************
etc/lib Directory
*****************
This **lib** directory is a store for Python modules that support the
conditional code generation in some of the **etc/templates** files. This
conditional code generation is controlled by various settings in
**Cookiecutter.json**.

When support for this conditional code is needed, the appropriate module
in this directory will be copied to the **src** directory's **util**
sub-directory (which may need to be created if it does not already exist).
This is done in the Cookiecutter hook **pre_gen_project.py**.

The Cookiecutter hook **post_gen_project.py** will be used to always delete
this **lib** directory at the end of Cookiecutter generation.

.. note:: Some support software may have associated test modules, as is the
          case with the **config** package.


