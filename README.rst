====================
Django Bootstrapped
====================

Bootstrapped is a reusable Django application to quickly integrate the Bootstrap toolkit from Twitter.  It's a
collection of the bootstrap toolkit files and template tags to display them.

This application depends on django.contrib.staticfiles.

No files from Twitter's Bootstrap toolkit have been modified and retain their Apache 2.0 license.

    * Note: This app only works on Django 1.3 and newer.

Installation
============

pip install django-bootstrapped


Configuration
=============

#. Add the `bootstrapped` directory to your Python path.

#. Ensure `django.contrib.staticfiles` is added to your `INSTALLED_APPS` setting.

#. Ensure `django.contrib.staticfiles` is configured properly.

#. Add `bootstrapped` to your `INSTALLED_APPS` setting.

#. Run `manage.py collectstatic` to copy the Twitter Bootstrap toolkit files to your static directory.


Template Usage
==============

Loading bootstrap
-----------------

::

    {% include "bootstrap/medias.inc.html" %}

Output::

    <link rel="stylesheet" type="text/css" href="/static/bootstrap/css/bootstrap.css">
    <script src="/static/bootstrap/js/bootstrap.js" type="text/javascript"></script>


Loading bootstrap uncompressed
------------------------------

::
    {% with dev=true %}
    {% include "bootstrap/medias.inc.html" %}
    {% endif %}

Output::

    <link rel="stylesheet" type="text/css" href="/static/bootstrap/css/bootstrap.min.css">
    <script src="/static/bootstrap/js/bootstrap.min.js" type="text/javascript"></script>


```bootstrap_less```

::

    {% bootstrap_less %}

Output::

    <script src="/static/bootstrap/js/less-1.1.5.min.js" type="text/javascript"></script>
