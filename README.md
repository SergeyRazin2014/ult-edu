# Тестовое задание для Ultimate Education

## Описание задания
Создайте представление, которое выводит все продукты со всеми тарифами, с учетом акций. Вывод должен быть в формате XML, структура произвольная. Акция для тарифа должна выбираться по наибольшему проценту скидки. В представлении должна отображаться информация о дате окончания акции, базовая цена и цена со скидкой (если акция есть).

## Модели данных
- **Product** — имя
- **Tariff** – название, базовая цена, продукт (FK)
- **Promotion** – название, процент скидки, даты начала и окончания, тарифы (M2M)

## Технические требования
- Django REST Framework (DRF)
- PostgreSQL в качестве базы данных

## Запуск проекта
1. Находясь в папке с проектом - выполните команду в консоли:
   docker-compose up
2. Подождите, пока установятся зависимости и пройдут миграции базы данных.
   (В консоли должна отобразиться запись:
   Initialize db command executed successfully
   Watching for file changes with StatReloader )
3. В браузере перейдите по пути:   http://127.0.0.1:8000/api/v1/products/
4. После чего должны отобразиться данные в виде XML.
