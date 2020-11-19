from db_service import WhseDbService

db = WhseDbService()

class Whse:
    #def __init__(self):

    def is_goods_exists(self):
        return (len(db.get_goods()) > 0)

    def add_good(self, good):
        db.add_good(good)

    def add_goods_list(self, goods_list):
        db.add_good_list(goods_list)

    def get_goods(self):
        return db.get_goods()

    def delete_good(self, id):
        db.delete_good(id)

    def report_by_field(self, field):
        return db.report_by_field(field)