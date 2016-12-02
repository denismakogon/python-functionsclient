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

from functionsclient import client

from functionsclient.v1 import apps


class FunctionsAPIV1(client.FunctionsClient):

    def __init__(self, api_host: str,
                 api_port: int=8080,
                 api_protocol: str="http"):
        """
        Creates V1 IronFunctions client

        :param api_host: IronFunctions host
        :param api_port: IronFunctions port
        :param api_protocol: IronFunctions API protocol
        """
        super(FunctionsAPIV1, self).__init__(
            api_host,
            api_port=api_port,
            api_version="v1",
            api_protocol=api_protocol,
        )
        self.apps = apps.FunctionsApps(self)
