# whatwasthatbookcalled

A place where users help eachother remember the titles of forgotten books.

Final project for SoftUni Django course.

## Getting Started

### Requirements

-   Python 3.9+
-   [Pipenv](https://pipenv.pypa.io/en/latest/)
-   PostgreSQL 13+

### Installation

Download and install [Pipenv](https://pipenv.pypa.io/en/latest/). In the project directory install all the dependencies through `pipenv`:

```shell
$ pipenv install
```

Activate pipenv environment:

```shell
$ pipenv shell
```

Alternatively, install dependencies from `requirements.txt` and set up a `venv`.

## Configuration

Configuration is done with environment variables. Currently, the following options are supported:

| Name              | Description               | Default     |
| ----------------- | ------------------------- | ----------- |
| POSTGRES_USERNAME | Your PostgreSQL username  | "postgres"  |
| POSTGRES_PASSWORD | Your PostgreSQL password  | "postgres"  |
| POSTGRES_HOST     | Your PostgreSQL host      | "127.0.0.1" |
| SECRET_KEY        | Secret key used by Django | "SECRET"    |

Defaults are set in `config.example.json` which you can edit and rename for easy setup.

### Setup

The project is written in Django. To setup the project in Django you must first run the database migrations.

Run the following command in the pipenv environment:

```shell
$ python manage.py migrate
```

### Usage

To start the app run the following command in the pipenv environment:

```shell
$ python manage.py runserver
```
