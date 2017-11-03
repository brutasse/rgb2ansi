rgb2ansi
========

Color strings for terminal ouput (ANSI 256 colors) using CSS-style ``rgb``
notation.

Installation
------------

::

    pip install rgb2ansi

Usage
-----

.. code-block:: python

    from rgb2ansi import color

    print(color("Hello", fg='4444ff'), color("world!", bg='ff4400'))


You can pass a foreground (text) color, a background color, or both. The
following inputs are accepted as color parameters:

* Hex strings, e.g. ``ff4400``.
* Byte strings, e.g. ``b'\xff\x44\x00'``
* Sequences of integers, e.g. ``(255, 68, 0)``

Note that ``color()`` is lossy: it simply rounds the color to the closest
8-bit color available.

License
-------

BSD 3-clause.
