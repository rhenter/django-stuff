Generic Models
==============

You just need to add to your template to get the behaviors below. Use as many models as you want.


SlugModel
---------

Model with a slugField already implemented

Usage:

.. code-block:: python

    class YourModel(SlugModel)
       ...


SerializerModel
---------------

Model so you can serialize your instance data returning a dict.

Usage:

.. code-block:: python

    class YourModel(SerializerModel)
        ...

Example of a instance from a Model using the SerializerModel

.. code-block:: python

    instance.serialize()
    {
        'id': 1,
        'name': 'Test'
    }


TimestampedModel
----------------

Model with created_at and updated_at fields to let you know when your instance wore created and updated

Usage:

.. code-block:: python

    class YourModel(TimestampedModel)
        ...

UUIDModel
---------

Model with UUIDPrimaryKeyField already implemented


Usage:

.. code-block:: python

    class YourModel(UUIDModel)
        ...



