=============================
{{ cookiecutter.python_package_namespace }}
=============================

.. image:: https://badge.fury.io/py/{{ cookiecutter.github_repo }}.svg
    :target: https://badge.fury.io/py/{{ cookiecutter.github_repo }}

.. image:: https://travis-ci.org/hackoregon/{{ cookiecutter.github_repo }}.svg?branch=master
    :target: https://travis-ci.org/hackoregon/{{ cookiecutter.github_repo }}

{{ cookiecutter.project_short_description}}

Documentation
-------------

The full documentation is at http://hackoregon.github.io/{{ cookiecutter.github_repo }}

Quickstart
----------

Install {{ cookiecutter.python_package_namespace }}::

    pip install {{ cookiecutter.python_package_namespace }}

Add subpackages to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        '{{ cookiecutter.python_package_namespace }}.{{ cookiecutter.python_subpackage }}',
        ...
    )

Add {{ cookiecutter.python_package_namespace }}'s URL patterns:

.. code-block:: python

    from {{ cookiecutter.python_package_namespace }}.{{ cookiecutter.python_subpackage }} import urls as {{ cookiecutter.python_subpackage }}_urls


    urlpatterns = [
        ...
        url(r'^', include({{ cookiecutter.python_subpackage }}_urls)),
        ...
    ]
