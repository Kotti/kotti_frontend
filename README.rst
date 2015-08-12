**[IMPORTANT]** There is no need to a blank sheet solution because you can easily switch off all the things you don't need using the ``kotti.base_configure`` option. So kotti_frontend doesn't make sense anymore. The public frontend CMS implementation decoupled from the kotti backend development continues here https://github.com/substancek/substancek_cms_theme

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

``kotti_frontend`` is not meant to be used as a standalone
package. Instead you are supposed to include ``kotti_frontend``
as your dependency and do whatever you want.

If you install ``kotti_frontend`` as a standalone package and you run
``pserve development.ini`` you'll obtain:

* http://localhost:5000/cms. The private content administration area

* http://localhost:5000/. Nothing (not found page).
  Yes, it is correct because you are supposed to register the views
  you need for your application

With ``kotti_frontend`` you don't waste time removing or hiding
features or views not needed by your project and no CSS/Javascript conflicts
because you are supposed to implement or include what your you need.

The separation among frontend and backend (private content management area)
let you build applications with the maximum flexibility and without
being influenced by how the backend is built because they are two
separate applications.

For example you can use ``kotti_frontend`` as a good starting point for:

* CMS public website area with your opinionated frontend toolchain

* heavy Javascript based web applications (SPA)

* minimal web applications with a private content administration
  area
