# Магазин электроники - разработка классов для представления товаров магазина для проекта по созданию системы управления магазином электроники.
---
## Описание
---
* Созданы классы ElectronicStore, Phone и KeyBoard, а также класс-миксин MixinLog.
---
* class ElectronicStore - представление товара магазина электроники:
  * Заданы следующие атрибуты:
    * Название товара
    * Цена за единицу товара 
    * Количество товара в магазине
  * Реализованы методы:
    * Возвращает общую стоимость конкретного товара в магазине (calculate_total_price())
    * Возваращает стоимость товара со скидкой (discount_price())
  * Валидация:
    * При задании названия товара длина не должна превышать 10 символов
    * Реализован статический метод, который проверяет, является ли число целым
  * Права доступа:
    * Название товара является приватным атрибутом
  * Реализованы магические методы __str__, __repr__, __add__
  * Для создания экземпляров класса создан метод для считывания данных из csv-файла (instantiate_from_csv())
---
* class Phone - представление товара "телефон":
  * Наследуется от класса ElectronicStore (доступны все атрибуты и методы этого класса) 
  * Задан атрибут для хранения количества сим-карт
  * Права доступа:
    * Количество SIM является приватным атрибутом
  * Валидация:
    * Количество физических SIM-карт должно быть целым числом больше нуля
  * Реализован магический метод __repr__
---
* class MixinLog - класс-миксин с дополнительным функционалом по хранению и изменению раскладки клавиатуры
* class KeyBoard - класс для товара "клавиатура":
  * Наследуется от классов MixinLog и ElectronicStore (доступны все атрибуты и методы этих классов)  
---
## Сущности
* Товары
* Телефоны
* Клавиатуры
## Настройка проека
_Активация виртуального окружения:_
```
poetry init
```
_Запуск тестов:_
```
poetry run test
```
_Запуск тестов с оценкой покрытия:_:
```
poetry run pytest --cov
```