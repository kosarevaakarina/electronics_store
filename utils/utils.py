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
        self.name = name
        self.price = price
        self.amount = amount
        self.all.append(self)

    def calculate_total_price(self):
        """ Возвращает общую стоимость конкретного товара в магазине """
        return self.price * self.amount

    def discount_price(self):
        """ Возваращает стоимость товара со скидкой """
        self.price *= self.discount
        return self.price




