from ninja import Router
from typing import List, Optional
from sellers.models import Sellers
from sellers.schemas.sellers import SellersSchema, SellersSchemaID, NotFoundSchema


sellers_router = Router()

@sellers_router.post("sellers/", response={201: SellersSchema})
def create_seller(request, payload: SellersSchema):
    payload  = Sellers.objects.create(**payload.dict())
    return payload

@sellers_router.get("sellers/", response=List[SellersSchemaID])
def retrieve_sellers(request, title: Optional[str] = None):
    if title:
        return Sellers.objects.filter(title__icontains=title)
    return Sellers.objects.all()


@sellers_router.get("sellers/{seller_id}", response={200: SellersSchemaID, 404: NotFoundSchema})
def retrieve_seller(request, seller_id: int):
    try:
        seller = Sellers.objects.get(pk=seller_id)
        return 200, seller
    except Sellers.DoesNotExist as e:
        return 404, {"message": "Could not find seller"}
    

@sellers_router.put("sellers/{seller_id}", response={200: SellersSchemaID, 404: NotFoundSchema})
def change_seller(request, seller_id: int, data: SellersSchemaID):
    try:
        seller = Sellers.objects.get(pk=seller_id)
        for attribute, value in data.dict().items():
            setattr(seller, attribute, value)
        seller.save()
        return 200, seller
    except Sellers.DoesNotExist as e:
        return 404, {"message": "Could not find seller"}
    

@sellers_router.delete("sellers/{seller_id}", response={200: None, 404: NotFoundSchema})
def delete_seller(request, seller_id: int):
    try:
        seller = Sellers.objects.get(pk=seller_id)
        seller.delete()
        return 200
    except Sellers.DoesNotExist as e:
        return 404, {"message": "Could not find seller"}