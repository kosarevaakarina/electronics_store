import csv

from electronic_store.exceptions import InstantiateCSVError


class ElectronicStore:
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
    def name(self) -> str:
        """Возвращает значения приватного атрибута"""
        return self.__name

    @name.setter
    def name(self, name):
        """Проверяет, что при задании названия товара длина его не превышает 10 символов"""
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception("Длина наименования товара превышает 10 символов.")

    def calculate_total_price(self) -> float:
        """ Возвращает общую стоимость конкретного товара в магазине """
        return self.price * self.amount

    def discount_price(self) -> float:
        """ Возваращает стоимость товара со скидкой """
        self.price *= self.discount
        return self.price

    @classmethod
    def instantiate_from_csv(cls, file_csv) -> list | str:
        """Считывает данные из csv-файла и создает экземпляры класса"""
        try:
            with open(file_csv) as file:
                reader = list(csv.reader(file))
                item = []
                if reader[0] == ['name', 'price', 'quantity']:
                    for i in range(1, len(reader)):
                        item.append(ElectronicStore(reader[i][0], reader[i][1], reader[i][2]))
                else:
                    raise InstantiateCSVError
            return item
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {file_csv} не найден")
        except InstantiateCSVError:
            raise InstantiateCSVError(f"Файл {file_csv} поврежден")

    @staticmethod
    def is_integer(num) -> bool:
        """Проверяет, является ли чисто целым"""
        return int(num) == num

    def __repr__(self) -> str:
        """Возвращает формальное представление объекта"""
        return f'{self.__class__.__name__}({self.__name}, {self.price}, {self.amount})'

    def __str__(self) -> str:
        """Возвращает удобочитаемое строковое представление объекта (название товара)"""
        return f'{self.__name}'

    def __add__(self, other) -> int:
        """Складывает экземпляры класса Phone и Item по количеству товара"""
        if isinstance(other, ElectronicStore):
            return self.amount + other.amount


class Phone(ElectronicStore):
    def __init__(self, name, price, amount, number_of_sim):
        """Инициализация класса"""
        super().__init__(name, price, amount)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self) -> int:
        """Возвращает количество SIM"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        """Проверяет, что при задании количества сим-карт, это значение было больше 0"""
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self) -> str:
        """Возвращает формальное представление объекта"""
        return f'{self.__class__.__name__}({self.name}, {self.price}, {self.amount}, {self.number_of_sim})'


class MixinLog:
    """Класс-миксин с дополнительным функционалом по хранению и изменению раскладки клавиатуры"""

    def __init__(self, *args, **kwargs):
        self.__language = 'EN'
        super().__init__(*args, **kwargs)

    @property
    def language(self) -> str:
        """Возвращает язык клавиатуры"""
        return self.__language

    def change_lang(self):
        """Изменяет язык клавиатуры"""
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class KeyBoard(MixinLog, ElectronicStore):
    """Класс для товара 'клавиатура' """


