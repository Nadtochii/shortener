import unittest
from django.test import TestCase, Client

class SimpleTest(unittest.TestCase):
    def test_details(self):
        client = Client()
        response = client.get('/short/')
        self.assertEqual(response.status_code, 200)
