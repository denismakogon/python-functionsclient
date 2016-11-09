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


class TestFunctions(testtools.TestCase):

    def setUp(self):
        self.testloop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)

        self.api_host, self.api_port, self.api_proto, self.api_version = (
            os.getenv("FUNCTIONS_API_HOST"),
            os.getenv("FUNCTIONS_API_PORT", 8080),
            os.getenv("FUNCTIONS_API_PROTO", "http"),
            os.getenv("FUNCTIONS_API_VERSION", "v1"),
        )

        if not self.api_host:
            raise self.skipTest("Unable to locate Function "
                                "API host env variable.")

        self.v1 = client.FunctionsAPIV1(
            self.api_host,
            api_port=self.api_port,
            api_protocol=self.api_proto)

        # API limits app name to 30 symbols
        self.app_name = ("testapp-{}".format(str(uuid.uuid4())))[:30]
        self.new_app_name = ("testapp-{}".format(str(uuid.uuid4())))[:30]

        self.route_parameters = {
            "type": "sync",
            "path": "/hello-sync",
            "image": "iron/hello"
        }

        self.execution_parameters = {"name": "Johnny"}

        super(TestFunctions, self).setUp()

    def tearDown(self):
        super(TestFunctions, self).tearDown()
