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
        apps = self.testloop.run_until_complete(
            self.v1.apps.list(loop=self.testloop))
        self.assertEqual(0, len(apps))

        app = self.testloop.run_until_complete(
            self.v1.apps.create(self.app_name, loop=self.testloop))
        self.assertEqual(self.app_name, app.name)

        app_name = self.testloop.run_until_complete(
            self.v1.apps.list(loop=self.testloop))[0].name
        app = self.testloop.run_until_complete(
            self.v1.apps.show(app_name, loop=self.testloop))
        self.assertEqual(app_name, app.name)

        app_name = self.testloop.run_until_complete(
            self.v1.apps.list(loop=self.testloop))[0].name
        new_app = self.testloop.run_until_complete(
            self.v1.apps.update(app_name,
                                loop=self.testloop,
                                **{"name": self.new_app_name}))
        self.assertNotEqual(app_name, new_app)
        self.assertEqual(new_app.name, self.new_app_name)

    def test_routes(self):
        app = self.testloop.run_until_complete(
            self.v1.apps.create(self.app_name, loop=self.testloop))
        self.assertEqual(self.app_name, app.name)

        routes = self.testloop.run_until_complete(
            app.routes.list(loop=self.testloop))
        self.assertEqual(0, len(routes))

        route = self.testloop.run_until_complete(
            app.routes.create(
                **self.route_parameters, loop=self.testloop))
        self.assertEqual(app.name, route.appname)

        routes = self.testloop.run_until_complete(
            app.routes.list(loop=self.testloop))
        self.assertEqual(1, len(routes))

        route = self.testloop.run_until_complete(
            app.routes.list(loop=self.testloop))[0]
        copy_of_route = self.testloop.run_until_complete(
            app.routes.show(route.path, loop=self.testloop))
        self.assertEqual(route.path, copy_of_route.path)
        self.assertEqual(route.type, copy_of_route.type)

        route = self.testloop.run_until_complete(
            app.routes.list(loop=self.testloop))[0]

        result = self.testloop.run_until_complete(
            app.routes.execute(route.path, loop=self.testloop,
                               **self.execution_parameters))
        self.assertIsNotNone(result)

        route = self.testloop.run_until_complete(
            app.routes.list(loop=self.testloop))[0]
        self.testloop.run_until_complete(
            app.routes.delete(route.path, loop=self.testloop))
