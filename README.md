# python-app-template

[
![Test](https://img.shields.io/github/workflow/status/apirogov/python-app-template/test?label=test)
](https://github.com/apirogov/python-app-template/actions?query=workflow:test)
[
![Coverage](https://img.shields.io/codecov/c/github/apirogov/python-app-template)
](https://app.codecov.io/gh/apirogov/python-app-template)
[
![Docs](https://img.shields.io/badge/read-docs-success)
](https://www.pirogov.de/python-app-template/)
[
![PyPIPkgVersion](https://img.shields.io/pypi/v/python-app-template)
](https://pypi.org/project/python-app-template/)

A template with a reasonable basic setup, including:

* black *(formatting)*
* flake8 *(linting)*
* mypy *(type checking)*
* isort *(import sorting)*
* pre-commit *(check/fix the things above and more on each commit)*
* poetry *(dependency and venv management)*
* pytest *(testing)*
* tox *(easily test against multiple Python versions even locally)*
* pytest-cov *(compute coverage, uploaded to codecov.io)*
* pdoc *(generate documentation, deployed to Github Pages)*
* deployment to PyPI on Github Release (pre-configured for TestPyPI)

Inspired by
[Hypermodern Python](https://cookiecutter-hypermodern-python.readthedocs.io/)
and blog posts like [this](https://medium.com/georgian-impact-blog/python-tooling-makes-a-project-tick-181d567eea44).
You can look there for more tools and other choices.

* If you are building a CLI app, consider using [Typer](https://typer.tiangolo.com/)
* If you are building a web app, consider using [FastAPI](https://fastapi.tiangolo.com/)

## Setup

* Change the package name and path to the repository everywhere
* enable/configure Github Pages in the settings
* set tokens in the CI if needed (Codecov, PyPI)

## Development

This project uses [Poetry](https://python-poetry.org/docs/master/) for dependency management.

Clone this repository and run `poetry install`.

Run `pre-commit install` to enable pre-commit hooks for linting and sanity checks.

To locally generate documentation, run `pdoc -o docs python_app_template`.

To locally run tests and get coverage information, use `pytest --cov`.

To run the tests with different Python versions, run `tox`.
For that, you should install the Python versions in the `.python-version` file.
You can use [pyenv](https://github.com/pyenv/pyenv) to do that and switch between them as you please.
