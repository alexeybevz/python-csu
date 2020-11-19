import os
from good import Good
from whse import Whse
from whse_file_persistable import WhseFilePersistable

current_dir = os.path.dirname(os.path.realpath(__file__))
whse = Whse()
whseFilePersistable = WhseFilePersistable(current_dir + r'\whse.txt')

def add(whse):
    print("Введение название:")
    name = input()
    print("Введение количество:")
    qty = input()
    print("Введение производителя:")
    manufacturer = input()
    print("Введение цену:")
    price = input()
    print("Введение размер:")
    size = input()

    good = Good()
    good.name = name
    good.qty = float(qty)
    good.manufacter = manufacturer
    good.price = float(price)
    good.size = size
    whse.add_good(good)

def report(whse):
    print('Информация о товарах на складе:')
    if not whse.is_goods_exists():
        print('Склад пуст.')
        return

    goods = whse.get_goods()
    print('ID - Название - Количество - Производитель - Цена - Размер')
    for g in goods:
        print(f'{g.id} - {g.name} - {g.qty} - {g.manufacter} - {g.price} - {g.size}')

def report_by_field(field):
    if field == 'производитель':
        print('Статистика по производителю\n')
    elif field == 'размер':
        print('Статистика по размерам\n')
    else:
        return

    result = whse.report_by_field(field)
    for row in result:
        f, count = row
        print(f'{f} - {count}')

    print('\n')

def add_goods_runtime(path):
    whseReader = WhseFilePersistable(path)
    goods = whseReader.get_data()
    whse.add_goods_list(goods)

while True:
    print('\n1-добавить\n2-вывести все\n3-удалить\n4-дозагрузить остатки\n5-статистика\n6-выйти\n')
    mode = int(input())
    if mode == 1:
        add(whse)
    elif mode == 2:
        report(whse)
    elif mode == 3:
        report(whse)
        id = int(input('Введите id удаляемого товара:\n'))
        whse.delete_good(id)
    elif mode == 4:
        print('Укажите название файла. Файл должен находиться в текущей директории.')
        file_name = input()
        add_goods_runtime(f'{current_dir}\\{file_name}')
    elif mode == 5:
        report_by_field('производитель')
        report_by_field('размер')
    elif mode == 6:
        whseFilePersistable.save_data(whse.get_goods())
        break
    else:
        break
