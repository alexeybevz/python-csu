from good import Good
from whse import Whse
from good_id_generator import GoodIdGenerator

whse = Whse()
goodIdGenerator = GoodIdGenerator()

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
    good.id = goodIdGenerator.inc_id()
    good.name = name
    good.qty = qty
    good.manufacter = manufacturer
    good.price = price
    good.size = size
    whse.add_good(good)

def report(whse):
    print('Информация о товарах на складе:')
    if not whse.is_goods_exists():
        print('Склад пуст.')
        return

    goods = whse.get_goods()
    print('Название - Количество - Производитель - Цена - Размер')
    for good_id in goods.keys():
        g = goods[good_id]
        print(f'{g.id} - {g.name} - {g.qty} - {g.manufacter} - {g.price} - {g.size}')

while True:
    print('\n1-добавить\n2-вывести все\n3-удалить\n4-выйти\n')
    mode = int(input())
    if mode == 1:
        add(whse)
    elif mode == 2:
        report(whse)
    elif mode == 3:
        report(whse)
        id = int(input('Введите id удаляемого товара:\n'))
        whse.delete_good(id)
    else:
        break
