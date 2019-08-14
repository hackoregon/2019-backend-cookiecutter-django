import os
import re
import sh

import pytest
from binaryornot.check import is_binary

PATTERN = r"{{(\s?cookiecutter)[.](.*?)}}"
RE_OBJ = re.compile(PATTERN)


@pytest.fixture
def context():
    return {
      "full_name": "Your full name here",
      "email": "you@example.com",
      "github_username": "yourname",
      "hack_oregon_team": "Transportation Systems",
      "year": "2019",
      "github_repo": "2019-transportation-systems-backend",
      "project_root_path": "transportation",
      "python_package_namespace": "hackoregon_transportation_systems",
      "python_subpackage": "toad",
      "project_short_description": "Your project description goes in here",
      "version": "0.1.0",
      "gis_project": True
    }


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, subdirs, files in os.walk(root_dir)
        for file_path in files
    ]


def check_paths(paths):
    """Method to check all paths have correct substitutions,
    used by other tests cases
    """
    # Assert that no match is found in any of the files
    for path in paths:
        if is_binary(path):
            continue

        for line in open(path, "r"):
            match = RE_OBJ.search(line)
            msg = "cookiecutter variable not replaced in {}"
            assert match is None, msg.format(path)

def test_default_configuration(cookies, context):
    result = cookies.bake(extra_context=context)
    print(context)
    print(result)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context["github_repo"]
    assert result.project.isdir()

    paths = build_files_list(str(result.project))
    assert paths
    check_paths(paths)

def test_readme(cookies):
    result = cookies.bake()

    readme_file = result.project.join('README.md')
    readme_lines =[]
    with open(readme_file) as f:
        readme_lines.extend(f.readline() for x in range(2))

    assert readme_lines == [
        '# hackoregon_transportation_systems\n', '\n'
    ]
