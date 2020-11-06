def main():
    whse = Whse()

    while True:
        print("Введение название:")
        name = input()

        print("Введение количество:")
        qty = input()

        good = Good(name, qty)

        whse.addGood(good)

        print("Вывести все:")
        resultDialog = input()

        if resultDialog == "да":
            print("Информация о складе:")
            for good in whse.getGoods():
                print(good.name + " - " + str(good.qty))

class Good:
    def __init__(self, name, qty):
        self.name = name
        self.qty = qty

class Whse:
    goods = []

    def addGood(self, good):
        if good is not None:
            self.goods.append(good)

    def getGoods(self):
        return self.goods

main()