.. image:: https://img.shields.io/pypi/v/cherrypy-cors.svg
   :target: https://pypi.org/project/cherrypy-cors

.. image:: https://img.shields.io/pypi/pyversions/cherrypy-cors.svg

.. image:: https://github.com/cherrypy/cherrypy-cors/actions/workflows/main.yml/badge.svg
   :target: https://github.com/cherrypy/cherrypy-cors/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

.. image:: https://readthedocs.org/projects/cherrypy-cors/badge/?version=latest
   :target: https://cherrypy-cors.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/skeleton-2025-informational
   :target: https://blog.jaraco.com/skeleton

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
