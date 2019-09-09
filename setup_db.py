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
                                        last_name text,
                                        first_name text,
                                        birthyear text,
                                        birthmonth text,
                                        birthday text,
                                        visit_date text,
                                        visit_type text,
                                        directed text,
                                        complaints text,
                                        sicktime text,
                                        prev_treatment text,
                                        other_illness text,
                                        diabetes text,
                                        infections text,
                                        allergy text,
                                        drug_allergy text,
                                        heredity text,
                                        medicaments text,
                                        addictions text,
                                        blood_donor text,
                                        loc_stat text,
                                        process_characteristic text,
                                        skin_of text,
                                        symptoms text,
                                        dermographism1 text,
                                        dermographism2 text,
                                        mucous_membranes text,
                                        mucous_membranes2 text,
                                        lymph text,
                                        lymph_description text,
                                        lymph_description1 text,
                                        lymph_description2 text,
                                        lymph_description4 text,
                                        lymph_description6 text,
                                        lymph_description5 text,
                                        hair_description text,
                                        hair_description2 text,
                                        nails_of text,
                                        nails_desc text,
                                        additional_symp text,
                                        scabies_comment text,
                                        diagnosis_main text,
                                        form text,
                                        stage text,
                                        code text,
                                        diagnosis2 text,
                                        complication text,
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
                                        comeback text,
                                        doctor text
                                        );"""
    sql_create_diagnosis_table = """ CREATE TABLE IF NOT EXISTS Diagnosis
    (                                   diagnosis_main text PRIMARY KEY,
                                        form text,
                                        stage text,
                                        code text,
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
                                        last_name text,
                                        first_name text,
                                        birthyear text,
                                        birthmonth text,
                                        birthday text,
                                        visit_date text,
                                        visit_type text,
                                        directed text,
                                        complaints text,
                                        sicktime text,
                                        prev_treatment text,
                                        other_illness text,
                                        diabetes text,
                                        infections text,
                                        allergy text,
                                        drug_allergy text,
                                        heredity text,
                                        medicaments text,
                                        addictions text,
                                        blood_donor text,
                                        loc_stat text,
                                        process_characteristic text,
                                        skin_of text,
                                        symptoms text,
                                        dermographism1 text,
                                        dermographism2 text,
                                        mucous_membranes text,
                                        mucous_membranes2 text,
                                        lymph text,
                                        lymph_description text,
                                        lymph_description1 text,
                                        lymph_description2 text,
                                        lymph_description4 text,
                                        lymph_description6 text,
                                        lymph_description5 text,
                                        hair_description text,
                                        hair_description2 text,
                                        nails_of text,
                                        nails_desc text,
                                        additional_symp text,
                                        scabies_comment text,
                                        diagnosis_main text,
                                        form text,
                                        stage text,
                                        code text,
                                        diagnosis2 text,
                                        complication text,
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
                                        comeback text,
                                        doctor text
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
