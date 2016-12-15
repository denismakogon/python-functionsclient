[![TravisCI](https://travis-ci.org/denismakogon/python-functionsclient.svg?branch=master)](https://travis-ci.org/denismakogon/python-functionsclient)
[![Codecov](https://codecov.io/gh/denismakogon/python-functionsclient/branch/master/graph/badge.svg)](https://codecov.io/gh/denismakogon/python-functionsclient)
[![Docs](https://readthedocs.org/projects/python-functionsclient/badge/?version=latest)](http://aioservice.readthedocs.io/en/latest/?badge=latest)

## Functions API aiohttp-based Python client

## What is IronFunctions?

[IronFunctions](https://github.com/iron-io/function) is an open source serverless platform, or as we like to refer to it,
Functions as a Service (FaaS) platform that you can run anywhere.

## IronFunctions Python API Usage Examples

* [Apps](https://github.com/denismakogon/python-functionsclient/tree/master/examples/apps_api.p) - An application is essentially a grouping of functions, that put together, form an API.
* [Routes](https://github.com/denismakogon/python-functionsclient/tree/master/examples/routes_api.py) - A route is a way to define a path in your application that maps to a function.

## Testing

In order to run tests, set the corresponding environment variables::

    PYTHONASYNCIODEBUG=1
    FUNCTIONS_API_URL = http://<functions-host>:<functions-port>/v1


### Style checks

    tox -e pep8

### Integration tests

    tox -e py35

### Docs tests

    tox -e docs
