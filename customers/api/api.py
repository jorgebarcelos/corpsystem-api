from ninja import Router
from typing import List, Optional
from customers.models import Customer
from customers.schemas.customers import CustomerSchema, CustomerSchemaID, NotFoundSchema

customers_router  = Router()

@customers_router.post('customers/', response={201: CustomerSchema})
def test(request, paylad: CustomerSchema):
    paylad = Customer.objects.create(**paylad.dict())
    return paylad


@customers_router.get("customers/", response=List[CustomerSchema])
def tracks(request, title: Optional[str] = None):
    if title:
        return Customer.objects.filter(title__icontains=title)
    return Customer.objects.all()


@customers_router.get("customers/{customer_id}", response={200: CustomerSchemaID, 404: NotFoundSchema})
def track(request, customer_id: int):
    try:
        customer = Customer.objects.get(pk=customer_id)
        return 200, customer
    except Customer.DoesNotExist as e:
        return 404, {"message": "Could not find customer"}
    

@customers_router.put("customers/{customer_id}", response={200: CustomerSchemaID, 404: NotFoundSchema})
def change_track(request, customer_id: int, data: CustomerSchemaID):
    try:
        customer = Customer.objects.get(pk=customer_id)
        for attribute, value in data.dict().items():
            setattr(customer, attribute, value)
        customer.save()
        return 200, customer
    except Customer.DoesNotExist as e:
        return 404, {"message": "Could not find customer"}
    

@customers_router.delete("customers/{customer_id}", response={200: None, 404: NotFoundSchema})
def delete_track(request, customer_id: int):
    try:
        customer = Customer.objects.get(pk=customer_id)
        customer.delete()
        return 200
    except Customer.DoesNotExist as e:
        return 404, {"message": "Could not find customer"}