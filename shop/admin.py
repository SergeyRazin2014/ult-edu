from django.contrib import admin

from shop.models import Product, Tariff, Promotion

admin.site.register(Product)
admin.site.register(Tariff)
admin.site.register(Promotion)