from good import Good
from whse import Whse

class WhseFilePersistable:
    def __init__(self, path):
        self.path = path

    def get_data(self):
        goods = {}

        with open(self.path, 'r') as f:
            next(f)
            for line in f:
                line = line[:-1]
                props = line.split(';')
                g = Good()
                g.id = int(props[0])
                g.name = props[1]
                g.qty = float(props[2])
                g.manufacter = props[3]
                g.price = float(props[4])
                g.size = props[5]
                goods[g.id] = g

        return goods

    def save_data(self, goods):
        f = open(self.path, 'w')
        f.write('ID;Название;Количество;Производитель;Цена;Размер\n')

        for good_id in goods.keys():
            g = goods[good_id]
            f.write(f'{g.id};{g.name};{g.qty};{g.manufacter};{g.price};{g.size}\n')

        f.close()