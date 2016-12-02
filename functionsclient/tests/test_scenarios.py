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

from functionsclient.tests import base


class TestAPI(base.TestFunctions):

    def test_apps(self):

        async def scenarios_one():
            apps = await self.v1.apps.list(loop=self.testloop)
            self.assertEqual(0, len(apps))

            created_app = await self.v1.apps.create(
                self.app_name, loop=self.testloop)
            self.assertEqual(self.app_name, created_app.name)

            apps = await self.v1.apps.list(loop=self.testloop)
            self.assertEqual(1, len(apps))

            show_app = await self.v1.apps.show(
                created_app.name, loop=self.testloop)
            self.assertEqual(created_app.name, show_app.name)

            updated_app = await self.v1.apps.update(
                created_app.name, loop=self.testloop,
                **{"name": self.new_app_name})
            self.assertEqual(show_app.name, updated_app.name)

            await self.v1.apps.delete(
                created_app.name, loop=self.testloop)
            apps = await self.v1.apps.list(loop=self.testloop)
            self.assertEqual(0, len(apps))

        self.testloop.run_until_complete(scenarios_one())

    def test_routes(self):
        async def scenarios_two():
            created_app = await self.v1.apps.create(
                self.app_name, loop=self.testloop)
            app_routes = await created_app.routes.list(
                loop=self.testloop)
            self.assertEqual(0, len(app_routes))

            create_route = await created_app.routes.create(
                **self.route_parameters, loop=self.testloop)

            self.assertEqual(self.route_parameters["type"],
                             create_route.type)

            app_routes = await created_app.routes.list(loop=self.testloop)
            self.assertEqual(1, len(app_routes))

            copy_of_route = await created_app.routes.show(
                create_route.path, loop=self.testloop)
            self.assertEqual(create_route.path, copy_of_route.path)
            self.assertEqual(create_route.type, copy_of_route.type)

            updated_route = await created_app.routes.update(
                create_route.path, loop=self.testloop, **{
                    "type": "sync"})
            self.assertNotIn(create_route.type, updated_route.type)

            result = await created_app.routes.execute(
                updated_route.path, loop=self.testloop,
                **self.execution_parameters)
            self.assertIsNotNone(result)

            await created_app.routes.delete(
                create_route.path, loop=self.testloop)
            app_routes = await created_app.routes.list(
                loop=self.testloop)
            self.assertEqual(0, len(app_routes))

            await self.v1.apps.delete(
                created_app.name, loop=self.testloop)

        self.testloop.run_until_complete(scenarios_two())

    def test_get_unknown_app(self):
        self.assertRaises(Exception,
                          self.testloop.run_until_complete,
                          self.v1.apps.show(
                              "uknown", loop=self.testloop))

    def test_get_unknown_route(self):
        async def scenarios():
            created_app = await self.v1.apps.create(
                self.app_name, loop=self.testloop)

            await created_app.routes.show(
                "/unknown", loop=self.testloop)

        self.assertRaises(Exception, self.testloop.run_until_complete,
                          scenarios())
        self.testloop.run_until_complete(self.v1.apps.delete(
            self.app_name, loop=self.testloop))

    def test_delete_app_with_routes(self):
        async def scenarios():
            created_app = await self.v1.apps.create(
                self.app_name, loop=self.testloop)

            await created_app.routes.create(
                **self.route_parameters, loop=self.testloop)

            await self.v1.apps.delete(created_app.name, loop=self.testloop)

        self.assertRaises(Exception, self.testloop.run_until_complete,
                          scenarios())

        _app = self.testloop.run_until_complete(self.v1.apps.show(
            self.app_name, loop=self.testloop))

        for route in self.testloop.run_until_complete(
                _app.routes.list(loop=self.testloop)):

            self.testloop.run_until_complete(_app.routes.delete(
                route.path, loop=self.testloop))

        self.testloop.run_until_complete(self.v1.apps.delete(
            self.app_name, loop=self.testloop))
