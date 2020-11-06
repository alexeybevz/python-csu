class Good:
    def __init__(self, name, qty, manufacturer, price, size):
        self.name = name
        self.qty = qty
        self.manufacturer = manufacturer
        self.price = price
        self.size = size


class Whse:
    def __init__(self):
        self.goods = {}

    def addGood(self, good):
        self.goods[good.name] = good.qty

    def getGoods(self):
        return self.goods

    def delGoods(self, key):
        self.goods.pop(key, None)

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
    good = Good(name, qty, manufacturer, price, size)

    whse.addGood(good)


def report(whse):
    print("Информация о складе:")
    info = whse.getGoods()
    for good in whse.getGoods().keys():
        print(f'{good} - {info[good]}')
    print('\n')


whse = Whse()
while True:
    print('1-добавить\n2-Вывести все\n3-удалить\n4-выйти\n')
    name = int(input())
    if name == 1:
        add(whse)
    elif name == 2:
        report(whse)
    elif name == 3:
        report(whse)
        key = input('введите ключ\n')
        whse.delGoods(key)
    else:
        break
