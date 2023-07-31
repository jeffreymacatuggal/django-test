from django.test import TestCase
import requests

req_products = requests.get('http://127.0.0.1:8000/products/')

print(req_products.json())