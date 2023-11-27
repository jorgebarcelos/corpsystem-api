from ninja import ModelSchema, Schema
from products.models import Products


class ProductsSchema(ModelSchema):
    '''No ID Model'''
    class Config:
        model = Products
        model_fields = ['name', 'description', 'price']


class ProductSchemaID(ModelSchema):
    '''ID Model'''
    class Config:
        model = Products
        model_fields = '__all__'


class NotFoundSchema(Schema):
    message: str