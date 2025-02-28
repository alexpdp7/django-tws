# Django training wheels

This project is in alpha state and is not ready for general use.

The objective of this project is to improve some rough edges that newcomers to Django can face.

Additionally, this project includes a Django showcase project that demonstrates how to address common requirements with Django.

## Alternatives

Until this project is not alpha, you might want to look at:

* [Cookiecutter Django](https://cookiecutter-django.readthedocs.io/en/latest/)
* [nanodjango](https://github.com/radiac/nanodjango)

## Usage

### Experiment with the showcase project

[Install uv](https://docs.astral.sh/uv/getting-started/installation/).
Note that uv prints out some instructions you need to follow before you can use it.

Clone this repository, change into the repository directory, and then:

```
cd showcase
uv run devserver.py
```

Browse to http://localhost:8000/admin/ and log in as `admin`/`admin`.

The showcase demonstrates:

* [Demo data](showcase/showcase/dj/app/devserver_data.py) to create different users, groups, and permissions.
* The "user restricted models" admin shows different items to different users.
* The "user restricted models" uses `raw_id_fields` for the user foreign key.

### Create a new Django project

[Install uv](https://docs.astral.sh/uv/getting-started/installation/).

Run:

```
uvx copier copy gh:alexpdp7/django-tws -r project-template destination
```

`copier` creates a `destination` directory.
Change to the `destination` directory and read the `README.md` file for further instructions.

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
The showcase project includes:

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

## Non-objectives

Django training wheels does not intend to be a complete full solution, because I think a complete project can be overwhelming to Django newcomers.
As developers become more acquainted with Django, they can evolve their projects with more functionality.

The following features are explicitly not in scope:

* Any kind of HTML/CSS/JS
* Testing and other static analysis
* Production deployments
* Custom authentication
* Custom user models

Django training wheels is designed to simplify adding these features to projects, but to not pay the complexity overhead until they are necessary.
For example, Django training wheels uses [django-environ](https://github.com/joke2k/django-environ) for configuration, so deployments can use the `$DATABASE_URL` variable in production to connect to the database.

Refer to [alternatives](#alternatives) for other projects that might include these features.

## Probably asked questions

### Are projects created with Django training wheels ready to be deployed and exposed to the Internet?

This is part of the [non-objectives](#non-objectives).
I prefer that you become familiar with the [Django deployment documentation](https://docs.djangoproject.com/en/5.1/howto/deployment/), your chosen deployment method, the [Django deployment checklist](https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/), and any other production readiness checks.
Refer to [alternatives](#alternatives) for other projects that might contain more support for production use.

Although Django training wheels does not provide support for production use, adding production support to projects should not require heavy modification of Django training wheels-produced code.

### How do you support users of Django training wheels?

I do not even use Django training wheels *yet*.
My previous Django projects follow similar patterns, and the next Django projects I create will use Django training wheels.
Feel free to open issues, although I guarantee no support.

Note that you can remove most Django training wheels from a project.
(Although the project/app structure are unfriendly to use of the standard templates in `manage.py` `startapp`.)

### Does Django training wheels support databases other than SQLite?

Not yet.

You can use the `DATABASE_URL` variable to deploy applications connecting to other databases supported by Django.

However, the Django training wheels development workflow currently only supports SQLite.

You can create Django projects that can run in multiple databases, and this can be very convenient.

I would like to add support for PostgreSQL development by using projects such as:

* [ZONKY Embedded Postgres Binaries](https://github.com/zonkyio/embedded-postgres-binaries)
* [PostgreSQL Binaries](https://github.com/theseus-rs/postgresql-binaries)

With these projects, you can run specific versions of PostgreSQL without installing software nor having root privileges.
