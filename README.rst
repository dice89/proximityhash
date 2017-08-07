ProximityPyHash: Geohashes in Proximity
=======================================

|image0| |Code Health| |PyPI version| |PyPI|

This is a fork of ProximityHash which improved the setup and changed the
dependency towards calculating geohash to pygeohash instead of geohash.

Geohash is a geocoding system invented by Gustavo Niemeyer and placed
into the public domain. It is a hierarchical spatial data structure
which subdivides space into buckets of grid shape, which is one of the
many applications of what is known as a Z-order curve, and generally
space-filling curves.

**ProximityPyHash** generates a set of geohashes that cover a circular
area, given the center coordinates and the radius. It also has an
additional option to use
`GeoRaptor <https://github.com/ashwin711/georaptor>`__ that creates the
best combination of geohashes across various levels to represent the
circle, starting from the highest level and iterating till the optimal
blend is brewed. Result accuracy remains the same as that of the
starting geohash level, but data size reduces considerably, thereby
improving speed and performance.

Usage
-----

::

    $ proximityhash -h


      usage: proximityhash [-h] [--georaptor GEORAPTOR] [--minlevel MINLEVEL]
                         [--maxlevel MAXLEVEL]
                         latitude longitude radius precision_level

      positional arguments:
          latitude              latitude of the center point
          longitude             longitude of the center point
          radius                radius of coverage in metres
          precision_level       geohash precision level

      optional arguments:
          -h, --help            show this help message and exit
          --georaptor GEORAPTOR georaptor flag to compress the output (default: false)
          --minlevel MINLEVEL   minimum level of geohash if georaptor set to true(default: 1)
          --maxlevel MAXLEVEL   maximum level of geohash if georaptor set to true(default: 12)

Example
~~~~~~~

::

    $ proximitypyhash 48.858156 2.294776 1000 7

.. figure:: https://raw.github.com/ashwin711/proximityhash/master/images/proximityhash.png
   :alt: 

::

    $ proximitypyhash 48.858156 2.294776 2000 7 --georaptor true

.. figure:: https://raw.github.com/ashwin711/proximityhash/master/images/proximityhash_georaptor.png
   :alt: 

::

    $ proximitypyhash 48.858156 2.294776 2000 7 --georaptor true --minlevel 3 --maxlevel 6

.. figure:: https://raw.github.com/ashwin711/proximityhash/master/images/proximityhash_georaptor_limited.png
   :alt: 

In-Code Usage Example
~~~~~~~~~~~~~~~~~~~~~

You can use the code also as a library in your application:

::

    import proximitypyhash
    proximitypyhash.get_geohash_radius_approximation(latitude=12.0,longitude=77.0,radius=20.0,precision=8,georaptor_flag=False,minlevel=1,maxlevel=12)

Installation
------------

To install proximitypyhash, simply:

::

    $ pip install proximitypyhash

Development Setup using pyenv
-----------------------------

Install pyenv and pyenv virtualenv:

::

    brew install pyenv
    brew install pyenv-virtualenv

Create and activate the virtualenv:

::

    pyenv virtualenv proximitypyhash
    pyenv activate proximitypyhash
    python setup.py develop

Run the tests

::

    python setup.py test

License:
--------

The code is orginally from Ashwin Nair, I just made some changes to it
to make the setup smoother and added testing functionality with a better
setup.

Licensed under the Apache License, Version 2.0.

::

    Copyright 2017 Ashwin Nair <https://www.linkedin.com/in/nairashwin7>
    Copyright 2017 Alexander Mueller <https://www.linkedin.com/in/alexander-m%C3%BCller-727315a7/>

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

Contributors:
-------------

-  Ashwin Nair [https://github.com/ashwin711]
-  Arjun Menon [http://github.com/arjunmenon92]
-  Alexander Mueller[https://github.com/dice89]

.. |image0| image:: https://travis-ci.org/dice89/proximityhash.svg?branch=master
   :target: https://travis-ci.org/dice89/proximityhash
.. |Code Health| image:: https://landscape.io/github/dice89/proximityhash/master/landscape.svg?style=flat
   :target: https://landscape.io/github/dice89/proximityhash/master
.. |PyPI version| image:: https://badge.fury.io/py/proximitypyhash.svg
   :target: https://badge.fury.io/py/proximitypyhash
.. |PyPI| image:: https://img.shields.io/pypi/pyversions/proximitypyhash.svg
   :target: https://img.shields.io/pypi/pyversions/proximitypyhash.svg
