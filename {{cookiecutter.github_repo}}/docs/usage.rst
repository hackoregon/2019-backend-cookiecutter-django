=====
Usage
=====

To use {{ cookiecutter.python_package_namespace }}.{{ cookiecutter.python_subpackage }} in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        '{{ cookiecutter.python_subpackage }}',
        ...
    )

Add {{ cookiecutter.python_package_namespace }}.{{ cookiecutter.python_subpackage }}'s URL patterns:

.. code-block:: python

    from {{ cookiecutter.python_package_namespace }}.{{ cookiecutter.python_subpackage }} import urls as {{ cookiecutter.python_subpackage }}_urls


    urlpatterns = [
        ...
        url(r'^', include({{ cookiecutter.python_subpackage }}_urls)),
        ...
    ]
