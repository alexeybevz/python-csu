import pyodbc
from good import Good

class WhseDbService:
    def __init__(self):
        self.conn = pyodbc.connect(
            'Driver={SQL Server Native Client 11.0};'
            'Server=ALEX-PC\ALEXSERVER;'
            'Database=PythonProject;'
            'Trusted_Connection=yes;')

    def add_good(self, good):
        cursor = self.conn.cursor()
        query = r'''INSERT INTO whse (good_name, qty, manufacter, price, size)
                    VALUES (?, ?, ?, ?, ?);'''
        cursor.execute(query, (good.name, good.qty, good.manufacter, good.price, good.size))

        good_id = cursor.execute('SELECT @@IDENTITY AS id;').fetchone()[0]
        cursor.commit()
        good.id = good_id
        return good

    def add_good_list(self, goods_list):
        for good in goods_list:
            self.add_good(good)

    def delete_good(self, id):
        cursor = self.conn.cursor()
        query = 'DELETE FROM whse WHERE id = ?'
        cursor.execute(query, (id))
        cursor.commit()

    def get_goods(self):
        cursor = self.conn.cursor()
        query = 'SELECT id, good_name, qty, manufacter, price, size FROM whse'
        cursor.execute(query)

        goods = []
        for row in cursor:
            g = Good()
            g.id = row[0]
            g.name = row[1]
            g.qty = row[2]
            g.manufacter = row[3]
            g.price = row[4]
            g.size = row[5]
            goods.append(g)

        return goods

    def report_by_field(self, field):
        db_field = ''
        if field == 'производитель':
            db_field = 'manufacter'
        elif field == 'размер':
            db_field = 'size'
        else:
            return

        cursor = self.conn.cursor()
        query = f'SELECT {db_field} AS field, COUNT(id) AS field_count FROM whse GROUP BY {db_field}'
        cursor.execute(query)

        result = []
        for row in cursor:
            result.append(row)

        return result