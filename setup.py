#!/usr/bin/env python

from setuptools import setup

with open('README.txt') as readme:
    long_description = readme.read()

setup_args = dict(
    name='cherrypy-cors',
    version='1.1',
    url='http://yougov.kilnhg.com/Code/Repositories/global/cherrypy-cors/',
    author='Yougov',
    long_description=long_description,
    author_email='gustavo.picon@yougov.com',
    license='Apache License 2.0',
    py_modules=['cherrypy_cors'],
    description='CORS handling as a cherrypy tool.',
)

if __name__ == '__main__':
    setup(**setup_args)
