# Functions API aiohttp-based Python client

## What is IronFunctions?
[IronFunctions](https://github.com/iron-io/functions) is an open source serverless platform, or as we like to refer to it,
Functions as a Service (FaaS) platform that you can run anywhere.

## IronFunctions Python API Usage Examples
* [Apps](examples/apps_api.py)
* [Routes](examples/routes_api.py)


## Testing
In order to run tests, set the corresponding environment variables:

        PYTHONASYNCIODEBUG=1
        FUNCTIONS_API_PROTO=http
        FUNCTIONS_API_HOST=<api-host>
        FUNCTIONS_API_PORT=<api-port>
        FUNCTIONS_API_VERSION=v1

### Style checks
    tox -epep8
    
### Integration tests
    tox -epy35
