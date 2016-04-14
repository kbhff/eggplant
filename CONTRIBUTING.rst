============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/kbhff/eggplant/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

eggplant could always use more documentation, whether as part of the
official eggplant docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/kbhff/eggplant/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

.. _getstarted:

Get Started!
------------

Ready to contribute? Here's how to set up `eggplant` for local development.

If you are completely new to source code versioning using git, please search
for a video explaining it. And ask for help getting a git tool set up on your
machine.

.. note:: We have decided to use the very conventional
          `a simple git branching model <https://gist.github.com/jbenet/ee6c9ac48068889b0912>`_.
          Read the guide to get a good introduction to Git workflows.

::

    $ git clone git@github.com:kbhff/eggplant.git

Virtualenv
~~~~~~~~~~

The project is pretty basic, these are classical just steps. Just make note
that it's a Python 3.4 only project. Enter the git project folder.

::

    $ pip install virtualenvwrapper

To get the mkvirtualenv command you need to::

    source  /usr/local/bin/virtualenvwrapper.sh

On debian this file in::

    /etc/bash_completion.d/virtualenvwrapper

start a new bash session to source it.

::

    $ mkvirtualenv eggplantenv -p python3.4
    $ workon eggplantenv
    $ pip install -r requirements/development.txt
    $ python manage.py syncdb
    $ python manage.py runserver

Use "workon eggplantenv" to activate the eggplan virtual environment,
and "deactivate" to exit.

This will deploy a local SQLite database and run a local webserver. If you are
completely new to Django and Python, notice that you need
`pip <https://pip.pypa.io/en/stable/installing.html>`_, too.


Vagrant
~~~~~~~

(Optional) This takes some time (downloading) and some harddisk capacity.

Another way to get started contributing to this project is to 
download and install git and `Vagrant <http://vagrantup.com/>`_, 
Clone the project (as mentioned above), change directory into the eggplant
folder and then run the following commands:

::

    $ vagrant up
    $ vagrant ssh
    $ python manage.py migrate
    $ python manage.py test
    $ python manage.py createsuperuser
    $ python manage.py runserver

This will download and bootstrap an ubuntu 14.04 vagrant box, connect to it,
start the django development server. The project should now be available at
http://192.168.33.28:8000/.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.4.
   https://travis-ci.org/kbhff/eggplant/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

    $ python manage.py test --tests=eggplant.profiles.tests.TestProfile

