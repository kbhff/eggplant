# Eggplant 

Eggplant is an open source web application that provides simple and flexible 
infrastructure for organizing food coops and other local
community-driven projects.


## How to get started

### Virtualenv

The project is pretty basic, these are classical just steps. Just make note
that it's a Python 3 only project.

    pip install virtualenv-wrapper  # If you don't have this already
    mkvirtualenv eggplantenv -p python3
    workon eggplant 
    pip install -r requirements/development.txt
    python manage.py syncdb
    python manage.py runserver


This will deploy a local SQLite database and run a local webserver. If you are
completely new to Django and Python, notice that you need [pip](https://pip.pypa.io/en/stable/installing.html), too.


### Vagrant

Another way to get started contributing to this project is to 
download and install git and [Vagrant](http://vagrantup.com/), 
Clone the project, cd into the eggplant folder and then run the followin: 


    vagrant up
    vagrant ssh
    python manage.py migrate
    python manage.py test
    python manage.py createsuperuser
    python manage.py runserver
    python manage.py loaddata eggplant/membership/fixtures/initial_data.json


This will download and bootstrap an ubuntu 14.04 vagrant box, connect to it,
start the django development server. The project should now be 
available at [http://192.168.33.28:8000/](http://192.168.33.28:8000/)


## How to contribute

Read project description, organisation and goals on our GitHub project page:
[http://kbhff.github.io/eggplant/](http://kbhff.github.io/eggplant/)

The list of tickets is available on our Pivotal Tracker project:
[https://www.pivotaltracker.com/n/projects/1337462](https://www.pivotaltracker.com/n/projects/1337462)

We use slack for ad-hoc communication: Just [click to recieve an invitation](https://foodnet-slackin.herokuapp.com/)

The techical discussion takes place on Slack:
[https://foodnet.slack.com/messages/teamblue/](https://foodnet.slack.com/messages/teamblue/)

The design and organisational issues can also be raised on Slack in #teamgreen:
[https://foodnet.slack.com/messages/teamgreen/](https://foodnet.slack.com/messages/teamgreen/)

We decided to follow pep8 and use unix line endings.

*Write code, Write tests, Have fun.*


# Badges OMG OMG OMG

[![Build Status](https://travis-ci.org/kbhff/foodnet.svg?branch=master)](https://travis-ci.org/kbhff/foodnet)

[![Coverage Status](https://coveralls.io/repos/kbhff/foodnet/badge.svg)](https://coveralls.io/r/kbhff/foodnet)
