from ninja import ModelSchema, Schema
from order.models import Order


class OrderSchema(ModelSchema):
    '''No  ID Model'''
    class Config:
        model = Order
        model_fields = ['product_id', 'customer_id', 'quantity', 'price']

class OrderSchemaID(ModelSchema):
    '''ID Model'''
    class Config:
        model = Order
        model_fields = '__all__'


class NotFoundSchema(Schema):
    message: str