from flask import Flask
from flask_testing import TestCase

class MyTest(TestCase):

    def create_app(self):

        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_text(self):
        response = self.client.get('/')

        print("response", response)
        print(response.data)
        #assert "" == response.data
        self.assertEqual(response, "Hello World!")
        #assert 'Hello World!' not in response