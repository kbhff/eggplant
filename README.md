# Foodnet
FoodNet is an open source web application that provides simple and flexible infrastructure for organizing food coops and other local community-driven projects.


## How to get started
The easiers way to get started contributing to this project is to download and install [Vagrant](http://vagrantup.com/), clone the project, cd into the foodnet folder and then run **vagrant up**. This will download and bootstrap an ubuntu 14.04 box and allow you to get started by using the following commands:

* vagrant ssh
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py runserver 0:8000

This will start the django development serve. The project should now be available at [http://192.168.33.28:8000/]()

## How to contribute
Write code, Write tests. Have fun.
