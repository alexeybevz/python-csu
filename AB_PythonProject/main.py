class Good:
    def __init__(self, name, qty):
        self.name = name
        self.qty = qty


class Whse:
    def __init__(self):
        self.goods = {}

    def addGood(self, good):
        self.goods[good.name] = good.qty
        # self.goods.append(good)

    def getGoods(self):
        return self.goods

    def delGoods(self, key):
        self.goods.pop(key, None)


def add(whse):
    print("Введение название:")
    name = input()
    print("Введение количество:")
    qty = input()
    good = Good(name, qty)

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
