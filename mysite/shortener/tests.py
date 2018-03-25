import unittest
from django.test import TestCase, Client
from .models import Shortener

class SimpleTest(unittest.TestCase):
    def test_details(self):
        client = Client()
        response = client.get('/short/')
        self.assertEqual(response.status_code, 200)

    def test_action(self):
        client = Client()
        links_count = Shortener.objects.count()
        response = client.post('/short/', {'long_link':'https://translate.google.com.ua/?hl=uk#en/ru/'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Shortener.objects.count(), links_count + 1)