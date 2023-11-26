from ninja import ModelSchema, Schema
from customers.models import Customer


class CustomerSchema(ModelSchema):
    '''No  ID Model'''
    class Config:
        model = Customer
        model_fields = ['name']

class CustomerSchemaID(ModelSchema):
    '''ID Model'''
    class Config:
        model = Customer
        model_fields = '__all__'


class NotFoundSchema(Schema):
    message: str