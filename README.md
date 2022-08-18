
<h1>
  <p align="center">
    Quizhero Api (WIP)
  </p>
</h1>

# :book: Overview

This project is a production-ready API for quiz registration to help people practice a subject through quizzes

# :pushpin: Table of Contents

- [:book: Overview](#book-overview)
- [:pushpin: Table of Contents](#pushpin-table-of-contents)
- [:computer: Technologies](#computer-technologies)
- [:rocket: Features](#rocket-features)
- [:construction_worker: How to run](#construction_worker-how-to-run)
  - [To run with Docker Compose](#to-run-with-docker-compose)
  - [To run without Docker Compose](#to-run-without-docker-compose)
  - [To run without Docker Compose and with a SQLite database](#to-run-without-docker-compose-and-with-a-sqlite-database)

# :computer: Technologies
This project was made using the following technologies:

* Django
* Django Rest Framework
* Gunicorn
* Docker
* Pre-Commit
* Docker and Docker Compose

# :rocket: Features

* JWT Authentication
* Quiz CRUD
* Unit Tests

# :construction_worker: How to run
```bash
# Clone Repository
$ git clone https://github.com/MatheusBLopes/quizhero-api.git
```

## To run with Docker Compose
```bash
$ docker-compose build

$ docker-compose up
```

Go to http://localhost:8000/ to see the result.

## To run without Docker Compose

For this project you will need to install [Poetry](https://python-poetry.org/) for package management and provide a PostgreSQL database with the credentials configured in settings.py, after this, run the commands:

```bash
# Install Dependencies
$ poetry install

# Run Aplication
$ python manage.py runserver
```

Go to http://localhost:8000/ to see the result.

## To run without Docker Compose and with a SQLite database

Just change the database config in settings.py:

```python
# Remove this
DATABASES = {
    "default": config(
        "DATABASE_URL",
        cast=parse_db_url,
        default="postgresql://postgres:postgres@db/postgres",
    )
  }

# And put this instead

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
And then run the commands:

```bash
# Install Dependencies
$ poetry install

# Run Aplication
$ python manage.py runserver
```

Go to http://localhost:8000/ to see the result.

Give a ⭐️ if this project helped you!
