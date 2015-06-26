kotti_frontend
==============

This is the ``kotti_frontend`` motto::

    """(even) better development experience and complete frontend freedom"""

``kotti_frontend`` is your public website interface solution
completely decoupled by the Kotti backend and this gives you
much frontend power.

So ``kotti_frontend`` is not a standalone usable product but it is meant
to play with other components:

* ``kotti_frontend`` (http:://localhost:5000/)
  Here you see your public website powered by Kotti

* ``kotti_backend`` (http://localhost:5000/cms)
  It is a private content management area, so access requires authentication.
  Here you manage your contents, manage workflow states and so on.

* REST interface
  If you implement a REST interface you can use Kotti, kotti_frontend and
  kotti_backend as a framework for developing single page web applications with
  heavy Javascript development.
  Pyramid has different REST solutions and this is included in the Kotti roadmap

Kotti itself is a very good, manageable and light CMS and web framework, but if
you adopt a separation among frontend and backend your work will be even more agile.

Why ``kotti_frontend``?

* with ``kotti_frontend`` you don't waste time removing or hiding features or views
  not need by your project, just implement what you need.
  Probably guys with experience with big fat frameworks understand what I mean.

* no CSS or Javascript conflicts with the backend. You won't be influenced at all
  how to integrate your usual frontend toolchain with a framework with its own
  tools or opinions because they are two completely different applications

With ``kotti_frontend`` you can:

* start from a very basic theme
  kotti_frontend provides by default a very basic base theme you can extend.
  The base theme is built with the most recent frontend tools and technologies

* start from scratch
  Things move very fast. Are you strong opinionated about your own tool chain?
  Do you want to use other cutting-edge technologies? Does your project has
  a completely different design that does not fit the usual page layout?
  So start from scratch with a blank theme if you need the maximum control

Since the frontend and the backend are served on the same domain, there is shared
authentication so you can implement toolbar or live edit features (roadmap).

You can run this setup using two different process implementing a shared cookie
authentication by your own playing with domains.
Instead ``kotti_frontend`` use by default a different setup based on a composite
application powered by ``Paste#urlmap``.

This is a still **in progress** and **experimental** plugin so things will change.