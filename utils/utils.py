import csv


class Electronic_store:
    discount = 0.85
    all = []

    def __init__(self, name, price, amount):
        """
        Инициализация класса
        :param name: название товара
        :param price: цена за единицу товара
        :param amount: количество товара
        """
        self.__name = name
        self.price = price
        self.amount = amount
        self.all.append(self)

    @property
    def name(self):
        """Возвращает значения приватного атрибута"""
        return self.__name

    @name.setter
    def name(self, name):
        """Проверяет, что при задании названия товара длина его не превышает 10 символов"""
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception("Длина наименования товара превышает 10 символов.")

    def calculate_total_price(self):
        """ Возвращает общую стоимость конкретного товара в магазине """
        return self.price * self.amount

    def discount_price(self):
        """ Возваращает стоимость товара со скидкой """
        self.price *= self.discount
        return self.price

    @classmethod
    def instantiate_from_csv(cls, file_csv):
        """Считывает данные из csv-файла и создает экземпляры класса"""
        with open(file_csv) as file:
            reader = list(csv.reader(file))
            item = []
            for i in range(1, len(reader)):
                item.append(Electronic_store(reader[i][0], reader[i][1], reader[i][2]))
        return item

    @staticmethod
    def is_integer(num):
        """Проверяет, является ли чисто целым"""
        return int(num) == num

