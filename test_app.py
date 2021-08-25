import requests
import unittest


class test_hello_world(unittest.TestCase):
    def test_hello_world(self):
        result = requests.get('http://localhost:5000/hello_world', verify=False).text
        test = result.find("Hello World!") != -1
        self.assertTrue(test)


