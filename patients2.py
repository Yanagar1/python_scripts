#----DATA INITIALIZER FILE-----CROSS PLATFORMS
import sqlite3,  datetime, os
from tkinter import *
from tkcalendar import *
from tkinter import ttk, messagebox, filedialog
from fpdf import FPDF
from textwrap import *
import random
import atexit

id_taken = []
#check for necessary input to make an id
def check_input_none(last_name, visit_date):
    c = [last_name, visit_date]
    for i in c:
        if len(i)==0:
            return 0
    return 1

#helper function to check if a value is in list for combobox, then append
#returns index of the variable
def check_dupli(list, variable):
    if variable not in list:
        list.append(variable)
        current_index = (len(list)-1)
    else: #value already exists
        current_index = list.index(variable)
    return current_index

def generate_id():
    visit_id = ""
    for x in range (6):
        visit_id = "{}{}".format(visit_id, random.randint(0, 10))
    visit_id = int(visit_id)
    if visit_id not in id_taken:
        id_taken.append(visit_id)
        return visit_id
    else:
        generate_id()


#split lines for nice pdf
def line_splitter(entry_text):
    my_wrap = TextWrapper(width = 90)
    wrap_list = my_wrap.wrap(text=entry_text)
    return wrap_list

class Visit:
    def __init__(self, last_name: str, first_name: str, visit_id: int, birthyear: str,
    birthmonth: str,  birthday: str, visit_date: str,
    visit_type: str, directed: str, complaints: str, sicktime: str, prev_treatment: str,
    other_illness: str, diabetes: str, infect: str, allergy: str, drug_allergy: str,
    heredity: str, medicaments: str, addictions: str, blood_donor: str, loc_stat: str,
    process_characteristic, skin_of: str, symptoms: str, dermographism1: str, dermographism2: str,
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
            self.visit_id = visit_id
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
            self.skin_of = skin_of
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

saved_for_later = []

#creates new scrollable frame
def new_frame(frame, height):
    #canvas, frame, window, scroll
    mycanvas = Canvas(frame, width=600, height=500, scrollregion=(0,0,680, 500))
    mycanvas.grid(row=0, column=0, sticky="nsew")

    myframe1 = Frame(mycanvas, width=600, height=500, background = "snow")
    myframe1.grid(row = 0, column = 0)
    myframe1.rowconfigure(0, weight=1)
    myframe1.columnconfigure(0, weight=1)
    mycanvas.create_window(20, 5, width = 600, height = height, window = myframe1, anchor = NW)

    canvbar = Scrollbar(frame, orient = "vertical", command = mycanvas.yview)
    canvbar.grid(row = 0, column = 1, sticky="ns")
    mycanvas.configure(yscrollcommand = canvbar.set)
    mycanvas.configure(scrollregion=mycanvas.bbox("all"))
    return myframe1

def save_to_text():
    #unfinished cards write to a text file
    if len(saved_for_later)==0:
        return
    else:
        with open('unfinished_cards.txt', 'w', -1, "utf-8") as f:
            for i in saved_for_later:
                f.write(str(i.last_name))
                f.write(";")
                f.write(str(i.first_name))
                f.write(";")
                f.write(str(i.visit_id))
                f.write(";")
                f.write(str(i.birthyear))
                f.write(";")
                f.write(str(i.birthmonth))
                f.write(";")
                f.write(str(i.birthday))
                f.write(";")
                f.write(str(i.visit_date))
                f.write(";")
                f.write(str(i.visit_type))
                f.write(";")
                f.write(str(i.directed))
                f.write(";")
                f.write(str(i.complaints))
                f.write(";")
                f.write(str(i.sicktime))
                f.write(";")
                f.write(str(i.prev_treatment))
                f.write(";")
                f.write(str(i.other_illness))
                f.write(";")
                f.write(str(i.diabetes))
                f.write(";")
                f.write(str(i.infect))
                f.write(";")
                f.write(str(i.allergy))
                f.write(";")
                f.write(str(i.drug_allergy))
                f.write(";")
                f.write(str(i.heredity))
                f.write(";")
                f.write(str(i.medicaments))
                f.write(";")
                f.write(str(i.addictions))
                f.write(";")
                f.write(str(i.blood_donor))
                f.write(";")
                f.write(str(i.loc_stat))
                f.write(";")
                process=', '.join(i.process_characteristic)
                f.write(process)
                f.write(";")
                f.write(str(i.skin_of))
                f.write(";")
                f.write(str(i.symptoms))
                f.write(";")
                f.write(str(i.dermographism1))
                f.write(";")
                f.write(str(i.dermographism2))
                f.write(";")
                f.write(str(i.mucous_membranes))
                f.write(";")
                f.write(str(i.mucous_membranes2))
                f.write(";")
                f.write(str(i.lymph))
                f.write(";")
                f.write(str(i.lymph_description))
                f.write(";")
                f.write(str(i.lymph_description1))
                f.write(";")
                f.write(str(i.lymph_description2))
                f.write(";")
                f.write(str(i.lymph_description4))
                f.write(";")
                f.write(str(i.lymph_description6))
                f.write(";")
                f.write(str(i.lymph_description5))
                f.write(";")
                f.write(str(i.hair_description))
                f.write(";")
                f.write(str(i.hair_description2))
                f.write(";")
                f.write(str(i.nails_of))
                f.write(";")
                f.write(str(i.nails_desc))
                f.write(";")
                f.write(str(i.additional_symp))
                f.write(";")
                f.write(str(i.scabies_comment))
                f.write(";")
                f.write(str(i.diagnosis_main))
                f.write(";")
                f.write(str(i.form))
                f.write(";")
                f.write(str(i.stage))
                f.write(";")
                f.write(str(i.code))
                f.write(";")
                f.write(str(i.diagnosis2))
                f.write(";")
                f.write(str(i.complication))
                f.write(";")
                f.write(str(i.treatment))
                f.write(";")
                f.write(str(i.treatment2))
                f.write(";")
                f.write(str(i.treatment3))
                f.write(";")
                f.write(str(i.treatment4))
                f.write(";")
                f.write(str(i.treatment5))
                f.write(";")
                f.write(str(i.treatment6))
                f.write(";")
                f.write(str(i.recomm))
                f.write(";")
                f.write(str(i.recomm2))
                f.write(";")
                f.write(str(i.recomm3))
                f.write(";")
                f.write(str(i.recomm4))
                f.write(";")
                f.write(str(i.recomm5))
                f.write(";")
                f.write(str(i.recomm6))
                f.write(";")
                f.write(str(i.comeback))
                f.write(";")
                f.write(str(i.doctor))
                f.write("\n")
            f.close()
    return

def on_termination():
    save_to_text()
    saved_for_later.clear()
    return

def launch():
    #read from text file of unfinished cards
    #load to the UI if any
    with open('unfinished_cards.txt', 'r', -1, "utf-8") as f:
        f1 = [line.rstrip('\n') for line in f]
    f.close()
    #print(os.stat('unfinished_cards.txt').st_size)
    #if os.stat('unfinished_cards.txt').st_size<=3:
    #    return
#    else:
    for i in f1:
        m = i.split(";")
        if len(m)==62:
            #create visit with read strings
            new_visit = Visit(m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11],
            m[12], m[13], m[14], m[15], m[16], m[17], m[18], m[19], m[20],
            m[21], m[22], m[23], m[24], m[25], m[26], m[27], m[28], m[29], m[30], m[31], m[32], m[33],
            m[34], m[35], m[36], m[37], m[38], m[39], m[40], m[41], m[42], m[43], m[44], m[45], m[46],
            m[47], m[48], m[49], m[50], m[51], m[52], m[53], m[54], m[55], m[56], m[57], m[58], m[59], m[60], m[61])
            saved_for_later.append(new_visit)
            id_taken.append(m[2])
        else:
            continue
    #f =  open('unfinished_cards.txt', 'w', -1, "utf-8").close()
    return


