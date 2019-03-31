# Project Title

Recipe RESTful WebAPI.

## Build Status
[![Build Status](https://travis-ci.org/mydjangoprojects/recipe-app-api.svg?branch=master)](https://travis-ci.org/mydjangoprojects/recipe-app-api)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the web app and how to install them

* [Docker](https://docs.docker.com/install/) - Docker provides a way to run applications securely isolated in a container, packaged with all its dependencies and libraries.
* [Docker Compose](https://docs.docker.com/compose/install/) - Compose is a tool for defining and running multi-container Docker applications.


### Installing

Open the terminal, change the directory in which you cloned the repo and just build the docker image by executing:

```
$ docker-compose build
```

## Running the tests

To run the tests execute the following command:
```
$ docker-compose run --rm app sh -c "python manage.py test && flake8"
```
This will test every endpoint and core functionality. And will apply check for codestyle regarding the PEP-8 convention.

## Deployment

1. Open the terminal and clone the repository:
```
$ git clone git@github.com:mydjangoprojects/recipe-app-api.git
```
2. Change the directory and build the docker image by executing:
```
$ cd recipe-app-api
$ docker-compose build
```

## Running

```
$ cd recipe-app-api
$ docker-compose up
```

## Built With
* [Python 3.7.2](https://www.python.org/) - Python is a programming language that lets you work quickly
and integrate systems more effectively.
* [Django](https://www.djangoproject.com/) - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [Django Rest-Framework](https://www.django-rest-framework.org/) - Django REST framework is a powerful and flexible toolkit for building Web APIs.
* [PostgreSQL](https://www.postgresql.org/) - PostgreSQL is a powerful, open source object-relational database.

## Authors

* **Nikolay Nedkov** - [Psykepro](https://github.com/Psykepro)

See also the list of [contributors](https://github.com/mydjangoprojects/recipe-app-api/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/mydjangoprojects/recipe-app-api/blob/master/LICENSE) file for details
