from domain.sneakers_product import SneakersProduct
from decimal import Decimal

class CustomizableSneakersProduct(SneakersProduct):
    def __init__(self):
        super().__init__()
        self._size = ''
        self._color = ''
        self.__print_price = Decimal(0.0)
        self.__shoe_laces_price = Decimal(0.0)

        self.__type_prints_dict = {
            "Print1": 100.0,
            "Print2": 200.0,
            "Print3": 300.0,
        }

        self.__shoe_laces_dict = {
            "ShoeLace1": 10.0,
            "ShoeLace2": 20.0,
            "ShoeLace3": 30.0,
        }

    def console_input(self):
        super().console_input()
        self.type_print = input(f'Выберите принт ({self.__type_prints_dict}):')
        self.shoe_laces = input(f'Выберите шнурки ({self.__shoe_laces_dict}):')

    def parse_input(self, row):
        super().parse_input(row)
        self.type_print = row[7]
        self.shoe_laces = row[8]

    def console_output(self):
        print('Тип - Артикул - Название - Количество - Производитель - Цена - Размер - Цвет - Принт - Шнурки')
        print(f'{self.__class__.__name__} - {self._sku} - {self._name} - {self._qty} - {self._manufacter} - {self._price} - {self._size} - {self._color} - {self._type_print} - {self._shoe_laces}')


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
            'type_print': self.type_print,
            'shoe_laces': self.shoe_laces,            
        }                  

    @property
    def price(self):
        return super().price + self.__print_price + self.__shoe_laces_price

    @price.setter
    def price(self, value):
        self._price = float(value)

    #region Property TypePrint
    @property
    def type_print(self):
        return self._type_print

    @type_print.setter
    def type_print(self, value):
        if not value in self.__type_prints_dict.keys():
            raise TypeError('type_prints must be an instance of TypePrints dictionary')
        self._type_print = value
        self.__shoe_laces_price = self.__type_prints_dict[value]
    #endregion

    #region Property ShoeLaces
    @property
    def shoe_laces(self):
        return self._shoe_laces

    @shoe_laces.setter
    def shoe_laces(self, value):
        if not value in self.__shoe_laces_dict.keys():
            raise TypeError('shoe_laces must be an instance of ShoeLaces dictionary')
        self._shoe_laces = value
        self.__print_price = self.__shoe_laces_dict[value]
    #endregion
