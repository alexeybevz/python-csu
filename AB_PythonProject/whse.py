class Whse:
    def __init__(self):
        self.goods = {}

    def is_goods_exists(self):
        return (len(self.goods) > 0)

    def add_good(self, good):
        self.goods[good.id] = good

    def add_goods_list(self, goods_dict):
        for good_id in goods_dict.keys():
            self.goods[good_id] = goods_dict[good_id]

    def get_goods(self):
        return self.goods

    def delete_good(self, key):
        self.goods.pop(key, None)