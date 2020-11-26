from domain.product import Product

class TShirtProduct(Product):

    def console_input(self):
        super().console_input()
        self._color = input("Введение цвет:")
        self._size = input("Введение размер:")

    #region Property Size
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
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