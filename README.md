# Backend


## Description
This is the backend for the Elea Africa web app.


## Author


* [**Brian Major**](https://github.com/bryomajor)

## Features


As an admin of the web application you will be able to:

1. Post, edit and delete events
2. Generate APIs
2. Consume data from the APIs

## Specifications
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| Admin visits the app dashboard  | Admin logs in | Directed to the dashboard | 
Events load | Admin clicks on an event | Event details show |
|  Add button displays | Admin clicks on add button | Form appears where one can post an event from.


## Getting started
### Prerequisites
* python3.6
* virtual environment
* pip

### Cloning
* In your terminal:
        
        $ git clone https://github.com/bryomajor/elea-africa.git
        $ cd elea-africa/django

## Running the Application
* Install virtual environment using `$ python3.6 -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all the dependencies from the requirements.txt file by running `python3.6 pip install -r requirements.txt`
* Create a database and edit the database configurations in `settings.py` to your own credentials.
* Make migrations

        $ python manage.py makemigrations api
        $ python3.6 manage.py migrate 

* To run the application, in your terminal:

        $ python3.6 manage.py runserver
        
        
## Technologies Used
* Python3.6
* Django

This application is developed using [Python3.6](https://www.python.org/doc/) and [Django](https://www.djangoproject.com/).


## Support and Team
Brian Major


[Slack Me!](https://slack.com/intl/en-ke/)  @bryomajor


### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license/MIT)
