from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

# Create your tests here.
class CustomerTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = 'http://127.0.0.1:8000/api/v1/customers/customers/'
    
    def test_create_customer(self):
        
        payload = {"name": "Danilo"}
        reponse = self.client.post(self.url, data=payload, content_type="application/json")
        json_response = reponse.json()
        self.assertEqual(json_response['name'], payload['name'])
        

    def test_retrieve_customers(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)