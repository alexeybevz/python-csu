class Product:

    def console_input(self):
        self._sku = input("Введите артикул:")
        self._name = input("Введите название:")
        self._qty = int(input("Введите количество:"))
        self._manufacter = input("Введите производителя:")
        self._price = float(input("Введите цену:"))

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
        self._qty = value
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
        self._price = value
    #endregion