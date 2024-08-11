=============
Release Notes
=============

1.X
===

1.4.0
-----

- Added a right sidebar, which holds a local TOC (toggleable).

1.3.1
-----

- Fixed bug where page width was broken with long highlighted code (`#3`_).
- Fixed bug where headers would be doubled when using labels (`#2`_).

.. _#2: https://github.com/autophagy/insegel/issues/2
.. _#3: https://github.com/autophagy/insegel/issues/3

1.3.0
-----

- The option to use datarum/wending dates has been removed, for dependency simplicity.
- Added custom.css for easier third party CSS plugins.
- Updated the layout and search pages to be more compatible with Sphinx 4.2.0.
- Added support for not using a logo, in which case it will default to the project name.


1.2.0
-----

- Added copyright notice to the footer.
- Fixed an incompatability with nbsphinx.
- Added multiple level rendering of sidebar toctrees.
- Theme now uses Gregorian calendar by default.


1.1.0
-----

- Added styling for Sphinx's autodoc/autoclass extension.
- Added support for changing the logo using the ``html_logo`` option.


1.0.2
-----

- Added a ``<code>`` background colour for odd table rows, so that they're distinguishable.


1.0.1
-----

- Fixed footer margins to be in line with other elements.


1.0.0
-----

- Updated the theme to a cleaner, less cluttered one that matches that of `Hrǽw`_.

.. _Hrǽw: https://hraew.autophagy.io/

0.X
===


0.3.0
-----

- Updated the favicon to new Autophagy sigil.
- Fixed datarum version to 0.3.0.

0.2.1
-----

- Removed min-width from body, so that it scales properly on mobile resolutions.
- Changed the default Autophagy sigil.
- Refactored the footer build detail seperation.

0.2.0
-----

- Changed the logo link from ``/`` to the ``master_doc`` setting.
- Updated the ``last_updated`` footer element to use the `Datárum`_ library to
  render documentation updated dates in the Wending format, a custom variant on
  the French Revolutionary calendar.
- Added theme option to disable Wending date display, which then uses regular
  Gregorian dates.
- Changed monospace font stack to use Inconsolata.

.. _Datárum: https://github.com/Autophagy/datarum

0.1.0
-----

First release of Insegel.

Features include:

- 2 column layout with a navigation/search sidebar
- Some basic styling of most Sphinx generated elements
- Default Pygments styling for code blocks
- Footer that displays source link, last commit and last build date
- Some RTD specific stuff (like a hosting message)
- Gracefull tablet/mobile degredation
