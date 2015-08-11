kotti_frontend
==============

|build status|_
|code coverage|_

.. |build status| image:: https://secure.travis-ci.org/Kotti/kotti_frontend.png?branch=master
.. _build status: http://travis-ci.org/Kotti/kotti_frontend
.. |code coverage| image:: http://codecov.io/github/Kotti/kotti_frontend/coverage.svg?branch=master
.. _code coverage: http://codecov.io/github/Kotti/kotti_frontend?branch=master

``kotti_frontend`` is a **blank sheet** starting point
if you need to build a ``Kotti`` application with a **decoupled**
private content administration area.

So ``kotti_frontend`` is not meant to be used as a standalone
package. Instead you are supposed to include ``kotti_frontend``
as your dependency and do whatever you want, for example:

* CMS public website area with your opinionated frontend toolchain

* heavy Javascript based web applications (SPA)

* minimal web applications with a private content administration
  area

So if you install ``kotti_frontend`` as a standalone package and you run
``pserve development.ini`` you'll obtain:

* http://localhost:5000/cms, the private content administration area

* http://localnost:5000/, not found page (yes, it is correct).
  You are supposed to register the views you need for your application
