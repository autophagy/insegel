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

.. _Datárum: https://github.com/Autophagy/datarum
