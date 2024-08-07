from django.core.management.base import BaseCommand

from shop.models import Product, Promotion, Tariff


class Command(BaseCommand):
    help = 'Инициализация базы данных начальными значениями'

    def handle(self, *args, **options):
        if not Product.objects.count():
            # Создаем и сохраняем продукт
            product = Product(name='Product1')
            product.save()

            # Создаем и сохраняем тариф, связывая его с продуктом
            tariff = Tariff(name='Tariff1', base_price=100.00, product=product)
            tariff.save()

            # Создаем и сохраняем акцию
            promotion = Promotion(
                name='Discount1',
                discount_percentage=10,
                start_date='2024-06-01',
                end_date='2025-08-31'
            )
            promotion.save()

            # Связываем акцию с тарифом
            promotion.tariffs.add(tariff)

            self.stdout.write(self.style.SUCCESS(
                'Initialize db command executed successfully'))
