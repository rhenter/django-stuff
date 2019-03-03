============
Django Stuff
============

|PyPI latest| |PyPI Version| |PyPI License|  |CicleCI Status| |Coverage|

Is a pack a few Utilities for Django


Requirements
============

Django Stuff requires Django 1.11 or later


How to install
==============

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
`settings.py` file::

    INSTALLED_APPS = (
        ...
        'django_stuff',
        ...
    )


Run the migrations
------------------

To complete the instalation you need to run the migrations right after you have added the `django_stuff` to
the `INSTALLED_APPS` on `settings` file in your project folder:

.. code:: shell

    $ cd YOUR-PROJECT
    $ python manage.py migrate


.. |PyPI Version| image:: https://img.shields.io/pypi/pyversions/django-stuff.svg?maxAge=360
   :target: https://pypi.python.org/pypi/django-stuff
.. |PyPI License| image:: https://img.shields.io/pypi/l/django-stuff.svg?maxAge=360
   :target: https://github.com/rhenter/django-stuff/blob/master/LICENSE
.. |PyPI latest| image:: https://img.shields.io/pypi/v/django-stuff.svg?maxAge=360
   :target: https://pypi.python.org/pypi/django-stuff
.. |CicleCI Status| image:: https://circleci.com/gh/rhenter/django-stuff.svg?style=svg
   :target: https://circleci.com/gh/rhenter/django-stuff
.. |Coverage| image:: https://codecov.io/gh/rhenter/django-stuff/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/rhenter/django-stuff
