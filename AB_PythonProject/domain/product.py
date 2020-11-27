from decimal import Decimal

class Product:

    def console_input(self):
        self._sku = input("Введите артикул:")
        self._name = input("Введите название:")
        self._qty = input("Введите количество:")
        self._manufacter = input("Введите производителя:")
        self._price = input("Введите цену:")

    def parse_input(self, row):
        self._sku = row[0]
        self._name = row[1]
        self._qty = row[2]
        self._manufacter = row[3]
        self._price = row[4]

    def console_output(self):
        print('Тип - Артикул - Название - Количество - Производитель - Цена')
        print(f'{self.__class__.__name__} - {self._sku} - {self._name} - {self._qty} - {self._manufacter} - {self._price}')

    #region Property Sku
    @property
    def sku(self):
        return self._sku

    @sku.setter
    def sku(self, value):
        self._sku = value
    #endregion

    #region Property Name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    #endregion

    #region Property Qty
    @property
    def qty(self):
        return self._qty

    @qty.setter
    def qty(self, value):
        if (int(value) < 0):
            raise ValueError('Количество не может быть отрицательным')
        self._qty = int(value)
    #endregion

    #region Property Manufacter
    @property
    def manufacter(self):
        return self._manufacter

    @manufacter.setter
    def manufacter(self, value):
        self._manufacter = value
    #endregion

    #region Property Price
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if (Decimal(value) < 0):
            raise ValueError('Цена не может быть отрицательной')
        self._price = Decimal(value)
    #endregion