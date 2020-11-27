import os
from product_creator import ProductCreator
from db_service import DbService
from whse_file_persistable import WhseFilePersistable

current_dir = os.path.dirname(os.path.realpath(__file__))
db = DbService()
product_creator = ProductCreator()
whseFilePersistable = WhseFilePersistable(current_dir + r'\whse.csv')

def report():
    products = db.get_products()

    print('Информация о товарах на складе:')
    if len(products) == 0:
        print('Склад пуст.')
        return

    for p in products:
        p.console_output()

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

type_products = { 1: 'TShirtProduct', 2: 'SneakersProduct', 3: 'CustomizableSneakersProduct' }

while True:
    print('\n1-добавить\n2-вывести все\n3-удалить\n4-дозагрузить остатки\n5-статистика\n6-выйти\n')
    mode = int(input())
    if mode == 1:
        s = ''
        for k, v in type_products.items():
            s = s + f'{k}-{v}; '

        selected_type_product = int(input(f'Введите тип товара ({s[:-1]}):'))
        product = product_creator.create(type_products[selected_type_product])
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
        whseReader = WhseFilePersistable(f'{current_dir}\\{file_name}')
        products = whseReader.get_data()
        db.add_product_list(products)
    elif mode == 5:
        report_by_field('производитель')
        report_by_field('размер')
    elif mode == 6:
        whseFilePersistable.save_data(db.get_products())
        break
    else:
        break
