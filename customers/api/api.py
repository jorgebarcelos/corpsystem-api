from ninja import Router
from django.http import JsonResponse

customers_router  = Router()

@customers_router.get('test/')
def test(request):
    return JsonResponse({"test": 1})