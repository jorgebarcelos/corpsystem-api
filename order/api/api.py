from ninja import Router
from typing import List, Optional
from order.models import Order
from products.models import Products
from customers.models import Customer
from order.schemas.order import OrderSchema, OrderSchemaID, NotFoundSchema


order_router = Router()

@order_router.post('order/', response={201: OrderSchema})
def create_order(request, payload: OrderSchema):
    product = Products.objects.get(pk=payload.product_id)
    customer = Customer.objects.get(pk=payload.customer_id)

    order = Order(
        product_id=product,
        customer_id=customer,
        quantity=payload.quantity,
        price=payload.price
    )
    order.save()

    return OrderSchemaID(**order.__dict__)