django-developer-toolkit
========================

Django utility app for Django developers with these features:

- settings constants
- request object data
- debugging email configuration
- internal server error template view
- raise exception view
- environment constants

Tested on Django 1.4.5 and Django 1.8.2


Requirements
------------
- Django


Installation
------------

1. Install python library using pip: ``pip install django-developer-toolkit``

2. Add ``developer_toolkit`` to ``INSTALLED_APPS`` in your Django settings file

3. Include ``developer_toolkit.urls`` in your urls.py


Recommendation
--------------
You may like to add toolkit features to admin. To do so, follow these steps:

1. Add ``os.path.join(ABSOLUTE_PATH_TO_DEVELOPER_TOOLKIT, 'templates'),`` to ``TEMPLATE_DIRS`` in your Django settings file, where ABSOLUTE_PATH_TO_DEVELOPER_TOOLKIT is absolute path to developer toolkit library. For example: ``'/home/project/environment/lib/python2.7/site-packages/developer_toolkit'``

(If you have a better idea how to do that, please let me know. Thanks.)

2. Set ``TEMPLATE_DEBUG`` to True


Authors
-------

Library is by `Erik Telepovsky` from `Pragmatic Mates`_. See `our other libraries`_.

.. _Pragmatic Mates: http://www.pragmaticmates.com/
.. _our other libraries: https://github.com/PragmaticMates
