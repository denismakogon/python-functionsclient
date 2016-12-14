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

import aiohttp
import asyncio
import json


class FunctionsAPIException(Exception):

    def __init__(self, reason, status_code):
        self.reason = reason
        self.status = status_code
        super(FunctionsAPIException, self).__init__(reason)

    def __str__(self):
        return ("Error: HTTP code: {0}. Reason: {1}."
                .format(self.status, self.reason))


class FunctionsClient(object):

    def __init__(self, api_host: str,
                 api_port: int=8080,
                 api_version: str="v1",
                 api_protocol: str="http"):
        """
        Initializes connection with Functions service

        :param api_host: Functions API host
        :param api_port: Functions API port
        :param api_version: Functions API version
        :param api_protocol: Functions API protocol (http/https)
        """
        self.api_url = "{0}://{1}:{2}/{3}".format(
            api_protocol, api_host, api_port, api_version)
        self.route_execution_url = "{0}://{1}:{2}".format(
            api_protocol, api_host, api_port)

    async def raise_from_response(self, response):
        """
        Raises exception from response code including additional processing

        :param response: AIOHTTP response object
        :return:
        """
        try:
            response.raise_for_status()
        except Exception:
            try:
                response_object = await response.json()
                error_reason = response_object.get(
                    'error', {
                        "message": await response.text()
                    }).get("message", await response.text())
            except Exception:
                error_reason = await response.text()

            raise FunctionsAPIException(error_reason, response.status)

    async def get(self, url: str, body: dict=None,
                  loop: asyncio.AbstractEventLoop=None,
                  headers: dict=None,
                  timeout: int=300, params: dict=None) -> dict:
        """
        Runs HTTP GET

        :param url: accessible API URL
        :type url: str
        :param body:
        :type body: dict
        :param loop: Event loop instance
        :type loop: asyncio.AbstractEventLoop
        :param headers: HTTP headers
        :type headers: dict
        :param timeout: HTTP timeout
        :type timeout: int
        :param params: HTTP query parameters
        :type params: dict
        :return: response object
        """
        with aiohttp.ClientSession(loop=loop) as session:
            response = await session.get(
                "{0}{1}".format(self.api_url, url),
                data=body, headers=headers,
                timeout=timeout, params=params)
            await self.raise_from_response(response)
            return await response.json()

    async def post(self, url: str, body: dict,
                   loop: asyncio.AbstractEventLoop=None,
                   headers: dict=None, timeout=300) -> dict:
        """
        Runs HTTP POST

        :param url: accessible API URL
        :type url: str
        :param body:
        :type body: dict
        :param loop: Event loop instance
        :type loop: asyncio.AbstractEventLoop
        :param headers: HTTP headers
        :type headers: dict
        :param timeout: HTTP timeout
        :type timeout: int
        :return: response object
        """
        with aiohttp.ClientSession(loop=loop) as session:
            response = await session.post(
                "{0}{1}".format(self.api_url, url),
                data=json.dumps(body),
                headers=headers,
                timeout=timeout)
            await self.raise_from_response(response)
            return await response.json()

    async def execute(self, url: str, body: dict,
                      loop: asyncio.AbstractEventLoop=None,
                      headers: dict=None, timeout=300) -> dict:
        """
        Runs HTTP POST

        :param url: accessible API URL
        :type url: str
        :param body:
        :type body: dict
        :param loop: Event loop instance
        :type loop: asyncio.AbstractEventLoop
        :param headers: HTTP headers
        :type headers: dict
        :param timeout: HTTP timeout
        :type timeout: int
        :return: response object
        """
        with aiohttp.ClientSession(loop=loop) as session:
            response = await session.post(
                "{0}{1}".format(self.route_execution_url, url),
                data=json.dumps(body),
                headers=headers,
                timeout=timeout)
            await self.raise_from_response(response)
            return await response.text()

    async def put(self, url: str, body: dict,
                  loop: asyncio.AbstractEventLoop=None,
                  headers: dict=None, timeout: int=300) -> dict:
        """
        Runs HTTP PUT

        :param url: accessible API URL
        :type url: str
        :param body:
        :type body: dict
        :param loop: Event loop instance
        :type loop: asyncio.AbstractEventLoop
        :param headers: HTTP headers
        :type headers: dict
        :param timeout: HTTP timeout
        :type timeout: int
        :return: response object
        """
        with aiohttp.ClientSession(loop=loop) as session:
            response = await session.put(
                "{0}{1}".format(self.api_url, url),
                data=json.dumps(body),
                headers=headers,
                timeout=timeout)
            await self.raise_from_response(response)
            return await response.json()

    async def delete(self, url: str, body: dict=None,
                     loop: asyncio.AbstractEventLoop=None,
                     headers: dict=None, timeout: int=300) -> type(None):
        """
        Runs HTTP DELETE

        :param url: accessible API URL
        :type url: str
        :param body:
        :type body: dict
        :param loop: Event loop instance
        :type loop: asyncio.AbstractEventLoop
        :param headers: HTTP headers
        :type headers: dict
        :param timeout: HTTP timeout
        :type timeout: int
        :return: response object
        """
        with aiohttp.ClientSession(loop=loop) as session:
            response = await session.delete(
                "{0}{1}".format(self.api_url, url),
                data=body,
                headers=headers,
                timeout=timeout)

            await self.raise_from_response(response)
            response.close()

    async def patch(self, url: str, body: dict,
                    loop: asyncio.AbstractEventLoop=None,
                    headers: dict=None, timeout: int=300) -> dict:
        """
        Runs HTTP PATCH

        :param url: accessible API URL
        :type url: str
        :param body:
        :type body: dict
        :param loop: Event loop instance
        :type loop: asyncio.AbstractEventLoop
        :param headers: HTTP headers
        :type headers: dict
        :param timeout: HTTP timeout
        :type timeout: int
        :return: response object
        """
        with aiohttp.ClientSession(loop=loop) as session:
            response = await session.patch(
                "{0}{1}".format(self.api_url, url),
                data=json.dumps(body),
                headers=headers,
                timeout=timeout)
            await self.raise_from_response(response)
            return await response.json()
