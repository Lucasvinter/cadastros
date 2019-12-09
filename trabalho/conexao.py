import MySQLdb

conn = MySQLdb.connect(
    host = 'mysql.topskills.study',
    database = 'topskills09',
    user = 'topskills09',
    password = 'Jonas2019' 
)
cursor = conn.cursor()