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

****
TODO
****
Do the following in the order specified.

* DONE - Template Testing - get initial pytest/pytest-cookies env working
* DONE - First unit test to test the generated LICENSE file
* DONE - Create **hooks/pre_gen_project.py** see **etc_lib.rst**
* DONE - Create **hooks/post_gen_project.py** see **etc_lib.rst**
* Re-Test with the new cookiecutter.json dictionary format v1.5.1+
* Flesh out rest of cookiecutter.json variables and associated files/code
* Template Documentation
* Template Testing - Write Tests / Run Tests / Debug Tests
* Project Documentation
* Add conditional code generation variables to cookiecutter.json
* Update code to support conditional code generation
* Template Testing - Write Tests / Run Tests / Debug Tests
* Don't forget code coverage
* Deploy to Travis
* Template Testing - Write Tests / Run Tests / Debug Tests
* Project and Template Documentation README badges
* Run Tests
* Investigate tasks.py via Invoke
* Investigate ReadTheDocs deployment (did it with the IMM project)
* Somewhere along the line adopt the latest tools for handling requirements -- pipenv
* Travis autodeployment to PyPI -- see cookiecutter template reference 001



