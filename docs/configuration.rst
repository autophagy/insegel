=============
Configuration
=============

Custom Logo
===========

By default, Insegel's logo is put in the upper-left of the build documentation.
To use a custom logo for your project, use the `html_logo`_ option in your
``conf.py``::

    html_logo = "path/to/my/logo.png"

The path to this new logo has to be relative to the documentation's ``conf.py``
file.

Custom CSS
==========

If you need to modify Insegel's default CSS style, you can provide a custom CSS
stylesheet. To do this, create a folder named ``css`` with a file in it named
``custom.css``. This folder can be anywhere, but is conventionally in the ``_static``
folder. Then, set the `html_static_path`_ option in your configuration file to
the path to the folder that contains ``css/custom.css``.

For example, if the structure was ``_static/css/custom.css`` then your ``conf.py``
file would contain::

    html_static_path = ["_static"]


Sidebar Depth
=============

By default, the theme displays indexes 3 levels deep. To configure this to fewer
levels::

    html_theme_options = {
        'navigation_depth': 1
    }

Local TOC
=========

By default, the theme displays a local TOC, built from each documents headings and subheadings::

    html_theme_options = {
        'local_toc': True
    }


.. _html_logo: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_logo
.. _html_static_path: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_static_path
