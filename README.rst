============
Django Utils
============

|PyPI latest| |PyPI Version| |PyPI License|  |CicleCI Status| |Coverage|

Is a pack a few Utilities for Django


Requirements
============

Django Utils requires Django 2 or later


How to install
==============

Getting It
----------

You can get Django Utils by using pip:

.. code:: shell

    $ pip install django_utils


If you want to install it from source, grab the git repository from Gitlab and run setup.py:

.. code:: shell

    $ git clone git@github.com:rhenter/django_utils.git
    $ cd django_utils
    $ python setup.py install


Installing It
-------------

To enable `django_utils` in your project you need to add it to `INSTALLED_APPS` in your projects
`settings.py` file::

    INSTALLED_APPS = (
        ...
        'django_utils',
        ...
    )


Run the migrations
------------------

To complete the instalation you need to run the migrations right after you have added the `django_utils` to
the `INSTALLED_APPS` on `settings` file in your project folder:

.. code:: shell

    $ cd YOUR-PROJECT
    $ python manage.py migrate


.. |PyPI Version| image:: https://img.shields.io/pypi/pyversions/django-utils.svg?maxAge=360
   :target: https://pypi.python.org/pypi/django-utils
.. |PyPI License| image:: https://img.shields.io/pypi/l/django-utils.svg?maxAge=360
   :target: https://github.com/rhenter/django-utils/blob/master/LICENSE
.. |PyPI latest| image:: https://img.shields.io/pypi/v/django-utils.svg?maxAge=360
   :target: https://pypi.python.org/pypi/django-utils
.. |CicleCI Status| image:: https://circleci.com/gh/rhenter/django-utils.svg?style=svg
   :target: https://circleci.com/gh/rhenter/django-utils
.. |Coverage| image:: https://codecov.io/gh/rhenter/django-utils/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/rhenter/django-utils
