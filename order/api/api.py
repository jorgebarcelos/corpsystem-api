from ninja import Router
from typing import List, Optional
from order.models import Order
from products.models import Products
from customers.models import Customer
from order.schemas.order import OrderSchema, OrderSchemaID, NotFoundSchema


order_router = Router()

@order_router.post('order/', response={201: OrderSchema})
def create_order(request, payload: OrderSchema):

    customer = Customer.objects.get(pk=payload.customer_id)
    order = Order(
        customer_id=customer,
        quantity=payload.quantity,
        price=payload.price
    )
    products = Products.objects.filter(pk__in=payload.product_id)
    order.save()

    for product in products:
        order.product_id.add(product)
    order.save()

    return order


@order_router.get('order/', response=List[OrderSchemaID])
def retrieve_orders(request, title: Optional[str] = None):
    if title:
        return Order.objects.filter(title__icontains=title)
    return Order.objects.all()


@order_router.get('order/{customer_id}', response=List[OrderSchemaID])
def retrieve_order_by_customer(request, customer_id: int):

    orders = Order.objects.filter(customer_id=customer_id)

    return orders