
.. image:: https://codecov.io/gh/denismakogon/python-functionsclient/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/denismakogon/python-functionsclient

.. image:: https://readthedocs.org/projects/python-functionsclient/badge/?version=latest
    :target: http://aioservice.readthedocs.io/en/latest/?badge=latest


#########################################
Functions API aiohttp-based Python client
#########################################

What is IronFunctions?
######################

IronFunctions_ is an open source serverless platform, or as we like to refer to it,
Functions as a Service (FaaS) platform that you can run anywhere.

IronFunctions Python API Usage Examples
#######################################

* Apps_
* Routes_

Testing
#######
In order to run tests, set the corresponding environment variables::

    PYTHONASYNCIODEBUG=1
    FUNCTIONS_API_URL = http://<functions-host>:<functions-port>/v1


Style checks
############
.. code-block:: Bash

    tox -e pep8
    
Integration tests
#################
.. code-block:: Bash

    tox -e py35

Docs tests
##########
.. code-block:: Bash

    tox -e docs

.. _IronFunctions: https://github.com/iron-io/functions
.. _Apps: https://github.com/denismakogon/python-functionsclient/tree/master/examples/apps_api.py
.. _Routes: https://github.com/denismakogon/python-functionsclient/tree/master/examples/routes_api.py
