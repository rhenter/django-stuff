Installation
============

Requirements
------------

- Python 3.x
- Django 1.11 or later


Getting It
----------

You can get Django Stuff by using pip:

.. code:: shell

    $ pip install django-stuff


If you want to install it from source, grab the git repository from Gitlab and run setup.py:

.. code:: shell

    $ git clone git@github.com:rhenter/django_stuff.git
    $ cd django_stuff
    $ python setup.py install


Installing It
-------------

To enable `django_stuff` in your project you need to add it to `INSTALLED_APPS` in your projects
`settings.py` file:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_stuff',
        ...
    )
