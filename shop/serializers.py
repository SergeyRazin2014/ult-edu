from rest_framework import serializers
from .models import Product, Tariff, Promotion
from django.utils import timezone
import decimal


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['name', 'discount_percentage', 'end_date']


class TariffSerializer(serializers.ModelSerializer):
    promotion = serializers.SerializerMethodField()

    class Meta:
        model = Tariff
        fields = ['name', 'base_price', 'promotion']

    def get_promotion(self, obj):
        # Получаем активные акции для тарифа
        active_promotions = obj.promotions.filter(
            start_date__lte=timezone.now().date(),
            end_date__gte=timezone.now().date()
        ).order_by('-discount_percentage')

        if active_promotions.exists():
            # Выбираем акцию с наибольшим процентом скидки
            promotion = active_promotions.first()

            discount_price = obj.base_price * \
                (1 - (decimal.Decimal(promotion.discount_percentage) / 100))

            return {
                'name': promotion.name,
                'discount_percentage': promotion.discount_percentage,
                'end_date': promotion.end_date,
                'discount_price': discount_price.quantize(decimal.Decimal('0.00'))
            }
        return {}


class ProductSerializer(serializers.ModelSerializer):
    tariffs = TariffSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'tariffs']
