============
Django Stuff
============

|PyPI latest| |PyPI Version| |PyPI License|  |CicleCI Status| |Coverage| |Docs|

Django Stuff is a collection of tools and utilities to make your development with Django simpler.

Requirements
============

- Python 3.x
- Django 1.11 or later

Features
========

- Signals Add methods in your model to do any task before or after save your model

Example using Pre-save signal

Note: This will be made before you save your model

.. code-block:: python

    from django_stuff.models import SignalsModel
    ...

    class YourModel(SignalsModel)
        ...
        def pre_save(self):
            do_something()


- TimeStamp and History models to giving you information like when your record wore created/updated and History Changes
- UUID Model as primary key or not instead of sequence ID.
- Serializer model to return a dict with all data of your django instance.
- Backend to Login using email or username.
- And many other stuff. For more information, see our documentation at `Read the Docs <http://django-stuff.readthedocs.io/en/latest/>`_.

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
`settings.py` file:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_stuff',
        ...
    )


Documentation
=============

Check out the latest ``django-stuff`` documentation at `Read the Docs <http://django-stuff.readthedocs.io/en/latest/>`_


Contributing
============

Please send pull requests, very much appreciated.


1. Fork the `repository <https://github.com/rhenter/django_stuff>`_ on GitHub.
2. Make a branch off of master and commit your changes to it.
3. Install requirements. ``pip install -r requirements-dev.txt``
4. Install pre-commit. ``pre-commit install``
5. Run the tests with ``cd test-django-project; py.test -vv -s``
6. Create a Pull Request with your contribution


.. |Docs| image:: https://readthedocs.org/projects/django-stuff/badge/?version=latest
   :target: http://django-stuff.readthedocs.org/en/latest/?badge=latest
.. |PyPI Version| image:: https://img.shields.io/pypi/pyversions/django-stuff.svg?maxAge=60
   :target: https://pypi.python.org/pypi/django-stuff
.. |PyPI License| image:: https://img.shields.io/pypi/l/django-stuff.svg?maxAge=120
   :target: https://github.com/rhenter/django-stuff/blob/master/LICENSE
.. |PyPI latest| image:: https://img.shields.io/pypi/v/django-stuff.svg?maxAge=120
   :target: https://pypi.python.org/pypi/django-stuff
.. |CicleCI Status| image:: https://circleci.com/gh/rhenter/django-stuff.svg?style=svg
   :target: https://circleci.com/gh/rhenter/django-stuff
.. |Coverage| image:: https://codecov.io/gh/rhenter/django-stuff/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/rhenter/django-stuff
