from django.contrib import admin
from order.models import Order
from products.models import Products

# Register your models here.
admin.site.register(Order)
# class ItenProductInLine(admin.TabularInline):
#     readonly_fields = ('name',)
#     model = Products

# @admin.register(Order)
# class AdminOrder(admin.ModelAdmin):
#     inlines = [ItenProductInLine]
