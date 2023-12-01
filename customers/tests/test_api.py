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
        response = self.client.post(self.url, data=payload, content_type="application/json")
        json_response = response.json()
        self.assertEqual(json_response['name'], payload['name'])
        

    def test_retrieve_customers(self):

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    
    def test_retrieve_customer(self):

        user_id = {"id": 3}
        response = self.client.get(self.url, data=user_id)
        self.assertEqual(response.status_code, 200)

    
    def test_edit_customer(self):

        payload = {"id": 1, "name": "Jorge Barcelos Faria Jr"}
        response = self.client.put(self.url, data=payload)
        self.assertEqual(response.status_code, 200)

    
    def test_delete_customer(self):

        user_id = {"id": 4,}
        response = self.client.delete(self.url, user_id)
        self.assertEqual(response.status_code, 200)