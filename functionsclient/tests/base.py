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
import os
import uuid

import testtools

from functionsclient.v1 import client

from urllib import parse


class TestFunctions(testtools.TestCase):

    def setUp(self):
        self.testloop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)

        api_url = (
            os.getenv("FUNCTIONS_API_URL", "http://localhost:8080/v1")
        )

        parts = parse.urlparse(api_url)
        self.v1 = client.FunctionsAPIV1(
            parts.hostname,
            api_port=parts.port,
            api_protocol=parts.scheme,
        )

        # API limits app name to 30 symbols
        self.app_name = ("testapp-{}".format(str(uuid.uuid4())))[:30]
        self.new_app_name = ("testapp-{}".format(str(uuid.uuid4())))[:30]

        self.route_parameters = {
            "type": "async",
            "path": "/hello-sync",
            "image": "iron/hello"
        }

        self.execution_parameters = {"name": "Johnny"}

        super(TestFunctions, self).setUp()

    def tearDown(self):
        super(TestFunctions, self).tearDown()
