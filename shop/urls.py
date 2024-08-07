from django.contrib import admin
from django.urls import path

from shop.views import product_tariff_promotion_view

urlpatterns = [
    path('products/', product_tariff_promotion_view),
]
