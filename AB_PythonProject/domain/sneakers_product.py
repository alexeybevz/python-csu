from decimal import Decimal
from domain.product import Product

class SneakersProduct(Product):

    def __init__(self):
        super().__init__()
        self._size = 0
        self._color = ''

    def console_input(self):
        super().console_input()
        self.size = input("Введение размер:")
        self.color = input("Введение цвет:")

    def parse_input(self, row):
        super().parse_input(row)
        self.size = row[5]
        self.color = row[6]

    def console_output(self):
        print('Тип - Артикул - Название - Количество - Производитель - Цена - Размер - Цвет')
        print(f'{self.__class__.__name__} - {self._sku} - {self._name} - {self._qty} - {self._manufacter} - {self._price} - {self._size} - {self._color}')

    def serialize(self):
        return {
            'type_product': self.__class__.__name__,
            'sku': self.sku, 
            'name': self.name,
            'qty': str(self.qty),
            'manufacter': self.manufacter,
            'price': str(self.price),
            'size': str(self.size),
            'color': self.color,
        }              

    #region Property Size
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if (Decimal(value) < 0):
            raise ValueError('Размер не может быть отрицательным')
        self._size = value
    #endregion

    #region Property Color
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
    #endregion