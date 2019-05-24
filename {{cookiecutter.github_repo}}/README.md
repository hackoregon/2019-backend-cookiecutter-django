|
--------------------------------------------- |
{{ cookiecutter.python_package_namespace }} |

[![image](<https://badge.fury.io/py/>{{ cookiecutter.github_repo
}}.svg)](<https://badge.fury.io/py/>{{ cookiecutter.github_repo }})

[![image](<https://travis-ci.org/hackoregon/>{{
cookiecutter.github_repo
}}.svg?branch=master)](<https://travis-ci.org/hackoregon/>{{
cookiecutter.github_repo }})

{{ cookiecutter.project_short_description}}

# Documentation

The full documentation is at <<http://hackoregon.github.io/>>{{
cookiecutter.github_repo }}

# Features

> -   TODO (add what your project does)

# Data Sources

# Quickstart to install package in your own Django Project (Non-Hack
Oregon Workflow)

Install {{ cookiecutter.python_package_namespace }}:

> pip install {{ cookiecutter.python_package_namespace }}

Add subpackages to your `INSTALLED_APPS`:

`` ` python INSTALLED_APPS = (     ...     '{{ cookiecutter.python_subpackage }}',     ... ) ```

Add {{ cookiecutter.python_package_namespace }}'s URL patterns:

`` ` python from {{ cookiecutter.python_package_namespace }}.{{ cookiecutter.python_subpackage }} import urls as {{ cookiecutter.python_subpackage }}_urls   urlpatterns = [     ...     url(r'^', include({{ cookiecutter.python_subpackage }}_urls)),     ... ] ```

Setup your database with a matching schema

Run the project

# Running Tests

This repo uses pytest and pytest-django to run tests.

For project development work, tests will be run in docker container
using the bin/test.sh script:

# Credits

Tools used in rendering this package:

> -   [Cookiecutter](<https://github.com/audreyr/cookiecutter>)
> -   [cookiecutter-djangopackage](<https://github.com/pydanny/cookiecutter-djangopackage>)
