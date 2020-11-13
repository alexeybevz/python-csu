class GoodIdGenerator:
    def __init__(self):
        self.id = 0

    def set_id(self, goods):
        if len(goods) > 0:
            self.id = int(sorted(goods.keys())[-1])

    def inc_id(self):
        self.id = self.id + 1
        return self.id