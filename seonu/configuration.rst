=============
Configuration
=============

Last Updated Format
===================

By default, Insegel uses the `Datárum`_ library to render documentation updated
dates in the Wending format, a custom variant on the French Revolutionary
calendar.

To disable this, and render documentation updated dates in the boring old
Gregorian calendar, set the ``wending_last_updated`` setting to false::

    html_theme_options = {
        'wending_last_updated' : False
    }


Custom Logo
===========

By default, Insegel's logo is put in the upper-left of the build documentation.
To use a custom logo for your project, use the `html_logo`_ option in your
``config.py``::

    html_logo = "path/to/my/logo.png"

The path to this new logo has to be relative to the documentation's ``config.py``
file.


.. _Datárum: https://github.com/Autophagy/datarum
.. _html_logo: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_logo
