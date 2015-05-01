# Foodnet
FoodNet is an open source web application that provides simple and flexible 
infrastructure for organizing food coops and other local
community-driven projects.


## How to get started
The easiers way to get started contributing to this project is to 
download and install git and [Vagrant](http://vagrantup.com/), 
Clone the project, cd into the foodnet folder and then run the followin: 


    vagrant up
    vagrant ssh
    python manage.py migrate
    python manage.py test
    python manage.py createsuperuser
    python manage.py runserver 0:8000

This will download and bootstrap an ubuntu 14.04 vagrant box, connect to it,
start the django development server. The project should now be 
available at [http://192.168.33.28:8000/]()


## How to contribute

Read project description, organisation and goals on our GitHub project page:
[http://kbhff.github.io/foodnet/]()

The list of tickets is available on our Taiga project:
[http://taiga.socialsquare.dk/project/foodnet/backlog]()

The techical discussion takes place on Slack:
[https://foodnet.slack.com/messages/teamblue/]()

The design and organisational issues can also be raised on Slack in #teamgreen:
[https://foodnet.slack.com/messages/teamgreen/]()

We decided to follow pep8 and use unix line endings.

*Write code, Write tests, Have fun.*
