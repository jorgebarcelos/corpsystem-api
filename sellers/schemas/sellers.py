from ninja import ModelSchema, Schema
from sellers.models import Sellers


class SellersSchema(ModelSchema):
    '''No ID Model'''
    class Config:
        model = Sellers
        model_fields = ['seller_id', 'name']


class SellersSchemaID(ModelSchema):
    '''ID Model'''
    class Config:
        model = Sellers
        model_fields = '__all__'


class NotFoundSchema(Schema):
    message: str