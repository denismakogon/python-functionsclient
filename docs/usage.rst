==========================
Using IronFunctions client
==========================

Working with apps
#################

In order to work with functions it is necessary to create their placeholders - apps.
Each app is defined by name and configuration mapping.

Required imports::

    import asyncio
    from functionsclient.v1 import client
    eventloop = asyncio.get_event_loop()

Using *functionsclient* app can be created using following command::

    api_client = client.FunctionsAPIV1("functions-host", api_port=10501)
    app = api_client.apps.create("testapp", loop=eventloop)

Once app created it is possible to describe app details using *show* API call::

    app = api_client.apps.show("testapp", loop=eventloop)

App is a manageable resource, so it can be created, updated or deleted::

    await api_client.apps.list(loop=eventloop)
    await api_client.apps.update("testapp", loop=eventloop,
                                 name="new_testapp", config={"param": "test"})
    await api_client.apps.delete("testapp", loop=eventloop)

Working with routes
###################

So the app is a placeholder for routes, where each route is a data type that consists of::

    Docker image reference
    HTTP route that will be assigned to container and will be available as webhook URL
    Timeout to fit in function execution
    Execution type (sync or async)
    Max concurrency to define how many concurrent requests should be expected before suspending a container

Available API for routes::

    create
    list
    show
    update
    delete

In order to create a route following API must be used::

    app = await api_client.apps.create("testapp", loop=eventloop)
    route = await app.routes.create(**{
        "type": "async",
        "path": "/hello-sync",
        "image": "iron/hello",
        "timeout": 100,
        "max_concurrency": 2,
    }, loop=eventloop)

Listing routes::

    app = await api_client.apps.create("testapp", loop=eventloop)
    routes = await app.routes.list(loop=eventloop)

Showing route details::

    app = await api_client.apps.create("testapp", loop=eventloop)
    route = await app.routes.show("/hello-sync", loop=eventloop)

Updating route::

    app = await api_client.apps.create("testapp", loop=eventloop)
    route = await app.routes.update("/hello-sync", loop=eventloop, **{
                                        "type": "sync"
                                    })

Deleting route::

    app = await api_client.apps.create("testapp", loop=eventloop)
    await app.route.delete("/hello-sync", loop=eventloop)


Running functions
#################

Once route created it is possible to run function pinned to this route::

    app = await api_client.apps.create("testapp", loop=eventloop)
    result = await app.routes.execute("/hello-sync", loop=eventloop, **{"name": "Johnny"})

As it can be seen, coroutine *execute* accepts various number of parameters (using key-value args) that are being sent directly to a function.
