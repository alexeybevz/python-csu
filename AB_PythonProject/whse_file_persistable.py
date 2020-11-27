from product_creator import ProductCreator

product_creator = ProductCreator()

class WhseFilePersistable:
    def __init__(self, path):
        self.path = path

    def get_data(self):
        products = []

        with open(self.path, 'r') as f:
            next(f)
            for line in f:
                line = line[:-1]
                props = line.split(';')

                product = product_creator.create(props[0])
                del props[0]
                product.parse_input(props)
                products.append(product)

        return products

    def save_data(self, products):
        f = open(self.path, 'w')
        f.write('Тип;Артикул;Название;Количество;Производитель;Цена;Размер;Цвет;Принт;Шнурки\n')

        columns = [ 'sku', 'name', 'qty', 'manufacter', 'price', 'size', 'color', 'type_print', 'shoe_laces' ]
        for product in products:
            f.write(f'{product.__class__.__name__};')

            for c in columns:
                f.write(f'{self.__write_columns(product, c)}')

            f.write('\n')

        f.close()

    def __write_columns(self, product, property_name):
        if hasattr(product, property_name):
            return f'{getattr(product, property_name)};'
        else:
            return ';'
