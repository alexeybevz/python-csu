import os
from domain.product import Product
from domain.tshirt_product import TShirtProduct
from domain.sneakers_product import SneakersProduct
from domain.customizable_sneakers_product import CustomizableSneakersProduct
from db_service import DbService
from whse_file_persistable import WhseFilePersistable

current_dir = os.path.dirname(os.path.realpath(__file__))
db = DbService()
whseFilePersistable = WhseFilePersistable(current_dir + r'\whse.txt')

def report():
    products = db.get_products()

    print('Информация о товарах на складе:')
    if len(products) == 0:
        print('Склад пуст.')
        return

    print('Артикул - Тип - Название - Количество - Производитель - Цена - Размер - Цвет')
    for p in products:
        print(f'{p.sku} - {p.type_product} - {p.name} - {p.qty} - {p.manufacter} - {p.price} - {p.color}')

def report_by_field(field):
    if field == 'производитель':
        print('Статистика по производителю\n')
    elif field == 'размер':
        print('Статистика по размерам\n')
    else:
        return

    result = db.report_by_field(field)
    for row in result:
        f, count = row
        print(f'{f} - {count}')

    print('\n')

def add_goods_runtime(path):
    whseReader = WhseFilePersistable(path)
    goods = whseReader.get_data()
    db.add_goods_list(goods)

type_products = [ '1-TShirt', '2-Sneakers', '3-CustSneakers']

while True:
    print('\n1-добавить\n2-вывести все\n3-удалить\n4-дозагрузить остатки\n5-статистика\n6-выйти\n')
    mode = int(input())
    if mode == 1:
        selected_type_product = input(f'Введите тип товара ({type_products}):')
        if selected_type_product == '1':
            product = TShirtProduct()
        elif selected_type_product == '2':
            product = SneakersProduct()
        elif selected_type_product == '3':
            product = CustomizableSneakersProduct()
        else:
            raise TypeError('Неверный тип товара')
        product.console_input()
        db.add_product(product)
    elif mode == 2:
        report()
    elif mode == 3:
        report()
        sku = int(input('Введите артикул удаляемого товара:\n'))
        db.delete_product(sku)
    elif mode == 4:
        print('Укажите название файла. Файл должен находиться в текущей директории.')
        file_name = input()
        add_goods_runtime(f'{current_dir}\\{file_name}')
    elif mode == 5:
        report_by_field('производитель')
        report_by_field('размер')
    elif mode == 6:
        whseFilePersistable.save_data(db.get_goods())
        break
    else:
        break
