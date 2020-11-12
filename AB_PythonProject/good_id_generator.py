class GoodIdGenerator:
    def __init__(self):
        self.id = 0

    def inc_id(self):
        self.id = self.id + 1
        return self.id