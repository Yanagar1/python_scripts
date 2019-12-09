import sqlite3, os
from patients2 import *
#create a db connection to the SQLite db specified by db_file
#only run once

def create_table(connection,  create_table_sql):
    try:
        c = connection.cursor()
        c.execute(create_table_sql) # Create table
    except Exception as e:
        print(e)

def db_setup():
    file = "patients.db"
#    db_file_path = os.path.join(os.getcwd(),  file)
#    database = db_file_path
    sql_create_visits_table = """ CREATE TABLE IF NOT EXISTS visits
    (                                   id INTEGER PRIMARY KEY,
                                        Фамилия text,
                                        Имя text,
                                        Год_Рождения text,
                                        Месяц_Рождения text,
                                        День_Рождения text,
                                        Дата_визита text,
                                        Тип_визита text,
                                        Направлен text,
                                        Жалобы text,
                                        Болен text,
                                        Лечение_Самолечение text,
                                        Сопутствующие_заболевания text,
                                        Сахарный_диабет text,
                                        Инфекционные_заболевания text,
                                        Пищевая_аллергия text,
                                        Лекарственная_непереносимость text,
                                        Наследственность text,
                                        препараты text,
                                        Вредные_привычки text,
                                        Донор text,
                                        Локальный_статус text,
                                        Характер_процесса text,
                                        На_коже text,
                                        Высыпания_представлены text,
                                        Дермографизм1 text,
                                        Дермографизм2 text,
                                        Слизистые text,
                                        Слизистые2 text,
                                        Лимфузлы text,
                                        Лимфузлы0 text,
                                        Лимфузлы1 text,
                                        Лимфузлы2 text,
                                        Лимфузлы4 text,
                                        Лимфузлы6 text,
                                        Лимфузлы5 text,
                                        Оволосение text,
                                        Волосы text,
                                        Ногктевые_пластины text,
                                        Ногктевые_пластины2 text,
                                        Доп_симптомы text,
                                        чесотка_педикулез text,
                                        Диагноз_основной text,
                                        Форма text,
                                        Стадия text,
                                        Код_МКБ text,
                                        Диагноз_сопутствующий text,
                                        Осложнения text,
                                        treatment text,
                                        treatment2 text,
                                        treatment3 text,
                                        treatment4 text,
                                        treatment5 text,
                                        treatment6 text,
                                        recomm text,
                                        recomm2 text,
                                        recomm3 text,
                                        recomm4 text,
                                        recomm5 text,
                                        recomm6 text,
                                        Повторная_явка text,
                                        Врач text
                                        );"""
    sql_create_diagnosis_table = """ CREATE TABLE IF NOT EXISTS Diagnosis
    (                                   Диагноз_основной text PRIMARY KEY,
                                        Форма text,
                                        Стадия text,
                                        Код_МКБ text,
                                        treatment text,
                                        treatment2 text,
                                        treatment3 text,
                                        treatment4 text,
                                        treatment5 text,
                                        treatment6 text,
                                        recomm text,
                                        recomm2 text,
                                        recomm3 text,
                                        recomm4 text,
                                        recomm5 text,
                                        recomm6 text
                                        );"""
    sql_create_not_finished_table = """ CREATE TABLE IF NOT EXISTS not_finished
    (                                   id INTEGER PRIMARY KEY,
                                        Фамилия text,
                                        Имя text,
                                        Год_Рождения text,
                                        Месяц_Рождения text,
                                        День_Рождения text,
                                        Дата_визита text,
                                        Тип_визита text,
                                        Направлен text,
                                        Жалобы text,
                                        Болен text,
                                        Лечение_Самолечение text,
                                        Сопутствующие_заболевания text,
                                        Сахарный_диабет text,
                                        Инфекционные_заболевания text,
                                        Пищевая_аллергия text,
                                        Лекарственная_непереносимость text,
                                        Наследственность text,
                                        препараты text,
                                        Вредные_привычки text,
                                        Донор text,
                                        Локальный_статус text,
                                        Характер_процесса text,
                                        На_коже text,
                                        Высыпания_представлены text,
                                        Дермографизм1 text,
                                        Дермографизм2 text,
                                        Слизистые text,
                                        Слизистые2 text,
                                        Лимфузлы text,
                                        Лимфузлы0 text,
                                        Лимфузлы1 text,
                                        Лимфузлы2 text,
                                        Лимфузлы4 text,
                                        Лимфузлы6 text,
                                        Лимфузлы5 text,
                                        Оволосение text,
                                        Волосы text,
                                        Ногктевые_пластины text,
                                        Ногктевые_пластины2 text,
                                        Доп_симптомы text,
                                        чесотка_педикулез text,
                                        Диагноз_основной text,
                                        Форма text,
                                        Стадия text,
                                        Код_МКБ text,
                                        Диагноз_сопутствующий text,
                                        Осложнения text,
                                        treatment text,
                                        treatment2 text,
                                        treatment3 text,
                                        treatment4 text,
                                        treatment5 text,
                                        treatment6 text,
                                        recomm text,
                                        recomm2 text,
                                        recomm3 text,
                                        recomm4 text,
                                        recomm5 text,
                                        recomm6 text,
                                        Повторная_явка text,
                                        Врач text
                                        );"""
    connection =  create_connection()
    if connection is not None:
        create_table(connection,  sql_create_visits_table)
        create_table(connection,  sql_create_diagnosis_table)
        create_table(connection,  sql_create_not_finished_table)
        connection.commit()
        connection.close()
    else:
        print("Error")
    return

db_setup()
#database setup - only run once

# Insert a row of data
#c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)")

# Save (commit) the changes
#connection.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#connection.close()
