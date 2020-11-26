from domain.sneakers_product import SneakersProduct

class CustomizableSneakersProduct(SneakersProduct):
    def __init__(self):
        self.__print_price = 0.0
        self.__shoe_laces_price = 0.0

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
