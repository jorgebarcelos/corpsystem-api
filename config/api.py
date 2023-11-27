from ninja import NinjaAPI
from customers.api.api import customers_router
from products.api.api import products_router

api = NinjaAPI()

api.add_router('/customers', customers_router)
api.add_router('/products', products_router)