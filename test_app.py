import requests
import unittest


class test_hello_world(unittest.TestCase):
    def test_hello_world(self):
        result = requests.get('http://127.0.0.1:5000/hello_world').text
        test = result.find("Hello World!") != -1
        self.assertTrue(test)


