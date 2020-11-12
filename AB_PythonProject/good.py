class Good:
    def __init__(self):
        self.id = None
        self.name = None
        self.qty = None
        self.manufacturer = None
        self.price = None
        self.size = None

    #region Property Id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
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

    #region Property Manufacturer
    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value
    #endregion

    #region Property Price
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    #endregion

    #region Property Size
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    #endregion