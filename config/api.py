from ninja import NinjaAPI
from customers.api.api import customers_router
from products.api.api import products_router
from sellers.api.api import sellers_router
from order.api.api import order_router

api = NinjaAPI()

api.add_router('/customers', customers_router)
api.add_router('/products', products_router)
api.add_router('/sellers', sellers_router)
api.add_router('/order', order_router)