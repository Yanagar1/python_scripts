#----DATA INITIALIZER FILE-----
import sqlite3,  datetime,  os
import numpy as np
from tkinter import *
from tkcalendar import *
from tkinter import ttk

#create a db connection to the SQLite db specified by db_file
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return None

def create_table(connection,  create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = connection.cursor()
        c.execute(create_table_sql) # Create table
    except Exception as e:
        print(e)

def db_setup():
    file = "patients.db"
    db_file_path = os.path.join(os.getcwd(),  file)
    database = db_file_path
    print(database)
    sql_create_visits_table = """ CREATE TABLE IF NOT EXISTS patients_and_visits
    (                                   id integer AUTOINCREMENT,
                                        last_name text NOT NULL,
                                        first_name text,
                                        birthyear text NOT NULL,
                                        birthmonth text NOT NULL,
                                        birthday text NOT NULL,
                                        visit_date text NOT NULL,
                                        visit_type text,
                                        directed text,
                                        complaints text,
                                        sicktime text,
                                        prev_treatment text,
                                        other_illness text,
                                        diabetes text,
                                        infect text,
                                        allergy text,
                                        drug_allergy text,
                                        heredity text,
                                        medicaments text,
                                        addictions text,
                                        blood_donor text,
                                        loc_stat text,
                                        process_characteristic text,
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
    connection = create_connection(database)
    if connection is not None:
        create_table(connection,  sql_create_patients_and_visits_table)
        connection.commit()
        connection.close()
    else:
        print("Error")
#database setup - only run once

# Insert a row of data
#c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)")

# Save (commit) the changes
#connection.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#connection.close()
    return

"""def generate_id(last_name, birthyear,  birthmonth, visit_date):
    letters_in_string = "{}{}{}".format(last_name[0:5], str(birthyear)[2:], str(birthmonth) )
    patient_id = ""
    for char in letters_in_string:
        patient_id = "{}{}".format(patient_id,  ord(char))
    patient_id = int("{}{}{}{}".format(patient_id,  b,  birthmonth,  birthday))
    print (patient_id)
    return patient_id"""

class Visit:
    def __init__(self, last_name: str, first_name: str,  birthyear: str,
    birthmonth: str,  birthday: str, visit_date: str,
    visit_type: str, directed: str, complaints: str, sicktime: str, prev_treatment: str,
    other_illness: str, diabetes: str, infect: str, allergy: str, drug_allergy: str,
    heredity: str, medicaments: str, addictions: str, blood_donor: str, loc_stat: str,
    process_characteristic: str, symptoms: str, dermographism1: str, dermographism2: str,
    mucous_membranes: str, mucous_membranes2: str, lymph: str, lymph_description: str,
    lymph_description1: str, lymph_description2: str, lymph_description4: str,
    lymph_description6: str, lymph_description5: str, hair_description: str,
    hair_description2: str, nails_of: str, nails_desc: str, additional_symp: str,
    tkvr: str, diagnosis_main: str, form: str, stage: str, code: str, diagnosis2: str,
    complication: str, treatment: str, treatment2: str, treatment3: str, treatment4: str,
    treatment5: str, treatment6: str, recomm: str, recomm2: str, recomm3: str,
    recomm4: str, recomm5: str, recomm6: str, comeback: str, doctor: str):

            self.last_name = last_name
            self.first_name = first_name
            self.birthyear = birthyear
            self.birthmonth = birthmonth
            self.birthday = birthday
            self.visit_date = visit_date
            self.visit_type = visit_type
            self.directed = directed
            self.complaints = complaints
            self.sicktime = sicktime
            self.prev_treatment = prev_treatment
            self.other_illness = other_illness
            self.diabetes = diabetes
            self.infect = infect
            self.allergy = allergy
            self.drug_allergy = drug_allergy
            self.heredity = heredity
            self.medicaments = medicaments
            self.addictions = addictions
            self.blood_donor = blood_donor
            self.loc_stat = loc_stat
            self.process_characteristic = process_characteristic
            self.symptoms = symptoms
            self.dermographism1 = dermographism1
            self.dermographism2 = dermographism2
            self.mucous_membranes = mucous_membranes
            self.mucous_membranes2 = mucous_membranes2
            self.lymph = lymph
            self.lymph_description = lymph_description
            self.lymph_description1 = lymph_description1
            self.lymph_description2 = lymph_description2
            self.lymph_description4 = lymph_description4
            self.lymph_description6 = lymph_description6
            self.lymph_description5 = lymph_description5
            self.hair_description = hair_description
            self.hair_description2 = hair_description2
            self.nails_of = nails_of
            self.nails_desc = nails_desc
            self.additional_symp = additional_symp
            self.scabies_comment = tkvr
            self.diagnosis_main = diagnosis_main
            self.form = form
            self.stage = stage
            self.code = code
            self.diagnosis2 = diagnosis2
            self.complication = complication
            self.treatment = treatment
            self.treatment2 = treatment2
            self.treatment3 = treatment3
            self.treatment4 = treatment4
            self.treatment5 = treatment5
            self.treatment6 = treatment6
            self.recomm = recomm
            self.recomm2 = recomm2
            self.recomm3 = recomm3
            self.recomm4 = recomm4
            self.recomm5 = recomm5
            self.recomm6 = recomm6
            self.comeback = comeback
            self.doctor = doctor

def find_patient_in_db(last_name,  value): #standard search by last name
    c.execute("""SELECT * FROM patients_and_visits WHERE last_name MATCH value""")
    #c.execute(search for the patient)
    #if found: retrieve
    return

def add_patient_to_db(input_visit_date,  input_name,  input_birthdate,  number_of_visits,  input_illness_description,  input_diagnosis,  input_treatment):
#program somewhere that some values could be null
#call find_patient_in_db - if not found,  proceed
#if found: show data
#call the class object
#assign VALUES
#add to the database
    return

saved_for_later = []

def delete_patient_db(search_by,  value):
    #execute(select from and delete)
    return

def clean_name(some_var):
    return ''.join(char for char in some_var if char.isalnum())

#-- LISTS----
visit_types = {'Первый',  'Повторный после лечения'}
donor = {'Является',  'Не является'}
process = ['острый',  'подострый',  'хронический',  'невоспалительный',  'ограниченный',  'нераспространенный',  'распространенный',  'несимметричный',  'симметричный',  'генерализованный']
derm = {'красный', 'белый', 'смешанный'}
derm2 = {'стойкий', 'нестойкий'}
surf = {'ротовой полости', 'аногенитальной области'}
surf2 = {'розовые чистые', 'желтоватые', 'бледные', 'цианотичные'}
l3 = {'болезненные', 'безболезненные'}
l4 = {'плотные', 'мягкие'}
l5 = {'неподвижные', 'подвижные'}
l7 = {'женскому', 'мужскому'}

years = []
for i in range(datetime.date.today().year - 100,  datetime.date.today().year+1):
    years.append(i)

months = []
for i in range(1,  13):
    months.append(i)

days = []
for i in range(1,  32):
    days.append(i)
