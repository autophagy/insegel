=============
Configuration
=============

Last Updated Format
===================

By default, Insegel uses the Gregorian calendar to render documentation updated
dates. To use the `Datárum`_ library to render documentation updated
dates in the Wending format, a custom variant on the French Revolutionary
calendar::

    html_theme_options = {
        'wending_last_updated' : True
    }


Custom Logo
===========

By default, Insegel's logo is put in the upper-left of the build documentation.
To use a custom logo for your project, use the `html_logo`_ option in your
``config.py``::

    html_logo = "path/to/my/logo.png"

The path to this new logo has to be relative to the documentation's ``config.py``
file.


Sidebar Depth
=============

By default, the theme displays indexes 3 levels deep. To configure this to fewer
levels::

    html_theme_options = {
        'navigation_depth': 1
    }


.. _Datárum: https://github.com/Autophagy/datarum
.. _html_logo: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_logo
