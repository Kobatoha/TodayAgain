import duckdb

path = 'Database/duckdb/'
file_db = 'test.db'
table = 'monday'


def connect(path='Database/duckdb/', file_db='test.db'):
    con = duckdb.connect(path + file_db)
    return con


def create_table():
    with connect() as con:
        con.sql('CREATE TABLE monday (time TIME, task VARCHAR)')


def get_table_data(table=''):
    with connect() as con:
        data = con.sql(f"SELECT * FROM {table}").fetchall()
    return data
