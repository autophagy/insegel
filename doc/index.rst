=======
Insegel
=======

Don't let the name scare you. RST (ReStructured Text) is merely a very
simple yet clever human readable plain text format which can be
automatically converted into HTML (and other formats). This
explanation of RST formatting also doubles as an example.

To see this example in HTML go to:

http://www.turnkeylinux.org/rst-example.html

Paragraphs
----------

Paragraphs are just regular plain text paragraphs. Nothing special
about them. The only rule is that paragraphs are separated by an empty
line.

This is a new paragraph.

Links
-----

Several link formats are available.

A naked link: http://www.example.com/

A link to `My favorite search engine <http://www.google.com>`_.

Another link to Ubuntu_ in a different format.

.. _Ubuntu: http://www.ubuntu.com/

Headlines
---------

We decide something is a headline when it looks like it in plain text.

Technically this means the next line has a row of characters (e.g., -
= ~) of equal length. You've already seen four headline examples
above. It doesn't matter which characters you use so long as they are
not alphanumerics (letters A-Z or numbers 0-9). To signify a deeper
headline level, just use different underline character.

Preformatted text
-----------------

Notice the indentation of the text below and the double colon (I.e.,
::) at the end of this line::

    Preformatted text
    preserves formatting of
    newlines

    Great for code,
    poetry,
    or command line output...

    $ ps

      PID TTY          TIME CMD
      551 ttyp9    00:00:00 bash
    28452 ttyp9    00:00:00 ps

Lists
-----

An *ordered* list of items:

1) A short list item.

2) One great long item with no newlines or whitespace. Garbage
   filler: Proin ac sem. Sed massa. Phasellus bibendum dui eget
   ligula.  Vivamus quam quam, adipiscing convallis, pellentesque
   ut, porta quis, magna.

3) A long item, formatted so that all new lines align with the first.
   Garbage filler: Nam dapibus, neque quis feugiat fringilla, nunc
   magna ultrices leo, vitae sagittis augue quam vel nibh.  Praesent
   vulputate volutpat ligula. Aenean facilisis massa nec nibh.

An *unordered* list of items:

* A list item formatted as one long line. Garbage filler: Lorem
  ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
  risus quam, semper sit amet, posuere et, porttitor in, urna.

* A list item formatted as several lines aligned with the first.
  Garbage filler: Vivamus tincidunt. Etiam quis est sit amet velit
  rutrum viverra.  Curabitur fringilla. Etiam id erat. Etiam posuere
  lobortis augue.

Emphasis
--------

You emphasize a word or phase by putting stars around it. Like *this*.

Single stars provide *weak* emphasis, usually rendered in italics.

Double stars provide **strong** emphasis, usually rendered in bold.