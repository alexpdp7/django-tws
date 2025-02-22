# Django Training Wheels

This project is in alpha state and is not ready for general use.

The objective of this project is to improve some rough edges that newcomers to Django can face.

In the meantime, if you do not want with an alpha project, perhaps [Cookiecutter Django](https://cookiecutter-django.readthedocs.io/en/latest/) can work for you.

## Objectives

### Provide an improved Django starter template with [uv](https://docs.astral.sh/uv/)

Most Django projects require more dependencies over Django.
The Python ecosystem has multiple ways of managing project dependencies, but the default Django starter templates do not include any dependency management solution.

### Provide a smoother database experience in development

Django migrations are a reasonable way to manage database schemas.
However, the Django documentation does not explain a pleasant development workflow while exploring the database schema.

Django training wheels provides a `devserver` layer on top of `runserver`
`devserver` recreates the database from scratch, seeds development data, and starts `runserver` with the latest model definitions.

### Showcase typical Django patterns

Django training wheels includes a showcase project.
The showcase project will include:

* A model admin that uses `raw_id_fields` to replace a dropdown to select a value from a related table with a search functionality.
* A model admin that filters the database rows depending on the logged-in user.

### Provide an opinionated project structure

Although Django provides the `startproject` and `startapp` commands, they only guide you slighty towards a simple project structure.

Django newcomers can be confused by projects and apps.

Django training wheels supports the following structure:

* `$PROJECT/dj`
  * `settings.py`
  * `urls.py`
  * `manage.py`
  * `asgi.py`/`wsgi.py`
  * `$APP_1`
  * ...
  * `$APP_n`
* `devserver.py`
* `pyproject.toml`

Where `$PROJECT` is the name of your project.
`$APP_i` are the apps ("Django modules") that form your application.

All Django code is inside `$PROJECT.dj`, so that you place non-Django code in `$PROJECT.*`.

## Usage

```
cd showcase
uv run devserver.py
```

Browse to http://localhost:8000/admin/ and log in as `admin`/`admin`.
