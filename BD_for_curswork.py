import psycopg2
import sqlalchemy


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
    #print(list_of_id)
    return list_of_id


def foming_data_list(data_list, numer):
    id_str = numer
    data_list = []
    for person in data_list:
        a = id_str
        b = person ['id']
        c = f"{ person ['first_name']}"
        d = f"{ person ['last_name']}"
        data_tupie = (a, b, c, d)
        data_list.append(data_tupie)
        id_str += 1
    return data_list


def cheking_dubles(cheking_list):
    db = 'postgresql://py48galuta:1624@localhost:5432/postgres'  # читаем какой последний номер в столбце

    engine = sqlalchemy.create_engine(db)
    connection = engine.connect()

    list_of_idvk = connection.execute("""
        SELECT idvk FROM users ;
        """).fetchall()
    cheiging_list = []
    for person_1 in cheking_list:
        if person_1['id'] in list_of_idvk:
            continue
        else:
            cheiging_list.append(person_1)
    return cheiging_list





#reading_id_str()

# list = [(1, 2, '{иван}', '{петров}'), (2, 3, '{сергей}', '{жирнов}')]
# # writing_to_bd(list)
# print('ввод выполнен')
# [{'id': 147075112, 'first_name': 'Светлана', 'last_name': 'Паршуто', 'can_access_closed': False, 'is_closed': True, 'track_code': '12458a9ewiUBeU7xYxsZBnyaj4dr65T0R04QOdRvhIqu7UUiuRahXwYldvgzShwDSXV9S02DmvJEThA3sg'}, {'id': 82128228, 'first_name': 'Ольга', 'last_name': 'Туманская', 'can_access_closed': False, 'is_closed': True, 'track_code': '2b2900e3dgV7RuiAfO7s4SrsRPGQIdQzgSu8FdaSOuhwlx52aTAVfyEZ1Np-6rjqGQC_Cd1FySyMPM4b'}, {'id': 608261659, 'first_name': 'Анна', 'last_name': 'Пилеева', 'can_access_closed': True, 'is_closed': False, 'track_code': 'b3ec2c25MiSYfTYXQpebX_lSmeINb43PnFjO4BpM2oVFVu0rosRRXsgjWRFAl8payrpvJSsHg8mfWM7ufA'}, {'id': 73250920, 'first_name': 'Наталья', 'last_name': 'Викторова', 'can_access_closed': False, 'is_closed': True, 'track_code': '2a350de4w2qPpRIrCC241PnrSeXPmSgjBf9G4poItO5OYx6POw2gENX-LXpfJuzXwwe6HYL9NTwI6DTs'}, {'id': 351527234, 'first_name': 'Екатерина', 'last_name': 'Жаринова', 'can_access_closed': False, 'is_closed': True, 'track_code': '6cdde110Z02qfhGkNTTZaJLGTACZngesnqfv_ABthJt4KUpL_PsEN_olL_M1M9psoSq8yr_2Caqdp-_yZg'}, {'id': 647998500, 'first_name': 'Евгения', 'last_name': 'Кадушкина', 'can_access_closed': True, 'is_closed': False, 'track_code': 'b444b5133S8FUO9v_vjYiNC7XYgZ6EgZ_psTqaS9yL3dgLGLJN6-VQML0Dv5-4DU7VCuRj-ARh_9mxOnwg'}, {'id': 24629362, 'first_name': 'Викуся', 'last_name': 'Грязнова', 'can_access_closed': False, 'is_closed': True, 'track_code': '28e9902bF0nSfnEUBhWIC19m95cEUhEBB3gFYIbjypktH2EjH8N0M4l0QBADEIlWao4Gb0k2DB4Kb3du'}, {'id': 1787828, 'first_name': 'Юлия', 'last_name': 'Фролова', 'can_access_closed': True, 'is_closed': False, 'track_code': '878f0e5fPWijKhutEfzYhSISWZVzlMa61Ibq6lcvzPfC8MLiI6VeEvcgf6RF8Y7YF_ScBjLjwqvO45g'}, {'id': 451415886, 'first_name': 'Татьяна', 'last_name': 'Харвонен', 'can_access_closed': True, 'is_closed': False, 'track_code': 'ffc52771ZhIBfPSlsofu3UFgJGe5r1m5dhkHcEljQG_yU3FHGqIFaAd3zqK_juLdfIbfr5_HV791GQd-Lw'}]
