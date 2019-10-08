# My Diary API

My Diary API is a an application built with Flask(A micro web framework for python) with a REST approach to help users curate life's moments. It serves as the backend architecture powering a full featured client facing application running [on here](https://diaryly.herokuapp.com).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### **Prerequisites**

The followng are softwares you'll need to have installed and running on your system before attemping to get started with the project

```
- Python >= 3.6
- Pipenv >= 2018.1.26
- PostgreSQL >= 9.x
- Git
```

### **Installing**

To get the application running on your local environment, run the following commands

```
- Create a directory (e.g my-diary-api) and cd into it
- Run `git clone https://github.com/jesseinit/my-diary-flask.git .` to pull the code from Github to your machine
- Run `pipenv install` to install the application's dependencies
- Create a `.env` file populating it with actual values using the structure in the `.env.sample` file
- Ensure that you have created a database for development and test environments
```

#### Starting the API

- Run `pipenv shell` to activate the virtual environment(if its not already activated)
- Run `python manage.py runserver` to start the development server

#### Running the tests

- Ensure your're in the virtual environment or run `pipenv shell` to activate it.
- Run the test by running `pipenv run pytest` on the terminal or simply `make tests` if make is enabled on your pc

#### Deployment

This api has been successfully deployed and surrently running on an EC2 instance. I'll update address shortly

#### Built With

- [Flask](https://palletsprojects.com/p/flask/) - The fast and light-weight python micro-framework
- [Pipenv](https://pipenv-fork.readthedocs.io/) - A super configurable python dependency management cli app
- [PostgreSQL](https://www.postgresql.org/) - A production-ready relational database system emphasizing extensibility and technical standards compliance.

## Authors

- **Jesse Egbosionu** - [My Works](https://github.com/jesseinit)

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc
