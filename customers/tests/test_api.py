from django.test import TestCase
from customers.models import Customer
from django.test.client import Client
from django.urls import reverse

# Create your tests here.
class CustomerTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = 'http://127.0.0.1:8000/api/v1/customers/customers/'
        self.customer = Customer.objects.create(name="Odair")
        self.customer_put = Customer.objects.create(name="Fernando")

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
        payload = {"name": "Fernando José"}
        response = self.client.put(f'{self.url}{self.customer_put.id}', data=payload, content_type="application/json")
        self.assertEqual(response.status_code, 200)

    
    def test_delete_customer(self):

        response = self.client.delete(f'{self.url}{self.customer.id}')
        self.assertEqual(response.status_code, 200)