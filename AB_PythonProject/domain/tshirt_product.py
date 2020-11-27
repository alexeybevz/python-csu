from domain.product import Product

class TShirtProduct(Product):

    def console_input(self):
        super().console_input()
        self._size = input("Введение размер:")
        self._color = input("Введение цвет:")

    def parse_input(self, row):
        super().parse_input(row)
        self._size = row[5]
        self._color = row[6]

    def console_output(self):
        print('Тип - Артикул - Название - Количество - Производитель - Цена - Размер - Цвет')
        print(f'{self.__class__.__name__} - {self._sku} - {self._name} - {self._qty} - {self._manufacter} - {self._price} - {self._size} - {self._color}')

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