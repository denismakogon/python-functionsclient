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

from functionsclient.v1 import routes


class AppResource(object):

    def __init__(self, app_routes, **kwargs):
        self.routes = app_routes
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.__kwargs__ = kwargs


class FunctionsApps(object):

    apps_key = "apps"
    app_key = "app"

    def __init__(self, api_client):
        self.api_client = api_client

    async def list(
            self, loop: asyncio.AbstractEventLoop=None):
        """
        Lists available apps

        :param loop: event loop instance
        :type loop: asyncio.AbstractEventLoop
        :return: list of AppResource
        :rtype: list
        """
        apps = (await self.api_client.get("/apps", loop=loop))[self.apps_key]
        return [AppResource(
            routes.AppRoutes(attrs["name"], self.api_client),
            **attrs) for attrs in apps]

    async def create(self, name,
                     loop: asyncio.AbstractEventLoop=None):
        """
        Creates an app

        :param name: app name
        :type name: str
        :param loop: event loop instance
        :type loop: asyncio.AbstractEventLoop
        :return: app object
        :rtype: AppResource
        """
        app = (await self.api_client.post(
            "/apps", {"app": {"name": name}}, loop=loop))[self.app_key]
        return AppResource(routes.AppRoutes(name, self.api_client), **app)

    async def show(self, name,
                   loop: asyncio.AbstractEventLoop=None):
        """
        This gives more details about a app, such as statistics.

        :param name: app name
        :type name: str
        :param loop: event loop instance
        :type loop: asyncio.AbstractEventLoop
        :return: app
        :rtype: AppResource
        """
        app = (await self.api_client.get(
            "/apps/{0}".format(name), loop=loop))[self.app_key]
        return AppResource(routes.AppRoutes(name, self.api_client), **app)

    async def delete(self, name,
                     loop: asyncio.AbstractEventLoop=None):
        """
        Deletes app

        :param name: App name
        :param loop: event loop
        :return: None
        :rtype: None
        """
        await self.api_client.delete(
            "/apps/{0}".format(name), loop=loop
        )
        return None

    async def update(self, app,
                     loop: asyncio.AbstractEventLoop=None,
                     **parameters):
        """
        This gives more details about a app, such as statistics.

        :param app: app name
        :type app: str
        :param loop: event loop instance
        :type loop: asyncio.AbstractEventLoop
        :return: app
        :rtype: AppResource
        """
        await self.api_client.patch("/apps/{0}".format(app),
                                    {"app": parameters}, loop=loop)
        return await self.show(app, loop=loop)
