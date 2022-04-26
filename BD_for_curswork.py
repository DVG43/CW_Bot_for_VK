import psycopg2
import sqlalchemy
from pprint import pprint
import work_with_Api




def writing_to_bd(list_of_start):
    db = 'postgresql://py48galuta:1624@localhost:5432/postgres' # запись в  БД
    engine = sqlalchemy.create_engine(db)
    connection = engine.connect()

    for str_bd in list_of_start:
        connection.execute(f"""
           INSERT INTO users(idusers, idvk, name, sername)
           VALUES {str_bd} ;
           """)

def reading_id_str():
    db = 'postgresql://py48galuta:1624@localhost:5432/postgres' #читаем какой последний номер в столбце
    engine = sqlalchemy.create_engine(db)
    connection = engine.connect()

    list_of_id = connection.execute("""
    SELECT idusers FROM users ;
    """).fetchall()
    return list_of_id[-1][0]


reading_id_str()

# list = [(1, 2, '{иван}', '{петров}'), (2, 3, '{сергей}', '{жирнов}')]
# # writing_to_bd(list)
# print('ввод выполнен')

