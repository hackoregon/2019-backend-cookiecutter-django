backend-cookiecutter-django
==========================

|Build Status|

A cookiecutter template for creating reusable Django REST Framework
packages with the best practices quickly. This template is customized to
provide structure for quickstarting a Hack Oregon civic data project.

What is Hack Oregon?
--------------------

`Hack Oregon`_ is a rapid prototyping lab taking a creative approach to
data projects that bring insight to complex issues in the public
interest. We’re a community-powered nonprofit, our teams are made of
volunteers, and all the work we do is open source.

Features
--------

-  Tox configuration
-  Sane setup.py for easy PyPI registration/distribution
-  Choice of Open Source License options
-  Standard templates for README, issues and pull requests, Contribution
   guidelines

Requirements
------------

This repo uses the `Cookiecutter`_ templating project. You will need to
install Cookiecutter. The recommended method is by a pip install:

.. code:: bash

   $ pip install cookiecutter

Usage
-----

To generate a new repo:

::

   $ cookiecutter gh:hackoregon/2019-backend-cookiecutter-django --checkout BRANCH

You can leave out the ``--checkout BRANCH`` if checking out from MASTER.

You'll be prompted for some questions, answer them, then it will create
a backend-cookiecutter-django with your new package.

At this point, you are ready to connect with an external git.

Cookiecutter values
~~~~~~~~~~~~~~~~~~~

You will be asked the following information when creating a project:

::

   {
     "full_name": "Your full name here",
     "email": "you@example.com",
     "github_username": "yourname",
     "hack_oregon_team": "Transportation Systems",
     "year": "2019",
     "github_repo": "2019-transportation-systems-backend",
     "python_package_namespace": "hackoregon_transportation_systems",
     "python_subpackage": "toad",
     "project_short_description": "Your project description goes in here",
     "version": "0.1.0",
     "gis_project": "True"
   }

Explanation
~~~~~~~~~~~

-  full_name: Your name as project originator (for credit in
   documentation)
-  email: Your email address
-  github_username: Your github username
-  hack_oregon_team: Canonical name for the Hack Oregon Project Team, ie Transportation Systems or Sandbox
-  github_repo: naming of repo within the hackoregon organization, ie: 2019-transportation-systems-backend
-  python_package_namespace: Namespace to use for project subpackages in public package authority, ex: hackoregon_transportation_systems
-  python_subpackage: Name of the Django Rest Framework subpackage for project code. Cookiecutter will generate a single subpackage, though project may have multiple subpackages
-  project_short_description: A brief description of the project
-  version: initial version of the app, should be 0.1.0 if new project
-  gis_project: Boolean as to whether to include django-restframework-gis package in setup.py dependencies

Example
~~~~~~~

Tests
-----

To run tests on the Cookiecutter generation, please install TOX, which
is a generic virtualenv management and test command line tool.

TOX is avaiable to install from PyPI via pip:

::

   $ pip install tox

It will automatically create a fresh virtual environment

.. _Hack Oregon: http://www.hackoregon.org/
.. _Cookiecutter: https://cookiecutter.readthedocs.io/en/latest/

.. |Build Status| image:: https://travis-ci.org/hackoregon/backend-cookiecutter-django.svg?branch=master
   :target: https://travis-ci.org/hackoregon/backend-cookiecutter-django
