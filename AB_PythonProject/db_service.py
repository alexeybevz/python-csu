import pyodbc
from domain.product import Product
from domain.tshirt_product import TShirtProduct
from domain.sneakers_product import SneakersProduct
from domain.customizable_sneakers_product import CustomizableSneakersProduct
from product_creator import ProductCreator

product_creator = ProductCreator()

class DbService:
    def __init__(self):
        self.conn = pyodbc.connect(
            'Driver={SQL Server Native Client 11.0};'
            'Server=ALEX-PC\ALEXSERVER;'
            'Database=PythonProject;'
            'Trusted_Connection=yes;')

    def get_conn(self):
        return self.conn

    def add_product(self, product):
        if not product.sku.strip():
            raise ValueError('Не заполнено свойство sku')
        if not product.name.strip():
            raise ValueError('Не заполнено свойство name')
        if product.qty == 0:
            raise ValueError('Не заполнено свойство qty')
        if not product.manufacter.strip():
            raise ValueError('Не заполнено свойство manufacter')
        if product.price == 0:
            raise ValueError('Не заполнено свойство price')
        if product.size == 0:
            raise ValueError('Не заполнено свойство size')
        if not product.color.strip():
            raise ValueError('Не заполнено свойство color')

        if product.__class__.__name__ in ['TShirtProduct', 'SneakersProduct']:
            query = r'''INSERT INTO product (sku, type_product, name, qty, manufacter, price, size, color)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?);'''
            cursor = self.conn.cursor()
            cursor.execute(query, (
                product.sku,
                product.__class__.__name__,
                product.name,
                product.qty,
                product.manufacter,
                product.price,
                product.size,
                product.color
            ))
            cursor.commit()
        elif product.__class__.__name__ == 'CustomizableSneakersProduct':
            if product.type_print:
                raise ValueError('Не заполнено свойство size')
            if product.shoe_laces:
                raise ValueError('Не заполнено свойство color')

            query = r'''INSERT INTO product (sku, type_product, name, qty, manufacter, price, size, color, type_print, shoe_laces)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'''
            cursor = self.conn.cursor()
            cursor.execute(query, (
                product.sku,
                product.__class__.__name__,
                product.name,
                product.qty,
                product.manufacter,
                product.price,
                product.size,
                product.color,
                product.type_print,
                product.shoe_laces,
            ))
            cursor.commit()
        else:
            raise TypeError('add_product error')

    def add_product_list(self, products_list):
        for product in products_list:
            self.add_product(product)

    def delete_product(self, sku):
        cursor = self.conn.cursor()
        query = 'DELETE FROM product WHERE sku = ?'
        cursor.execute(query, (sku))
        cursor.commit()

    def get_products(self):
        cursor = self.conn.cursor()
        query = 'SELECT sku, name, qty, manufacter, price, size, color, type_print, shoe_laces, type_product FROM product'
        cursor.execute(query)

        index = 9
        products = []
        for row in cursor:
            product = product_creator.create(row[index])
            product.parse_input(row)
            products.append(product)

        return products

    def report_by_field(self, field):
        db_field = ''
        if field == 'производитель':
            db_field = 'manufacter'
        elif field == 'размер':
            db_field = 'size'
        else:
            return

        cursor = self.conn.cursor()
        query = f'SELECT {db_field} AS field, COUNT({db_field}) AS field_count FROM product GROUP BY {db_field}'
        cursor.execute(query)

        result = []
        for row in cursor:
            result.append(row)

        return result