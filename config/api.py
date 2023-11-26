from ninja import NinjaAPI
from customers.api.api import customers_router

api = NinjaAPI()

api.add_router('/customers', customers_router)