# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import asyncio

from functionsclient.v1 import client


if __name__ == "__main__":

    eventloop = asyncio.get_event_loop()

    api_client = client.FunctionsAPIV1("192.168.0.111", api_port=10501)

    async def create_app_route_and_execution():
        apps = await api_client.apps.list(loop=eventloop)
        print(apps)
        app = await api_client.apps.create("testapp", loop=eventloop)
        print(app.__dict__)

        route = await app.routes.create(**{
            "type": "sync",
            "path": "/hello-sync",
            "image": "iron/hello"
        }, loop=eventloop)
        print(route.__dict__)
        route = await app.routes.show("/hello-sync", loop=eventloop)
        print(route)

        result = await app.routes.execute("/hello-sync",
                                          loop=eventloop, **{"name": "Johnny"})
        print(result)

    eventloop.run_until_complete(create_app_route_and_execution())
