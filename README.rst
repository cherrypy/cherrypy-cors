.. image:: https://img.shields.io/pypi/v/cherrypy-cors.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/cherrypy-cors.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/cherrypy-cors

.. image:: https://github.com/cherrypy/cherrypy-cors/workflows/Automated%20Tests/badge.svg
   :target: https://github.com/cherrypy/cherrypy-cors/actions?query=workflow%3A%22Automated+Tests%22
   :alt: Automated Tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. .. image:: https://readthedocs.org/projects/skeleton/badge/?version=latest
..    :target: https://skeleton.readthedocs.io/en/latest/?badge=latest

CORS support for CherryPy

In a nutshell
=============

In your application, either install the tool globally.

.. code-block:: python

    import cherrypy_cors
    cherrypy_cors.install()

Or add it to your application explicitly.

.. code-block:: python

    import cherrypy_cors
    app = cherrypy.tree.mount(...)
    app.toolboxes['cors'] = cherrypy_cors.tools

Then, enable it in your cherrypy config. For example, to enable it for all
static resources.

.. code-block:: python

    config = {
        '/static': {
            'tools.staticdir.on': True,
            'cors.expose.on': True,
        }
    }

See `simple-example
<https://github.com/yougov/cherrypy-cors/blob/master/simple-example.py>`_
for a runnable example.
