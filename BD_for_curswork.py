import psycopg2
import sqlalchemy
from pprint import pprint

db = 'postgresql://py48galuta:1624@localhost:5432/postgres'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

list_of_start = [1, '2', 'иван', 'петров'], [2, '3', 'сергей', 'жирнов']



print("""Сейчас вы будете вводить лист""")

for str_bd in list_of_start:
    connection.execute(f"""
       INSERT INTO users(idusers, idvk, name, sername)
       VALUES({str_bd[0]},{str_bd[1]}, {str_bd[2]},{str_bd[2]});
       """)

print('ввод выполнен')