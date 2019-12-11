import MySQLdb

class Conexao:
    def __init__(self):
        self.conn = MySQLdb.connect(
            host = 'mysql.topskills.study',
            database = 'topskills09',
            user = 'topskills09',
            password = 'Jonas2019' 
        )
        self.cursor = self.conn.cursor()