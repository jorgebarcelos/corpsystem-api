from ninja import Router
from typing import List, Optional
from products.models import Products
from products.schemas.products import ProductsSchema, ProductSchemaID, NotFoundSchema

products_router = Router()

@products_router.post("products/", response={201: ProductsSchema})
def create_product(request, payload: ProductsSchema):
    payload = Products.objects.create(**payload.dict())
    return payload


@products_router.get("products/", response=List[ProductSchemaID])
def retrieve_products(request, title: Optional[str] = None):
    if title:
        return Products.objects.filter(title__icontains=title)
    return Products.objects.all()


@products_router.get("products/{product_id}", response={200: ProductSchemaID, 404: NotFoundSchema})
def retrieve_customer(request, product_id: int):
    try:
        product = Products.objects.get(pk=product_id)
        return 200, product
    except Products.DoesNotExist as e:
        return 404, {"message": "Could not find product"}


@products_router.put("products/{product_id}", response={200: ProductSchemaID, 404: NotFoundSchema})
def change_product(request, product_id: int, data: ProductSchemaID):
    try:
        product = Products.objects.get(pk=product_id)
        for attribute, value in data.dict().items():
            setattr(product, attribute, value)
        product.save()
        return 200, product
    except Products.DoesNotExist as e:
        return 404, {"message": "Could not find product"}


@products_router.delete("products/{product_id}", response={200: None, 404: NotFoundSchema})
def delete_product(request, product_id: int):
    try:
        product = Products.objects.get(pk=product_id)
        product.delete()
        return 200
    except Products.DoesNotExist as e:
        return 400,  {"message": "Could not find product"}