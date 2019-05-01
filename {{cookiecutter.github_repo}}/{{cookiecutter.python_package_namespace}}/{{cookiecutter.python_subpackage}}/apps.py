from django.apps import AppConfig


class {{ cookiecutter.python_subpackage|title|replace(' ','') }}Config(AppConfig):
    name = '{{cookiecutter.python_subpackage}}'