def save_for_later(last_name, first_name, visit_id, birthyear,
                        birthmonth,  birthday, visit_date,
                        visit_type, directed, complaints, sicktime, prev_treatment,
                        other_illness, diabetes, infect, allergy, drug_allergy,
                        heredity, medicaments, addictions, blood_donor, loc_stat,
                        process_characteristic, skin_of, symptoms, dermographism1, dermographism2,
                        mucous_membranes, mucous_membranes2, lymph, lymph_description,
                        lymph_description1, lymph_description2, lymph_description4,
                        lymph_description6, lymph_description5, hair_description,
                        hair_description2, nails_of, nails_desc, additional_symp,
                        tkvr, diagnosis_main, form, stage, code, diagnosis2,
                        complication, treatment, treatment2, treatment3, treatment4,
                        treatment5, treatment6, recomm, recomm2, recomm3,
                        recomm4, recomm5, recomm6, comeback, doctor):
    if visit_id ==None:
        new_id = generate_id()
        new_visit = Visit(last_name, first_name, new_id, birthyear,
    birthmonth,  birthday, visit_date,
                            visit_type, directed, complaints, sicktime, prev_treatment,
                            other_illness, diabetes, infect, allergy, drug_allergy,
                                heredity, medicaments, addictions, blood_donor, loc_stat,
                                    process_characteristic, skin_of, symptoms, dermographism1, dermographism2,
                mucous_membranes, mucous_membranes2, lymph, lymph_description,
                    lymph_description1, lymph_description2, lymph_description4,
                    lymph_description6, lymph_description5, hair_description,
                                                        hair_description2, nails_of, nails_desc, additional_symp,
                                                        tkvr, diagnosis_main, form, stage, code, diagnosis2,
                                                        complication, treatment, treatment2, treatment3, treatment4,
                                                        treatment5, treatment6, recomm, recomm2, recomm3,
                                                        recomm4, recomm5, recomm6, comeback, doctor)
        saved_for_later.append(new_visit)
    else:
        index = next(i for i, x in enumerate(saved_for_later) if x.visit_id == visit_id)
        saved_for_later.pop(index)
        replace_visit = Visit(last_name, first_name, visit_id, birthyear,
    birthmonth,  birthday, visit_date,
                            visit_type, directed, complaints, sicktime, prev_treatment,
                            other_illness, diabetes, infect, allergy, drug_allergy,
                                heredity, medicaments, addictions, blood_donor, loc_stat,
                                    process_characteristic, skin_of, symptoms, dermographism1, dermographism2,
                mucous_membranes, mucous_membranes2, lymph, lymph_description,
                    lymph_description1, lymph_description2, lymph_description4,
                    lymph_description6, lymph_description5, hair_description,
                                                        hair_description2, nails_of, nails_desc, additional_symp,
                                                        tkvr, diagnosis_main, form, stage, code, diagnosis2,
                                                        complication, treatment, treatment2, treatment3, treatment4,
                                                        treatment5, treatment6, recomm, recomm2, recomm3,
                                                        recomm4, recomm5, recomm6, comeback, doctor)
        saved_for_later.append(replace_visit)
    return

def delete_from_saved_for_later(visit_id):
    if visit_id!=None:
        index = next(i for i, x in enumerate(saved_for_later) if x.visit_id == visit_id)
        saved_for_later.pop(index)
        id_taken.remove(visit_id)
        save_to_text() #updates the textfile on the background replace for faster work
    return

#-- LISTS VALUES----
visit_types = {'впервые',  'повторный после лечения'}
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
diabetes_options = {"отрицает", "первого типа", "второго типа"}
years = []
for i in range(datetime.date.today().year - 120,  datetime.date.today().year+1):
    years.append(i)

months = []
for i in range(1,  13):
    months.append(i)

days = []
for i in range(1,  32):
    days.append(i)
'''
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

def delete_patient_db(search_by,  value):
    #execute(select from and delete)
    return

def clean_name(some_var):
    return ''.join(char for char in some_var if char.isalnum())'''
