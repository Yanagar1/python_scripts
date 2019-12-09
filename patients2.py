#----DATA INITIALIZER FILE-----
import sqlite3,  datetime, os
from tkinter import *
from tkcalendar import *
from tkinter import ttk, messagebox, filedialog
from fpdf import FPDF
from textwrap import *
import random
import atexit
from PIL import ImageTk,Image

saved_for_later = []
list_of_found_entries=[]



#determines the longest entry in the list and returns number to adjust window width
def find_longest(list):
    longest = 60 #min for neat output
    for i in range(len(list)):
        length_i = len(list[i].last_name)+len(list[i].first_name)+len(list[i].birthyear)+len(list[i].visit_date)+len(list[i].diagnosis_main)+len(list[i].code)
        if length_i >= longest:
            longest = length_i
    return longest

#------------------------DB FUNCTIONS-------------------------------------------

def create_connection():
    try:
        connection = sqlite3.connect("patients.db")
        return connection
    except Error as e:
        print(e)
    return None


#writes patient to any table
def add_patient_to_db(connection, table_name, last_name,first_name, birthyear,birthmonth,birthday,visit_date,
visit_type,directed,complaints,sicktime,prev_treatment,other_illness,diabetes,infect,
allergy,drug_allergy,heredity,medicaments,addictions,blood_donor,loc_stat,process,
skin_of,symptoms,dermographism1,dermographism2,mucous_membranes,mucous_membranes2,lymph,lymph_description,
lymph_description1,lymph_description2,lymph_description4,lymph_description6,lymph_description5,
hair_description,hair_description2,nails_of,nails_desc,additional_symp,scabies_comment,diagnosis_main,form,
stage,code,diagnosis2,complication,treatment,treatment2,treatment3,treatment4,treatment5,treatment6,recomm,
recomm2,recomm3,recomm4,recomm5,recomm6,comeback,doctor):
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO {}(Фамилия, Имя, Год_Рождения, Месяц_Рождения, День_Рождения, Дата_визита,
    Тип_визита,Направлен,Жалобы,Болен,Лечение_Самолечение,Сопутствующие_заболевания,Сахарный_диабет,Инфекционные_заболевания,
    Пищевая_аллергия,Лекарственная_непереносимость,Наследственность,препараты,Вредные_привычки,Донор,Локальный_статус,Характер_процесса,
    На_коже,Высыпания_представлены,Дермографизм1,Дермографизм2,Слизистые,Слизистые2,Лимфузлы,Лимфузлы0,
    Лимфузлы1,Лимфузлы2,Лимфузлы4,Лимфузлы6,Лимфузлы5,
    Оволосение,Волосы,Ногктевые_пластины,Ногктевые_пластины2,Доп_симптомы,чесотка_педикулез,Диагноз_основной,Форма,
    Стадия,Код_МКБ,Диагноз_сопутствующий,Осложнения,treatment,treatment2,treatment3,treatment4,treatment5,treatment6,recomm,
    recomm2,recomm3,recomm4,recomm5,recomm6,Повторная_явка,Врач)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""".format(table_name),
    (last_name,first_name, birthyear,birthmonth,birthday,visit_date,
    visit_type,directed,complaints,sicktime,prev_treatment,other_illness,diabetes,infect,
    allergy,drug_allergy,heredity,medicaments,addictions,blood_donor,loc_stat,process,
    skin_of,symptoms,dermographism1,dermographism2,mucous_membranes,mucous_membranes2,lymph,lymph_description,
    lymph_description1,lymph_description2,lymph_description4,lymph_description6,lymph_description5,
    hair_description,hair_description2,nails_of,nails_desc,additional_symp,scabies_comment,diagnosis_main,form,
    stage,code,diagnosis2,complication,treatment,treatment2,treatment3,treatment4,treatment5,treatment6,recomm,
    recomm2,recomm3,recomm4,recomm5,recomm6,comeback,doctor))
    connection.commit()
    cursor.close()
    return cursor.lastrowid


def overwrite_patient(connection, table_name, visit_id_in, last_name, first_name, birthyear,
                        birthmonth,  birthday, visit_date,
                        visit_type, directed, complaints, sicktime, prev_treatment,
                        other_illness, diabetes, infect, allergy, drug_allergy,
                        heredity, medicaments, addictions, blood_donor, loc_stat,
                        process, skin_of, symptoms, dermographism1, dermographism2,
                        mucous_membranes, mucous_membranes2, lymph, lymph_description,
                        lymph_description1, lymph_description2, lymph_description4,
                        lymph_description6, lymph_description5, hair_description,
                        hair_description2, nails_of, nails_desc, additional_symp,
                        scabies_comment, diagnosis_main, form, stage, code, diagnosis2,
                        complication, treatment, treatment2, treatment3, treatment4,
                        treatment5, treatment6, recomm, recomm2, recomm3,
                        recomm4, recomm5, recomm6, comeback, doctor):
    cursor = connection.cursor()
    cursor.execute("""UPDATE {} SET Фамилия = ?, Имя=?, Год_Рождения=?, Месяц_Рождения=?, День_Рождения=?, Дата_визита=?,
    Тип_визита=?,Направлен=?,Жалобы=?,Болен=?,Лечение_Самолечение=?,Сопутствующие_заболевания=?,Сахарный_диабет=?,Инфекционные_заболевания=?,
    Пищевая_аллергия=?,Лекарственная_непереносимость=?,Наследственность=?,препараты=?,Вредные_привычки=?,Донор=?,Локальный_статус=?,Характер_процесса=?,
    На_коже=?,Высыпания_представлены=?,Дермографизм1=?,Дермографизм2=?,Слизистые=?,Слизистые2=?,Лимфузлы=?,Лимфузлы0=?,
    Лимфузлы1=?,Лимфузлы2=?,Лимфузлы4=?,Лимфузлы6=?, Лимфузлы5=?,
    Оволосение=?,Волосы=?,Ногктевые_пластины=?,Ногктевые_пластины2=?,Доп_симптомы=?,чесотка_педикулез=?,Диагноз_основной=?,Форма=?,
    Стадия=?,Код_МКБ=?,Диагноз_сопутствующий=?,Осложнения=?,treatment=?,treatment2=?,treatment3=?,treatment4=?,treatment5=?,treatment6=?,recomm=?,
    recomm2=?,recomm3=?,recomm4=?,recomm5=?,recomm6=?,Повторная_явка=?,Врач=? WHERE id = ?""".format(table_name),
    (last_name,first_name, birthyear,birthmonth,birthday,visit_date,
    visit_type,directed,complaints,sicktime,prev_treatment,other_illness,diabetes,infect,
    allergy,drug_allergy,heredity,medicaments,addictions,blood_donor,loc_stat,process,
    skin_of,symptoms,dermographism1,dermographism2,mucous_membranes,mucous_membranes2,lymph,lymph_description,
    lymph_description1,lymph_description2,lymph_description4,lymph_description6,lymph_description5,
    hair_description,hair_description2,nails_of,nails_desc,additional_symp,scabies_comment,diagnosis_main,form,
    stage,code,diagnosis2,complication,treatment,treatment2,treatment3,treatment4,treatment5,treatment6,recomm,
    recomm2,recomm3,recomm4,recomm5,recomm6,comeback,doctor, visit_id_in))
    connection.commit()
    cursor.close()
    return


def delete_entry_from_db(connection, table_name, visit_id):
    #check if the id value is there
    cur = connection.cursor()
    cur.execute("DELETE FROM "+ table_name+ " WHERE id = ?", (visit_id,))
    connection.commit()
    cur.close()
    return


def search_args_to_command(connection, last_name, first_name, birthyear, visit_date, diagnosis, code):
    columnnames = ["Фамилия","Имя","Год_Рождения","Дата_визита","Диагноз_основной", "Код_МКБ"]
    columnnames1=[]
    args = [last_name, first_name, birthyear, visit_date, diagnosis, code]
    args1=[]
    for i in range(len(args)):
        if len(str(args[i]))!=0:
            args1.append(args[i])
            columnnames1.append(columnnames[i])
    if len(args1)==0:
        string = "SELECT * from visits"
    else:
        string = "SELECT * from visits WHERE "
        i = 0
        while i < (len(args1)-1):
            string = string + columnnames1[i]+ '='+"'" + str(args1[i])+"'"+ " AND "
            i+=1
        string = string + columnnames1[len(columnnames1)-1]+ '= '+"'"+ args1[len(args1)-1]+"'"
    return string


def look_db(connection, exec_string):
    cur = connection.cursor()
    cur.execute(exec_string)
    output = cur.fetchall()
    connection.commit()
    cur.close()
    return output


def on_termination(connection):
    connection.commit()
    connection.close()
    return


def convert_db_entry_to_class(m, from_table): #m is tuple from db
    for i in m:
        new_visit = Visit(from_table, m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11],
        m[12], m[13], m[14], m[15], m[16], m[17], m[18], m[19], m[20],
        m[21], m[22], m[23], m[24], m[25], m[26], m[27], m[28], m[29], m[30], m[31], m[32], m[33],
        m[34], m[35], m[36], m[37], m[38], m[39], m[40], m[41], m[42], m[43], m[44], m[45], m[46],
        m[47], m[48], m[49], m[50], m[51], m[52], m[53], m[54], m[55], m[56], m[57], m[58], m[59], m[60], m[61])
    return new_visit


def append_saved_for_later(connection):
    #read_from_db
    #load_to_class list
    saved_for_later.clear()
    cur = connection.cursor()
    cur.execute("""SELECT * FROM not_finished""")
    rows = cur.fetchall()
    for row in rows:
        visit = convert_db_entry_to_class(row, "not_finished")
        saved_for_later.append(visit)
    connection.commit()
    cur.close()
    return



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


class Visit:
    def __init__(self, from_table: str, visit_id: int, last_name: str, first_name: str, birthyear: str,
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

            self.from_table = from_table
            self.visit_id = visit_id
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


#creates new scrollable frame
def new_frame(frame, height, start_row, columnspan, canvas_height, scrollregion_w, scrollregion_h):
    #canvas, frame, window, scroll
    mycanvas = Canvas(frame, width=600, height=canvas_height, scrollregion=(0,0,scrollregion_w, scrollregion_h))
    mycanvas.grid(row=start_row, column=0, columnspan = columnspan, sticky="nsew")

    myframe1 = Frame(mycanvas, width=600, height=height, background = "#ffffff")
    myframe1.grid(row = start_row, column = 0, columnspan = columnspan)
    myframe1.rowconfigure(0, weight=1)
    myframe1.columnconfigure(0, weight=1)
    mycanvas.create_window(20, 5, width=600, height = height, window = myframe1, anchor = NW)

    canvbar = Scrollbar(frame, orient = "vertical", command = mycanvas.yview)
    canvbar.grid(row = start_row, column = columnspan+1, sticky="ns")
    mycanvas.configure(yscrollcommand = canvbar.set)
    mycanvas.configure(scrollregion=mycanvas.bbox("all"))
    return myframe1

def create_pdf(last_name, visit_date, visit_type, directed, complaints, sicktime, prev_treatment,
other_illness, diabetes, infect, allergy, drug_allergy,
heredity, medicaments, addictions, blood_donor, loc_stat,
process_characteristic, skin_entry, symptoms, dermographism1, dermographism2,
mucous_membranes, mucous_membranes2, lymph, lymph_description,
lymph_description1, lymph_description2, lymph_description4,
lymph_description6, lymph_description5, hair_description,
hair_description2, nails_of, nails_desc, additional_symp,
tkvr, diagnosis_main, form, stage, code, diagnosis2,
complication, treatment, treatment2, treatment3, treatment4,
treatment5, treatment6, recomm, recomm2, recomm3,
recomm4, recomm5, recomm6, comeback, doctor):


    def print_if_not_empty(entry_name, width, new_line):
        if len(entry_name)!=0:
            pdf.cell(width, 3, txt= entry_name, ln = new_line)
            return 1
        else:
            return 0
    folder_selected = filedialog.askdirectory()
    pdf = FPDF(orientation='P', unit='mm', format='A5')
    pdf.set_margins(7, 5)
    pdf.set_auto_page_break(True, margin = 104)
    pdf.add_page()
    pdf.add_font('times', '', 'times.ttf', uni = True)
    pdf.set_font('times', '', 7)

    pdf.cell(40, 3, txt="Дата обращения",  border = "B", ln=0)
    pdf.cell(40, 3, txt= visit_date, ln = 0)
    pdf.cell(40, 3, txt="ДД-001", ln=1)

    pdf.cell(40, 3, txt="На приёме", border = "B", ln=0)
    pdf.cell(0, 3, txt= visit_type, ln = 1)

    pdf.cell(40, 3, txt="Направлен",border = "B", ln=0)
    pdf.cell(0, 3, txt= directed, ln = 1)

    pdf.cell(40, 3, txt="Жалобы",border = "B", ln=0)
    pdf.multi_cell(0, 3, txt = complaints)

    pdf.cell(40, 3, txt="Болен",border = "B", ln=0)
    pdf.cell(0, 3, txt= sicktime, ln = 1)

    pdf.cell(40, 3, txt="Лечение/Самолечение",border = "B", ln=0)
    pdf.multi_cell(0, 3, txt = prev_treatment)

    pdf.cell(40, 3, txt="Сопутствующие заболевания", border = "B",ln=0)
    pdf.multi_cell(0, 3, txt =other_illness)

    pdf.cell(40, 3, txt="Сахарный диабет", border = "B",ln=0)
    pdf.cell(0, 3, txt= diabetes, ln = 1)

    pdf.cell(40, 3, txt="Инфекционные заболевания", border = "B")
    pdf.multi_cell(0, 3, txt= infect)

    pdf.cell(40, 3, txt="Пищевая аллергия", border = "B",ln=0)
    pdf.cell(0, 3, txt= allergy, ln = 1)

    pdf.cell(40, 3, txt="Лекарственная непереносимость",border = "B", ln=0)
    pdf.cell(0, 3, txt= drug_allergy, ln = 1)

    pdf.cell(40, 3, txt="Наследственность",border = "B", ln=0)
    pdf.cell(0, 3, txt= heredity, ln = 1)

    pdf.cell(40, 3, txt="Постоянно принимает препараты",border = "B", ln=0)
    pdf.cell(0, 3, txt= medicaments, ln = 1)

    pdf.cell(40, 3, txt="Вредные привычки", border = "B",ln=0)
    pdf.cell(0, 3, txt= addictions, ln = 1)

    pdf.cell(40, 3, txt="Донором крови",border = "B", ln=0)
    pdf.cell(0, 3, txt= blood_donor, ln = 1)

    pdf.cell(40, 3, txt="Локальный статус", border = "B",ln=0)
    pdf.multi_cell(0, 3, txt = loc_stat)

    pdf.cell(0, 3, txt="Кожный патологический процесс:", border = "B", ln=1, align="C")
    process=', '.join(process_characteristic)

    pdf.cell(40, 3, txt="Характер процесса", border = "B", ln=0)
    pdf.multi_cell(0, 3, txt = process)

    pdf.cell(40, 3, txt="На коже", border = "B", ln=0)
    pdf.cell(0, 3, txt= skin_entry, ln = 1)

    pdf.cell(40, 3, txt="Высыпания представлены", border = "B",ln=0)
    pdf.multi_cell(0, 3, txt = symptoms)

    pdf.cell(40, 3, txt="Дермографизм", border = "B",ln=0)
    pdf.cell(40, 3, txt = dermographism1, ln = 0)
    pdf.cell(0, 3, txt= dermographism2, ln = 1)

    pdf.cell(40, 3, txt="Слизистые оболочки",border = "B", ln=0)
    pdf.cell(54, 3, txt = mucous_membranes, ln = 0)
    pdf.cell(0, 3, txt= mucous_membranes2, ln = 1)

    pdf.cell(40, 3, txt="Лимфатические узлы", border = "B",ln=0)
    pdf.multi_cell(0, 3, txt = lymph)

    if len(lymph_description) or len(lymph_description6) or len(lymph_description5) or len(lymph_description4)!=0:
        pdf.cell(40, 3, txt = "", ln = 0)
        pdf.cell(25, 3, txt = lymph_description, ln = 0)
        pdf.cell(25, 3, txt = lymph_description6, ln = 0)
        pdf.cell(25, 3, txt = lymph_description5, ln = 0)
        pdf.cell(25, 3, txt = lymph_description4, ln = 1)

    if len(lymph_description1)!=0:
        pdf.cell(40, 3, txt = "", ln = 0)
        pdf.cell(0, 3, txt = lymph_description1, ln = 1)

    if len(lymph_description2)!=0:
        pdf.cell(40, 3, txt = "", ln = 0)
        pdf.cell(0, 3, txt = lymph_description2, ln = 1)

    pdf.cell(40, 3, txt="Оволосение по типу: ", border = "B",ln=0)
    pdf.cell(0, 3, txt= hair_description, ln = 1)

    pdf.cell(40, 3, txt="Волосы", border = "B",ln=0)
    pdf.multi_cell(0, 3, txt = hair_description2)

    pdf.cell(40, 3, txt="Ногтевые пластины", border = "B",ln=0)
    pdf.cell(30, 3, txt= nails_of, ln = 0)
    pdf.multi_cell(0, 3, txt =nails_desc)

    pdf.cell(40, 3, txt="Дополнительные симптомы", border = "B",ln=0)
    pdf.multi_cell(0, 3, txt = additional_symp)

    pdf.cell(40, 3, txt="На момент осм. чесотка и педикулёз", border = "B", ln=0)
    pdf.cell(0, 3, txt= tkvr, ln = 1)

    if pdf.page_no()==1:
        pdf.add_page()


    pdf.cell(40, 3, txt="Диагноз основной", border = "B",ln=0)
    pdf.multi_cell(0, 3, txt= diagnosis_main)

    pdf.cell(40, 3, txt="Форма",border = "B", ln=0)
    pdf.cell(0, 3, txt= form, ln = 1)

    pdf.cell(40, 3, txt="Стадия",border = "B", ln=0)
    pdf.cell(0, 3, txt= stage, ln = 1)

    pdf.cell(40, 3, txt="Код МКБ", border = "B",ln=0)
    pdf.cell(0, 3, txt= code, ln = 1)

    pdf.cell(40, 3, txt="Диагноз сопутствующий",border = "B", ln=0)
    pdf.multi_cell(0, 3, txt= diagnosis2)

    pdf.cell(40, 3, txt="Осложнения",border = "B", ln=0)
    pdf.multi_cell(0, 3, txt= complication)

    pdf.cell(0, 3, txt="План обследования", border = "B", ln=1, align="C")
    pdf.cell(0, 3, txt=treatment, ln = 1)
    pdf.cell(0, 3, txt= treatment2, ln = 1)
    print_if_not_empty(treatment3, 0, 1)
    print_if_not_empty(treatment4, 0, 1)
    print_if_not_empty(treatment4, 0, 1)
    print_if_not_empty(treatment6, 0, 1)

    pdf.cell(0, 3, txt="Рекомендации", border = "B",ln=1, align="C")
    pdf.cell(0, 3, txt= recomm, ln = 1)
    pdf.cell(0, 3, txt= recomm2, ln = 1)
    print_if_not_empty(recomm3, 0, 1)
    print_if_not_empty(recomm4, 0, 1)
    print_if_not_empty(recomm4, 0, 1)
    print_if_not_empty(recomm6, 0, 1)

    pdf.cell(40, 3, txt="Повторная явка", border = "B", ln=0)
    pdf.multi_cell(0, 3, txt= comeback)

    pdf.cell(40, 3, txt="Врач", border = "B", ln=0)
    pdf.cell(40, 3, txt= doctor, ln = 1)

    file_str = folder_selected+"/"+last_name
    i=0
    while os.path.exists(file_str)==True:
        file_str = file_str+"({})".format(str(i))
        i+=1
    pdf.output(file_str)
    messagebox.showinfo("ОК", "Файл был сохранен")
    return


#-- LISTS VALUES----
visit_types = {'впервые',  'повторный после лечения'}
donor = {'является',  'не является'}
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
values_for_prev_treatment = ['отрицает','с положительной динамикой', 'с отрицательной динамикой', 'без эффекта']
values_for_ll1 = ['не увеличены','увеличены до']
values_for_ll2 = ['симметрично','не симметрично']
values_for_ll6 = ['неспаянные','спаянные']
values_for_hair = ['без изменений', 'изменены']
parts = {'кистей', 'стоп', 'кистей и стоп'}
choices = {'не выявлены', 'выявлены'}

years = []
for i in range(datetime.date.today().year - 120,  datetime.date.today().year+1):
    years.append(i)

months = []
for i in range(1,  13):
    months.append(i)

days = []
for i in range(1,  32):
    days.append(i)

#------------------------OTHER DB FUNCTIONS-------------------------------------------

#input cleaner for injection attack
#def clean_name(some_var):
#    return ''.join(char for char in some_var if char.isalnum())'''
