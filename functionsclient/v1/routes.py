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

import json


class AppRouteResource(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class AppRoutes(object):

    routes_key = "routes"
    route_key = "route"

    def __init__(self, app_name, api_client):
        self.api_client = api_client
        self.app_name = app_name

    async def list(self,
                   loop: asyncio.AbstractEventLoop=asyncio.get_event_loop()):
        """
        Lists available routes for app
        :param loop: event loop instance
        :type loop: asyncio.AbstractEventLoop
        :return: list of AppRoutes
        :rtype: list of AppRouteResource
        """
        routes = (await self.api_client.get(
            "/apps/{0}/routes".format(self.app_name),
            loop=loop))[self.routes_key]
        return [AppRouteResource(**attrs) for attrs in routes]

    async def create(self,
                     loop: asyncio.AbstractEventLoop=asyncio.get_event_loop(),
                     **parameters):
        """
        Creates app route
        :param parameters: app route parameters
        :param loop: event loop instance
        :type loop: asyncio.AbstractEventLoop
        :return: app route
        :rtype: AppRouteResource
        """
        parameters.update({"app_name": self.app_name})
        route = (await (self.api_client.post(
            "/apps/{0}/routes".format(self.app_name),
            {"route": parameters}, loop=loop)))[self.route_key]
        return AppRouteResource(**route)

    async def delete(self, route,
                     loop: asyncio.AbstractEventLoop=asyncio.get_event_loop()):
        """
        Deletes an app route
        :param route: route path
        :param loop: event loop instance
        :type loop: asyncio.AbstractEventLoop
        :return: None
        :rtype: None
        """
        await self.api_client.delete(
            "/apps/{0}/routes{1}".format(
                self.app_name, route), loop=loop)

    async def show(self, route_path,
                   loop: asyncio.AbstractEventLoop=asyncio.get_event_loop()):
        """
        Describes route for app
        :param route_path: route path
        :param loop: event loop instance
        :type loop: asyncio.AbstractEventLoop
        :return: app route
        :rtype: AppRouteResource
        """
        route = (await self.api_client.get(
            "/apps/{0}/routes{1}".format(
                self.app_name, route_path), loop=loop))[self.route_key]
        return AppRouteResource(**route)

    async def execute(self, route,
                      loop: asyncio.AbstractEventLoop=asyncio.get_event_loop(),
                      **parameters):
        """
        Runs execution against app route
        :param route: route path
        :param parameters: route execution parameters
        :param loop: event loop instance
        :type loop: asyncio.AbstractEventLoop
        :return: execution result
        :rtype: str
        """
        route = await self.show(route, loop=loop)
        result = (await self.api_client.execute(
            "/r/{0}{1}".format(route.appname, route.path, loop=loop),
            parameters, loop=loop))
        return result if route.type == "sync" else json.loads(result)
