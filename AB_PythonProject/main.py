import os
from good import Good
from whse import Whse
from good_id_generator import GoodIdGenerator
from whse_file_persistable import WhseFilePersistable

current_dir = os.path.dirname(os.path.realpath(__file__))
whse = Whse()
goodIdGenerator = GoodIdGenerator()
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

    goodIdGenerator.set_id(whse.get_goods())
    new_id = goodIdGenerator.inc_id()

    good = Good()
    good.id = new_id
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
    for good_id in goods.keys():
        g = goods[good_id]
        print(f'{g.id} - {g.name} - {g.qty} - {g.manufacter} - {g.price} - {g.size}')

def report_by_field(field):
    if field == 'производитель':
        print('Статистика по производителю\n')
    elif field == 'размер':
        print('Статистика по размерам\n')
    else:
        return

    goods = whse.get_goods().values()
    result = {}

    for g in goods:
        key = ""
        if field == 'производитель':
            key = g.manufacter
        elif field == 'размер':
            key = g.size
        else:
            return

        if key in result:
            result[key] = result[key] + 1
        else:
            result[key] = 1
    
    for k in result.keys():
        print(f'{k} - {result[k]}')

    print('\n')

def add_goods_runtime(path):
    whseReader = WhseFilePersistable(path)
    goods = whseReader.get_data()
    goodIdGenerator.set_id(whse.get_goods())    
    for k in goods.keys():
        goods[k].id = goodIdGenerator.inc_id()
    whse.add_goods_list(goods)

is_start_program = True
while True:
    if is_start_program:
        is_start_program = False
        whse.add_goods_list(whseFilePersistable.get_data())

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
        add_goods_runtime(current_dir + '\\' + file_name)
    elif mode == 5:
        report_by_field('производитель')
        report_by_field('размер')
    elif mode == 6:
        whseFilePersistable.save_data(whse.get_goods())
        break
    else:
        break
