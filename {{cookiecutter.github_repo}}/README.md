# {{ cookiecutter.python_package_namespace }}

![PyPI version](https://badge.fury.io/py/{{cookiecutter.github_repo}}.svg) | [![Build Status](https://travis-ci.org/hackoregon/{{cookiecutter.github_repo}}.svg?branch=master)](https://travis-ci.org/hackoregon/{{cookiecutter.github_repo}})

{{ cookiecutter.project_short_description}}

# Documentation

The full documentation is at http://hackoregon.github.io/{{cookiecutter.github_repo }}


# Features

> -   TODO (add what your project does)

# Data Sources

This API package in this repo is based on the Data Science work in the following projects:

* [{{cookiecutter.data_science_repo_name}}]({{cookiecutter.data_science_repo_url}})

# Quickstart to install package in your own Django Project (Non-Hack Oregon Workflow)

* Install {{ cookiecutter.python_package_namespace }}:  
  `pip install {{ cookiecutter.python_package_namespace }}`

* Add subpackages to your `INSTALLED_APPS`:

  ```python
  INSTALLED_APPS = [     
                      ...     
                      '{{ cookiecutter.python_subpackage }}',     
                      ...
                    ]
  ```

* Add {{ cookiecutter.python_package_namespace }}'s URL patterns:

  ```python
  from {{ cookiecutter.python_package_namespace }}.{{ cookiecutter.python_subpackage }}
  import urls as {{ cookiecutter.python_subpackage }}_urls   

  urlpatterns = [     
                  ...     
                  url(r'^', include({{ cookiecutter.python_subpackage}}_urls)),     
                  ...
                ]
  ```

* Setup your database with a matching schema

* Run the project

# Running Tests

This repo uses pytest and pytest-django to run tests.

For project development work, tests will be run in docker container
using the bin/test.sh script:

# Deployment

This repo is intended to be used in conjunction with a Travis CI based automated deploy chain to push projects to an AWS Fargate cluster

Prerequisites:

* [bumpversion](https://github.com/peritus/bumpversion#installation) - install on local computer, used for version management

Basic Steps:

1. Branches can be pushed/merged in Github. Automated tests will be run. Unless a tagged push is made, app will not deploy
2. When ready to deploy a new version, you'll confirm you have merged all latest code into your deployment branch (perhaps master?) and have this pulled to your local computer

3. Create a tagged commit using bumpversion, following semantic versioning:
v[major].[minor].[patch]

Lets take an example:
If the current version was `v1.10.4` and you wanted to update the minor portion (ie: a non-breaking but significant change), you will run the following command:

```
bumpversion minor --config-file ./{{cookiecutter.python_package_namespace}}/setup.cfg
```

this would then update the version to `v1.11.0`

to then create a patch update,

```
bumpversion patch --config-file ./{{cookiecutter.python_package_namespace}}/setup.cfg
```
Version will then become: `v1.11.1`

In the background - `bumpversion` checks in the `setup.cfg` file for any `bumpversion:file` entries for which to regex for the version tag syntax, which in this case is the VERSION file which contains the current version. Bumpversion then looks at the part you specify and updates that portion accordingly

Additionally and importantly for the deploy chain, it will also add a `git tag` with the version number.

4. Once you have created the new tagged version of your repo, you can go ahead and push a tagged release to github:

```
git push origin <version-tag>
```
5. Once you push this, Travis should run through it's testing/build cycle and then provided necessary env variables are configured in Travis and AWS services, deploy to the cloud.


# Credits

Tools used in rendering this package:

 * [Cookiecutter](https://github.com/audreyr/cookiecutter)
 * [cookiecutter-djangopackage](https://github.com/pydanny/cookiecutter-djangopackage)
