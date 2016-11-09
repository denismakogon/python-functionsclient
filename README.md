Functions API aiohttp-based Python client
=========================================

Apps Python API usage
---------------------

See sample in [examples](examples/apps_api.py)


Apps Python API usage
---------------------

See sample in [examples](examples/routes_api.py)


Testing
-------

In order to run tests please set corresponding env variables::

        PYTHONASYNCIODEBUG=1
        FUNCTIONS_API_PROTO=http
        FUNCTIONS_API_HOST=<where-api-deployed>
        FUNCTIONS_API_PORT=<api-port>
        FUNCTIONS_API_VERSION=v1

Style checks:

    tox -epep8
    
Integration scenarios tests:

    tox -epy35
