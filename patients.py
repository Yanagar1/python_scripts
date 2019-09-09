#/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

#----INTERFACE FILE---WINDOWS
from patients2 import *

launch()

def mainwin():
    main_menu = Tk()
    main_menu.geometry("620x580")
    frame = Frame(main_menu, width=620, height=500, background = "snow")
    frame.place(x=0, y=60)
    #frame.grid(sticky='news')
    main_menu.winfo_toplevel().title("Мои Пациенты")
    #check connection for none
    connection = create_connection()


    def clear_frame():
        for widget in frame.winfo_children():
            widget.destroy()
        return

    def search(last_name, first_name, birthyear, birthmonth, birthday, visit_date, diagnosis_main, code):
        #analyze input and make command
        search_parameters =[last_name, first_name, birthyear, birthmonth, birthday, visit_date, diagnosis_main, code]
        search_parameters2=[]
        for i in search_parameters:
            if len(i)!=0:
                search_parameters2.append(i)
        print(search_parameters2)
        return
    '''    connection.execute(("""SELECT * FROM visits WHERE last_name = {} AND
                                                        first_name = {} AND
                                                        birthyear  = {} AND
                                                        birthmonth = {} AND
                                                        birthday = {} AND
                                                        visit_date  = {} AND
                                                        diagnosis_main = {} AND
                                                        code = {}""").format(last_name, first_name, birthyear, birthmonth, birthday,visit_date, diagnosis_main, code))
        connection.commit()'''


    #function to call as the main button is pressed (search database)
    #creates entries for search
    def call_search():
        clear_frame()
        name_label1 = Label(frame, text="Фамилия", background = "snow")
        name_label2 = Label(frame, text="Имя", background = "snow")
        birthdate_label = Label(frame, text="Дата Рождения", background = "snow")
        visit_date_label = Label(frame, text="Дата визита", background = "snow")
        diagnosis_label = Label(frame, text="Диагноз основной", background = "snow")
        code_label = Label(frame, text="Код МКБ", background = "snow")
        name_entry1 = Entry(frame, width = 30)
        name_entry2 = Entry(frame, width = 30)
        tkvar_y = IntVar(frame)
        tkvar_m = IntVar(frame)
        tkvar_d = IntVar(frame)
        tkvar_y = StringVar(frame)
        birthyear = OptionMenu(frame, tkvar_y, *years)
        tkvar_m = StringVar(frame)
        birthmonth = OptionMenu(frame, tkvar_m, *months)
        tkvar_d = StringVar(frame)
        birthday = OptionMenu(frame, tkvar_d, *days)
        visit_date = Entry(frame, width = 30)
        diagnosis = Entry(frame, width = 30)
        code = Entry(frame, width = 30)
        name_label1.grid(row=0, column = 0, sticky = W)
        name_entry1.grid(row=0, column = 1, columnspan=2)
        name_label2.grid(row=1, column = 0, sticky = W)
        name_entry2.grid(row=1, column = 1, columnspan=2)
        birthdate_label.grid(row = 2, column = 0, sticky = W)
        birthyear.grid(row=2, column =1,sticky = W)
        birthmonth.grid(row=2, column =1)
        birthday.grid(row=2, column =1,sticky = E)
        visit_date_label.grid(row=3, column = 0, sticky = W)
        visit_date.grid(row=3, column=1, columnspan=2)
        diagnosis_label.grid(row=4, column = 0, sticky = W)
        diagnosis.grid(row=4, column = 1, sticky="ew", columnspan=2)
        code_label.grid(row=5, column = 0, sticky = W)
        code.grid(row=5, column = 1, columnspan=2)    #search_form()

        search_button = Button(frame, text = "Поиск", fg = "green", background = "snow",
        command = lambda: search(name_entry1.get(), name_entry2.get(),
        tkvar_y.get(),tkvar_m.get(),tkvar_d.get(),
        visit_date.get(),diagnosis.get(),code.get())).grid(row=6, column = 1)
            #found entries in a table
            #each is selectable
            #if any is selected:
                            # button edit => call_form() save overwrite
                            # button delete from db

        return

    #saves Visit class object to the saved_for_later list
    #is called when save_for_later button is pressed
    def save_and_report(later_param, visit_id, last_name, first_name, birthyear,
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
        if check_input_none(last_name, visit_date) == 1:
            if later_param == 1:
                report_text = "Карта сохранена на потом!"
                table_name="not_finished"
            else:
                report_text ="Карта сохранена!"
                table_name = "visits"
                delete_from_saved_for_later(visit_id)
            add_patient_to_db(connection, table_name, last_name, first_name, birthyear,
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
            clear_frame()
            messagebox.showinfo("Ok", report_text)
            return
        else:
            messagebox.showerror("Проблема", "Нужна фамилия и дата визита, чтобы сохранить и не запутаться!")

#helper

    def create_pdf(visit_id, last_name, visit_date, visit_type, directed, complaints, sicktime, prev_treatment,
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
                pdf.cell(width, 4, txt= entry_name, ln = new_line)
                return 1
            else:
                return 0
        folder_selected = filedialog.askdirectory()
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.set_margins(7, 5)
        pdf.set_auto_page_break(True, margin = 150)
        pdf.add_page()
        pdf.add_font('DejaVu', '', 'DejaVuSerif.ttf', uni=True)
        pdf.set_font('DejaVu', '', 7)

        pdf.cell(50, 4, txt="Дата обращения",  border = "B", ln=0)
        pdf.cell(50, 4, txt= visit_date, ln = 0)
        pdf.cell(50, 4, txt="ДД-001", ln=1, align = "R")

        pdf.cell(50, 4, txt="На приёме", border = "B", ln=0)
        pdf.cell(0, 4, txt= visit_type, ln = 1)

        pdf.cell(50, 4, txt="Направлен",border = "B", ln=0)
        pdf.cell(0, 4, txt= directed, ln = 1)

        if len(complaints) ==0:
            new_line = 1
        else:
            new_line = 0
        pdf.cell(50, 4, txt="Жалобы",border = "B", ln=new_line)
        m = line_splitter(complaints)
        for i in range(len(m)):
            pdf.cell(0, 4, txt = m[i], ln = 1)

        pdf.cell(50, 4, txt="Болен",border = "B", ln=0)
        pdf.cell(0, 4, txt= sicktime, ln = 1)

        if len(prev_treatment) ==0:
            new_line = 1
        else:
            new_line = 0
        pdf.cell(50, 4, txt="Лечение/Самолечение",border = "B", ln=new_line)
        m = line_splitter(prev_treatment)
        for i in m:
            pdf.cell(0, 4, txt = i, ln = 1)


        pdf.cell(50, 4, txt="Сопутствующие заболевания", border = "B",ln=0)
        m = line_splitter(other_illness)
        for i in m:
            pdf.cell(0, 4, txt = i, ln = 1)

        pdf.cell(50, 4, txt="Сахарный диабет", border = "B",ln=0)
        pdf.cell(0, 4, txt= diabetes, ln = 1)

        pdf.cell(100, 4, txt="Инфекционные заболевания в т.ч. сифилис, ВИЧ, гепатит", border = "B",ln=0)
        pdf.cell(0, 4, txt= infect, ln = 1)

        pdf.cell(50, 4, txt="Пищевая аллергия", border = "B",ln=0)
        pdf.cell(0, 4, txt= allergy, ln = 1)

        pdf.cell(50, 4, txt="Лекарственная непереносимость",border = "B", ln=0)
        pdf.cell(0, 4, txt= drug_allergy, ln = 1)

        pdf.cell(50, 4, txt="Наследственность",border = "B", ln=0)
        pdf.cell(0, 4, txt= heredity, ln = 1)

        pdf.cell(50, 4, txt="Постоянно принимает препараты",border = "B", ln=0)
        pdf.cell(0, 4, txt= medicaments, ln = 1)

        pdf.cell(50, 4, txt="Вредные привычки", border = "B",ln=0)
        pdf.cell(0, 4, txt= addictions, ln = 1)

        pdf.cell(50, 4, txt="Донором крови",border = "B", ln=0)
        pdf.cell(0, 4, txt= blood_donor, ln = 1)

        if len(loc_stat) ==0:
            new_line = 1
        else:
            new_line = 0
        pdf.cell(50, 4, txt="Локальный статус", border = "B",ln=new_line)
        m = line_splitter(loc_stat)
        for i in m:
            pdf.cell(0, 4, txt = str(i), ln = 1)

        pdf.cell(0, 4, txt="Кожный патологический процесс:", border = "B", ln=1, align="C")
        process=', '.join(process_characteristic)
        if len(process)==0:
            new_line = 1
        else:
            new_line = 0
        pdf.cell(50, 4, txt="Характер процесса", border = "B", ln=new_line)

        m = line_splitter(process)
        for i in m:
            pdf.cell(0, 4, txt = i, ln = 1)

        pdf.cell(50, 4, txt="На коже", border = "B", ln=0)
        pdf.cell(0, 4, txt= skin_entry, ln = 1)

        if len(symptoms)==0:
            new_line = 1
        else:
            new_line = 0
        pdf.cell(50, 4, txt="Высыпания представлены", border = "B",ln=new_line)
        m = line_splitter(symptoms)
        for i in m:
            pdf.cell(0, 4, txt = i, ln = 1)

        pdf.cell(50, 4, txt="Дермографизм", border = "B",ln=0)
        pdf.cell(40, 4, txt = dermographism1, ln = 0)
        pdf.cell(0, 4, txt= dermographism2, ln = 1)

        pdf.cell(50, 4, txt="Слизистые оболочки",border = "B", ln=0)
        pdf.cell(45, 4, txt = mucous_membranes, ln = 0)
        pdf.cell(0, 4, txt= mucous_membranes2, ln = 1)

        if len(lymph)==0:
            new_line = 1
        else:
            new_line = 0
        pdf.cell(50, 4, txt="Лимфатические узлы", border = "B",ln=new_line)
        new_line =print_if_not_empty(lymph, (len(lymph)+5)*2, 0)
        new_line =print_if_not_empty(lymph_description, 0, new_line)
        new_line =print_if_not_empty(lymph_description1, (len(lymph)+5)*2, new_line)
        new_line =print_if_not_empty(lymph_description2, 0, new_line)
        print_if_not_empty(lymph_description4, 50, 0)
        print_if_not_empty(lymph_description6, 50, 0)
        print_if_not_empty(lymph_description4, 0, 1)

        pdf.cell(50, 4, txt="Оволосение по типу: ", border = "B",ln=0)
        pdf.cell(0, 4, txt= hair_description, ln = 1)

        if len(hair_description2) ==0:
            new_line = 1
        else:
            new_line = 0
        pdf.cell(50, 4, txt="Волосы", border = "B",ln=new_line)
        m = line_splitter(hair_description2)
        for i in m:
            pdf.cell(0, 4, txt = i, ln = 1)

        pdf.cell(50, 4, txt="Ногктевые пластины", border = "B",ln=0)
        pdf.cell(30, 4, txt= nails_of, ln = 0)
        m = line_splitter(nails_desc)
        for i in m:
            pdf.cell(0, 4, txt = i, ln = 1)

        if len(additional_symp) == 0:
            new_line = 1
        else:
            new_line = 0
        pdf.cell(50, 4, txt="Дополнительные симптомы", border = "B",ln=new_line)
        m = line_splitter(additional_symp)
        for i in m:
            pdf.cell(0, 4, txt = i, ln = 1)

        pdf.cell(57, 4, txt="На момент осмотра чесотка и педикулёз", border = "B",ln=0)
        pdf.cell(0, 4, txt= tkvr, ln = 1)

        pdf.cell(50, 4, txt="Диагноз основной", border = "B",ln=0)
        pdf.cell(0, 4, txt= diagnosis_main, ln = 1)

        pdf.cell(50, 4, txt="Форма",border = "B", ln=0)
        pdf.cell(0, 4, txt= form, ln = 1)

        pdf.cell(50, 4, txt="Стадия",border = "B", ln=0)
        pdf.cell(0, 4, txt= stage, ln = 1)

        pdf.cell(50, 4, txt="Код МКБ", border = "B",ln=0)
        pdf.cell(0, 4, txt= code, ln = 1)

        pdf.cell(50, 4, txt="Диагноз сопутствующий",border = "B", ln=0)
        pdf.cell(0, 4, txt= diagnosis2, ln = 1)

        pdf.cell(50, 4, txt="Осложнения",border = "B", ln=0)
        pdf.cell(0, 4, txt= complication, ln = 1)

        pdf.cell(0, 4, txt="План обследования", border = "B", ln=1, align="C")
        pdf.cell(0, 4, txt=treatment, ln = 1)
        pdf.cell(0, 4, txt= treatment2, ln = 1)
        print_if_not_empty(treatment3, 0, 1)
        print_if_not_empty(treatment4, 0, 1)
        print_if_not_empty(treatment5, 0, 1)
        print_if_not_empty(treatment6, 0, 1)

        pdf.cell(0, 4, txt="Рекомендации", border = "B",ln=1, align="C")
        pdf.cell(0, 4, txt= recomm, ln = 1)
        pdf.cell(0, 4, txt= recomm2, ln = 1)
        print_if_not_empty(recomm3, 0, 1)
        print_if_not_empty(recomm4, 0, 1)
        print_if_not_empty(recomm5, 0, 1)
        print_if_not_empty(recomm6, 0, 1)

        pdf.cell(60, 4, txt="Повторная явка", border = "B", ln=0)
        pdf.cell(0, 4, txt= comeback, ln = 1)

        pdf.cell(50, 4, txt="Врач", border = "B", ln=0)
        pdf.cell(50, 4, txt= doctor, ln = 1)

        file_str = folder_selected+"/"+last_name
        pdf.output(file_str)
        messagebox.showinfo("ОК", "Файл был сохранен")
        return
#sets defaults entries to the form: new patient or not
    def call_form(visit_id_in):
        clear_frame()
        myframe1 = new_frame(frame, 1250)
        #LABELS
        name_label1 = Label(myframe1, text="Фамилия", background = "snow")
        name_label2 = Label(myframe1, text="Имя", background = "snow")
        birthdate_label = Label(myframe1, text="Дата Рождения", background = "snow")
        visit_date_label = Label(myframe1, text="Дата визита", background = "snow")
        visit_type_label = Label(myframe1, text="Тип визита", background = "snow")
        directed_label = Label(myframe1, text = "Направлен", background = "snow")
        complaints_label = Label(myframe1, text = "Жалобы", background = "snow")
        sicktime = Label(myframe1, text="Болен", background = "snow")
        prev_treatment_label = Label(myframe1, text = "Лечение/Самолечение", background = "snow")
        other_illness_label = Label(myframe1, text = "Сопутствующие заболевания", background = "snow")
        diabetes_label = Label(myframe1, text = "Сахарный диабет", background = "snow")
        infect_label = Label(myframe1, text = "Инфекционные заболевания", background = "snow")
        allergy_label = Label(myframe1, text = "Пищевая аллергия", background = "snow")
        drug_allergy_label = Label(myframe1, text = "Лекарственная непереносимость", background = "snow")
        inher_label = Label(myframe1, text = "Наследственность", background = "snow")
        med_label = Label(myframe1, text = "Постоянно принимает препараты", background = "snow")
        addict_label = Label(myframe1, text ="Вредные привычки", background = "snow")
        blood_donor_label = Label(myframe1, text = "Донором крови", background = "snow")
        loc_stat_label = Label(myframe1, text = "Локальный статус", background = "snow")
        process_label = Label(myframe1, text = "Кожный патологический процесс", background = "snow")
        process_char_label = Label(myframe1, text = "Характер процесса", background = "snow")
        skin = Label(myframe1, text = "На коже", background = "snow")
        symptoms_label = Label(myframe1, text="Высыпания представлены", background = "snow")
        derm_label = Label(myframe1, text = "Дермографизм", background = "snow")
        surf_label = Label(myframe1, text = "Слизистые оболочки", background = "snow")
        lymph_label = Label(myframe1, text = "Лимфатические узлы", background = "snow")
        hair_label = Label(myframe1, text = "Оволосение по типу:", background = "snow")
        h_label = Label(myframe1, text = "Волосы", background = "snow")
        n_label = Label(myframe1, text = "Ногктевые пластины", background = "snow")
        add_symp_label = Label(myframe1, text = "Дополнительные симптомы", background = "snow")
        comm_label = Label(myframe1, text = "На момент осмотра чесотка и педикулез", background = "snow")
        diagnosis_label = Label(myframe1, text="Диагноз основной", background = "snow")
        form_label = Label(myframe1, text="Форма", background = "snow")
        stage_label = Label(myframe1, text="Стадия", background = "snow")
        code_label = Label(myframe1, text="Код МКБ", background = "snow")
        diagnosis2_label = Label(myframe1, text="Диагноз сопутствующий", background = "snow")
        complications_label = Label(myframe1, text="Осложнения", background = "snow")
        treatment_label = Label(myframe1, text="План обследования", background = "snow")
        recomm_label = Label(myframe1, text="Рекомендации", background = "snow")
        comeback_label = Label(myframe1, text="Повторная явка", background = "snow")
        doctor_label = Label(myframe1, text="Врач", background = "snow")
        name_entry1 = Entry(myframe1, width = 30)
        name_entry2 = Entry(myframe1, width = 30)
        tkvar_y = IntVar(myframe1)
        tkvar_m = IntVar(myframe1)
        tkvar_d = IntVar(myframe1)
        tkvar_y = StringVar(myframe1)
        birthyear = OptionMenu(myframe1, tkvar_y, *years)
        tkvar_m = StringVar(myframe1)
        birthmonth = OptionMenu(myframe1, tkvar_m, *months)
        tkvar_d = StringVar(myframe1)
        birthday = OptionMenu(myframe1, tkvar_d, *days)
        visit_date = Entry(myframe1, width = 30)
        tkvar_visit_type = StringVar(myframe1)
        visit_type = OptionMenu(myframe1, tkvar_visit_type, *visit_types)
        directed =Entry(myframe1, width = 30)
        complaints=Entry(myframe1, width = 30)
        sicktime_entry1 = Entry(myframe1, width = 30)
        values_for_prev_treatment = ['отрицает','с положительной динамикой', 'с отрицательной динамикой', 'без эффекта']
        other_illness = Entry(myframe1, width = 30)
        diabetes_var=StringVar(myframe1)
        diabetes = OptionMenu(myframe1, diabetes_var, *diabetes_options)
        infect = Entry(myframe1, width = 30)
        allergy = Entry(myframe1, width = 30)
        drug_allergy = Entry(myframe1, width = 30)
        inher = Entry(myframe1, width = 30)
        med = Entry(myframe1, width = 30)
        addict = Entry(myframe1, width = 30)
        tkvar_blood_donor = StringVar(myframe1)
        blood_donor = OptionMenu(myframe1, tkvar_blood_donor, *donor)
        loc_stat = Entry(myframe1, width = 30)
        scroll = Scrollbar(myframe1)
        process_char = Listbox(myframe1, selectmode = MULTIPLE, yscrollcommand = scroll.set, height = 3, width = 25)
        for item in process:
            process_char.insert(END, item)
        scroll.config(command = process_char.yview)
        def read_selected_items():
            selected_items = []
            for i in process_char.curselection():
                selected_items.append(process_char.get(i))
            return selected_items
        skin_entry = Entry(myframe1, width = 30)
        symptoms = Entry(myframe1, width = 30)
        tkvar_derm = StringVar(myframe1)
        dermm = OptionMenu(myframe1, tkvar_derm, *derm)
        tkvar_derm2 = StringVar(myframe1)
        dermm2 = OptionMenu(myframe1, tkvar_derm2, *derm2)
        tkvar_surf = StringVar(myframe1)
        surff = OptionMenu(myframe1, tkvar_surf, *surf)
        tkvar_surf2 = StringVar(myframe1)
        surff2 = OptionMenu(myframe1, tkvar_surf2, *surf2)
        lymph = Entry(myframe1, width = 30)
        tkvar_l3 = StringVar(myframe1)
        ll3 = OptionMenu(myframe1, tkvar_l3, *l3)
        values_for_ll1 = ['не увеличены','увеличены до']
        values_for_ll2 = ['симметрично','не симметрично']
        tkvar_l4 = StringVar(myframe1)
        ll4 = OptionMenu(myframe1, tkvar_l4, *l4)
        values_for_ll6 = ['неспаянные','спаянные']
        tkvar_l5 = StringVar(myframe1)
        ll5 = OptionMenu(myframe1, tkvar_l5, *l5)
        tkvar_l7 = StringVar(myframe1)
        ll7 = OptionMenu(myframe1, tkvar_l7, *l7)
        values_for_hair = ['без зменений', 'изменены']
        tkvar_nails = StringVar(myframe1)
        parts = {'кистей', 'стоп', 'кистей и стоп'}
        tkvarparts = OptionMenu(myframe1, tkvar_nails, *parts)
        nails = Entry(myframe1, width = 30)
        add_symp = Entry(myframe1, width = 30)
        tkvr = StringVar(myframe1)
        choices = {'не выявлены', 'выявлены'}
        var8 = OptionMenu(myframe1, tkvr, *choices)
        diagnosis = Entry(myframe1, width = 30)
        form = Entry(myframe1, width = 30)
        stage = Entry(myframe1, width = 30)
        code = Entry(myframe1, width = 30)
        diagnosis2 = Entry(myframe1, width = 30)
        complication = Entry(myframe1, width = 30)
        treatment = Entry(myframe1, width = 30)
        treatment2 = Entry(myframe1, width = 30)
        treatment3 = Entry(myframe1, width = 30)
        treatment4 = Entry(myframe1, width = 30)
        treatment5 = Entry(myframe1, width = 30)
        treatment6 = Entry(myframe1, width = 30)
        recomm = Entry(myframe1, width = 30)
        recomm2 = Entry(myframe1, width = 30)
        recomm3 = Entry(myframe1, width = 30)
        recomm4 = Entry(myframe1, width = 30)
        recomm5 = Entry(myframe1, width = 30)
        recomm6 = Entry(myframe1, width = 30)
        comeback = Entry(myframe1, width = 30)
        doctor = Entry(myframe1, width = 30)
        if visit_id_in==None:
            #set all variables to the new defaults
            #current date
            year=datetime.date.today().year
            month=datetime.date.today().month
            day=datetime.date.today().day
            text = "{}/{}/{}".format(day, month, year)
            visit_date.insert(0, text)
            directed.insert(0, "самостоятельно")
            sicktime_entry1.insert(0, "находится на лечении")
            prev_treatment = ttk.Combobox(myframe1, values = values_for_prev_treatment)
            other_illness.insert(0, "полностью не обследован")
            infect.insert(0,"отрицает")
            allergy.insert(0,"отрицает")
            drug_allergy.insert(0,"отрицает")
            inher.insert(0,"не отягощяна")
            med.insert(0,"отрицает")
            addict.insert(0,"отрицает")
            ll1 = ttk.Combobox(myframe1, values = ['не увеличены','увеличены до'])
            ll2 = ttk.Combobox(myframe1, values = ['симметрично','не симметрично'])
            ll6 = ttk.Combobox(myframe1, values = ['неспаянные','спаянные'])
            hair3 = ttk.Combobox(myframe1, values = ['без зменений', 'изменены'])
            nails.insert(0, "не изменены")
            treatment.insert(0, "1.")
            treatment2.insert(0, "2.")
            recomm.insert(0, "1. Режим")
            recomm2.insert(0, "2. Диета")
            doctor.insert(0, "Большева А. А.")
        else:
            #find the index of the needed visit by visit_id in saved for later
            visit_index = next(j for j, x in enumerate(saved_for_later) if x.visit_id == visit_id_in)
            #set to the existing values
            name_entry1.insert(0, saved_for_later[visit_index].last_name)
            name_entry2.insert(0, saved_for_later[visit_index].first_name)
            tkvar_y.set(saved_for_later[visit_index].birthyear)
            tkvar_m.set(saved_for_later[visit_index].birthmonth)
            tkvar_d.set(saved_for_later[visit_index].birthday)
            visit_date.insert(0, saved_for_later[visit_index].visit_date)
            tkvar_visit_type.set(saved_for_later[visit_index].visit_type)
            directed.insert(0, saved_for_later[visit_index].directed)
            complaints.insert(0, saved_for_later[visit_index].complaints)
            sicktime_entry1.insert(0, saved_for_later[visit_index].sicktime)
            a = saved_for_later[visit_index].prev_treatment
            #check if the value exists
            curr_ind = check_dupli(values_for_prev_treatment, a)
            prev_treatment = ttk.Combobox(myframe1, values = values_for_prev_treatment)
            prev_treatment.current(curr_ind)
            other_illness.insert(0, saved_for_later[visit_index].other_illness)
            diabetes_var.set(saved_for_later[visit_index].diabetes)
            infect.insert(0, saved_for_later[visit_index].infect)
            allergy.insert(0, saved_for_later[visit_index].allergy)
            drug_allergy.insert(0, saved_for_later[visit_index].drug_allergy)
            inher.insert(0, saved_for_later[visit_index].heredity)
            med.insert(0, saved_for_later[visit_index].medicaments)
            addict.insert(0, saved_for_later[visit_index].addictions)
            tkvar_blood_donor.set(saved_for_later[visit_index].blood_donor)
            loc_stat.insert(0, saved_for_later[visit_index].loc_stat)
            for i in saved_for_later[visit_index].process_characteristic:
                process_char.select_set(i)
            symptoms.insert(0, saved_for_later[visit_index].symptoms)
            tkvar_derm.set(saved_for_later[visit_index].dermographism1)
            tkvar_derm2.set(saved_for_later[visit_index].dermographism2)
            tkvar_surf.set(saved_for_later[visit_index].mucous_membranes)
            tkvar_surf2.set(saved_for_later[visit_index].mucous_membranes2)
            lymph.insert(0, saved_for_later[visit_index].lymph)
            tkvar_l3.set(saved_for_later[visit_index].lymph_description)
            a1 = saved_for_later[visit_index].lymph_description1
            current_index1 = check_dupli(values_for_ll1, a1)
            ll1 = ttk.Combobox(myframe1, values = values_for_ll1)
            ll1.current(current_index1)
            a2 = saved_for_later[visit_index].lymph_description2
            current_index2 = check_dupli(values_for_ll2, a2)
            ll2 = ttk.Combobox(myframe1, values = values_for_ll2)
            ll2.current(current_index2)
            tkvar_l4.set(saved_for_later[visit_index].lymph_description4)
            current_index6 = check_dupli(values_for_ll6, saved_for_later[visit_index].lymph_description6)
            ll6 = ttk.Combobox(myframe1, values = values_for_ll6)
            ll6.current(current_index6)
            tkvar_l5.set(saved_for_later[visit_index].lymph_description5)
            tkvar_l7.set(saved_for_later[visit_index].hair_description)
            current_index_h = check_dupli(values_for_hair, saved_for_later[visit_index].hair_description2)
            hair3 = ttk.Combobox(myframe1, values = values_for_hair)
            hair3.current(current_index_h)
            tkvar_nails.set(saved_for_later[visit_index].nails_of)
            nails.insert(0, saved_for_later[visit_index].nails_desc)
            add_symp.insert(0, saved_for_later[visit_index].additional_symp)
            tkvr.set(saved_for_later[visit_index].scabies_comment)
            diagnosis.insert(0, saved_for_later[visit_index].diagnosis_main)
            form.insert(0, saved_for_later[visit_index].form)
            stage.insert(0, saved_for_later[visit_index].stage)
            code.insert(0, saved_for_later[visit_index].code)
            diagnosis2.insert(0, saved_for_later[visit_index].diagnosis2)
            complication.insert(0, saved_for_later[visit_index].complication)

            treatment.insert(0, saved_for_later[visit_index].treatment)
            treatment2.insert(0, saved_for_later[visit_index].treatment2)
            treatment3.insert(0, saved_for_later[visit_index].treatment3)
            treatment4.insert(0, saved_for_later[visit_index].treatment4)
            treatment5.insert(0, saved_for_later[visit_index].treatment5)
            treatment6.insert(0, saved_for_later[visit_index].treatment6)

            recomm.insert(0, saved_for_later[visit_index].recomm)
            recomm2.insert(0, saved_for_later[visit_index].recomm2)
            recomm3.insert(0, saved_for_later[visit_index].recomm3)
            recomm4.insert(0, saved_for_later[visit_index].recomm4)
            recomm5.insert(0, saved_for_later[visit_index].recomm5)
            recomm6.insert(0, saved_for_later[visit_index].recomm6)

            comeback.insert(0, saved_for_later[visit_index].comeback)

            doctor.insert(0, saved_for_later[visit_index].doctor)
#GRID ALL
        name_label1.grid(row=0, column = 0, sticky = W)
        name_entry1.grid(row=0, column = 1)
        name_label2.grid(row=1, column = 0, sticky = W)
        name_entry2.grid(row=1, column = 1)
        birthdate_label.grid(row = 2, column = 0, sticky = W)
        birthyear.grid(row=2, column =1,sticky = W)
        birthmonth.grid(row=2, column =1)
        birthday.grid(row=2, column =1,sticky = E)
        visit_date_label.grid(row=3, column = 0, sticky = W)
        visit_date.grid(row=3, column=1)
        visit_type_label.grid(row=4, column = 0, sticky = W)
        visit_type.grid(row=4, column = 1, sticky="ew")

        directed_label.grid(row=5, column = 0, sticky = W)
        directed.grid(row=5, column = 1)
        complaints_label.grid(row=6, column = 0, sticky = W)
        complaints.grid(row=6, column = 1)
        sicktime.grid(row=7, column = 0, sticky = W)
        sicktime_entry1.grid(row=7, column = 1)
        prev_treatment_label.grid(row=8, column = 0, sticky = W)
        prev_treatment.grid(row=8, column = 1, sticky="ew")
        other_illness_label.grid(row=10, column = 0, sticky = W)
        other_illness.grid(row=10, column = 1)
        diabetes_label.grid(row=11, column = 0, sticky = W)
        diabetes.grid(row=11, column = 1, sticky="ew")
        infect_label.grid(row=12, column = 0, sticky = W)
        infect.grid(row=12, column = 1)
        allergy_label.grid(row=13, column = 0, sticky = W)
        allergy.grid(row=13, column = 1)

        drug_allergy_label.grid(row=14, column = 0, sticky = W)
        drug_allergy.grid(row=14, column = 1)
        inher_label.grid(row=15, column = 0, sticky = W)
        inher.grid(row=15, column = 1)
        med_label.grid(row=16, column = 0, sticky = W)
        med.grid(row=16, column = 1)
        addict_label.grid(row=17, column = 0, sticky = W)
        addict.grid(row=17, column = 1)

        blood_donor_label.grid(row=18, column = 0, sticky = W)
        blood_donor.grid(row=18, column = 1, sticky="ew")
        loc_stat_label.grid(row=19, column = 0, sticky = W)
        loc_stat.grid(row=19, column = 1)
        process_label.grid(row = 20, columnspan = 3)
        process_char_label.grid(row = 21, column = 0, sticky = W)
        scroll.grid(row = 21, column = 2, sticky = W)
        process_char.grid(row = 21, column = 1, sticky="ew")
        skin.grid(row = 22, column = 0, sticky="w")
        skin_entry.grid(row = 22, column = 1)

        symptoms_label.grid(row = 23, column = 0, sticky = W)
        symptoms.grid(row = 23, column = 1)
        derm_label.grid(row = 24, column = 0, sticky = W)
        dermm.grid(row=24, column = 1, sticky="ew")
        dermm2.grid(row=24, column = 2, sticky="ew")
        surf_label.grid(row = 25, column = 0, sticky = W)
        surff.grid(row=25, column = 1, sticky="ew")
        surff2.grid(row=25, column = 2, sticky="ew")

        lymph_label.grid(row = 26, column = 0, sticky = W)
        lymph.grid(row = 26, column = 1)
        ll3.grid(row=26, column = 2, sticky="ew")
        ll1.grid(row=27, column = 1, sticky="ew")
        ll2.grid(row=28, column = 1, sticky="ew")
        ll4.grid(row=27, column = 2, sticky="ew")
        ll6.grid(row=29, column = 1, sticky="ew")
        ll5.grid(row=28, column = 2, sticky="ew")

        hair_label.grid(row = 30, column = 0, sticky = W)
        ll7.grid(row=30, column = 1, sticky="ew")
        h_label.grid(row = 31, column = 0, sticky=W)
        hair3.grid(row = 31, column = 1, sticky="ew")
        n_label.grid(row = 32, column = 0, sticky = W)
        tkvarparts.grid(row = 32, column = 1, sticky="ew")
        nails.grid(row = 32, column = 2)#nails_desc

        add_symp_label.grid(row = 35, column = 0, sticky = W)
        add_symp.grid(row = 35, column = 1)
        comm_label.grid(row = 36, column = 0, columnspan=2, sticky = W)
        var8.grid(row = 36, column = 1, sticky="ew")

        diagnosis_label.grid(row = 37, column = 0, sticky = W)
        diagnosis.grid(row = 37, column = 1)
        form_label.grid(row = 38, column = 0, sticky = W)
        form.grid(row = 38, column = 1)
        stage_label.grid(row = 39, column = 0, sticky = W)
        stage.grid(row = 39, column = 1)
        code_label.grid(row = 40, column = 0, sticky = W)
        code.grid(row = 40, column = 1)
        diagnosis2_label.grid(row = 41, column = 0, sticky = W)
        diagnosis2.grid(row = 41, column = 1)
        complications_label.grid(row = 43, column = 0, sticky = W)
        complication.grid(row = 43, column = 1)

        treatment_label.grid(row=44, column = 1)
        treatment.grid(row = 45, column = 0)
        treatment2.grid(row = 45, column = 1)
        treatment3.grid(row = 45, column = 2)
        treatment4.grid(row = 46, column = 0)
        treatment5.grid(row = 46, column = 1)
        treatment6.grid(row = 46, column = 2)
        recomm_label.grid(row=47, column = 1)
        recomm.grid(row = 48, column = 0)
        recomm2.grid(row = 48, column = 1)
        recomm3.grid(row = 48, column = 2)
        recomm4.grid(row = 49, column = 0)
        recomm5.grid(row = 49, column = 1)
        recomm6.grid(row = 49, column = 2)
        comeback_label.grid(row=50, column = 0)
        comeback.grid(row = 50, column = 1)
        doctor_label.grid(row=51, column = 0)
        doctor.grid(row = 51, column = 1)

        save_button = Button(myframe1, text = "Сохранить на потом", fg = "green", background = "snow",
        command = lambda: save_and_report(1, visit_id_in, name_entry1.get(), name_entry2.get(),
        tkvar_y.get(),tkvar_m.get(),tkvar_d.get(),
        visit_date.get(),tkvar_visit_type.get(),directed.get(),
        complaints.get(),sicktime_entry1.get(),
        prev_treatment.get(),other_illness.get(),
        diabetes_var.get(),infect.get(),allergy.get(),
        drug_allergy.get(),inher.get(),med.get(),
        addict.get(),tkvar_blood_donor.get(),loc_stat.get(),
        read_selected_items(), skin_entry.get(),
        symptoms.get(),tkvar_derm.get(),tkvar_derm2.get(),
        tkvar_surf.get(),tkvar_surf2.get(),
        lymph.get(),tkvar_l3.get(),
        ll1.get(),ll2.get(),tkvar_l4.get(),ll6.get(),
        tkvar_l5.get(),tkvar_l7.get(),hair3.get(),tkvar_nails.get(), nails.get(),
        add_symp.get(),tkvr.get(),diagnosis.get(),
        form.get(),stage.get(),code.get(),
        diagnosis2.get(),complication.get(),treatment.get(), treatment2.get(),
        treatment3.get(),treatment4.get(),treatment5.get(),treatment6.get(),
        recomm.get(),recomm2.get(),recomm3.get(),
        recomm4.get(),recomm5.get(),recomm6.get(),
        comeback.get(),doctor.get())).grid(row=1, column = 2)


        print_pdf_button = Button(myframe1, text = "Создать PDF", fg = "green", background = "snow",
        command = lambda: create_pdf(visit_id_in, name_entry1.get(), visit_date.get(), tkvar_visit_type.get(),
        directed.get(), complaints.get(),sicktime_entry1.get(),
        prev_treatment.get(),other_illness.get(),
        diabetes_var.get(),infect.get(),allergy.get(),
        drug_allergy.get(),inher.get(),med.get(),
        addict.get(),tkvar_blood_donor.get(),loc_stat.get(),
        read_selected_items(), skin_entry.get(),
        symptoms.get(),tkvar_derm.get(),tkvar_derm2.get(),
        tkvar_surf.get(),tkvar_surf2.get(),
        lymph.get(),tkvar_l3.get(),
        ll1.get(),ll2.get(),tkvar_l4.get(),ll6.get(),
        tkvar_l5.get(),tkvar_l7.get(),hair3.get(),tkvar_nails.get(), nails.get(),
        add_symp.get(),tkvr.get(),diagnosis.get(),
        form.get(),stage.get(),code.get(),
        diagnosis2.get(),complication.get(),treatment.get(), treatment2.get(),
        treatment3.get(),treatment4.get(),treatment5.get(),treatment6.get(),
        recomm.get(),recomm2.get(),recomm3.get(),
        recomm4.get(),recomm5.get(),recomm6.get(),
        comeback.get(),doctor.get())).grid(row=52, column = 0, columnspan = 3)

        save_todb_button = Button(myframe1, text="Сохранить",fg = "green", background = "snow",
        command = lambda: save_and_report(0, visit_id_in, name_entry1.get(), name_entry2.get(),
        tkvar_y.get(),tkvar_m.get(),tkvar_d.get(),
        visit_date.get(),tkvar_visit_type.get(),directed.get(),
        complaints.get(),sicktime_entry1.get(),
        prev_treatment.get(),other_illness.get(),
        diabetes_var.get(),infect.get(),allergy.get(),
        drug_allergy.get(),inher.get(),med.get(),
        addict.get(),tkvar_blood_donor.get(),loc_stat.get(),
        read_selected_items(), skin_entry.get(),
        symptoms.get(),tkvar_derm.get(),tkvar_derm2.get(),
        tkvar_surf.get(),tkvar_surf2.get(),
        lymph.get(),tkvar_l3.get(),
        ll1.get(),ll2.get(),tkvar_l4.get(),ll6.get(),
        tkvar_l5.get(),tkvar_l7.get(),hair3.get(),tkvar_nails.get(), nails.get(),
        add_symp.get(),tkvr.get(),diagnosis.get(),
        form.get(),stage.get(),code.get(),
        diagnosis2.get(),complication.get(),treatment.get(), treatment2.get(),
        treatment3.get(),treatment4.get(),treatment5.get(),treatment6.get(),
        recomm.get(),recomm2.get(),recomm3.get(),
        recomm4.get(),recomm5.get(),recomm6.get(),
        comeback.get(),doctor.get()))
        save_todb_button.grid(row=53, column = 0, columnspan = 3 )
        return


    def call_saved_for_later():
        clear_frame()
        myframe1 = new_frame(frame, (len(saved_for_later)+1)*100)
        for i in range(len(saved_for_later)):
            name_button = Button(myframe1, text = saved_for_later[i].last_name, background = "snow", command= lambda i=i: call_form(saved_for_later[i].visit_id))
            name_button.pack()
        return

#------------------ MAIN MENU BUTTONS ------------

    todays_patients = Button(main_menu, text = "Незавершенные карты", fg = "green", background = "snow", width = 27, height = 3, command = call_saved_for_later)
    todays_patients.place(x=0, y=0)

    search_db = Button (main_menu, text = "Поиск", fg = "green",  background = "snow",  width = 27, height = 3, command = call_search)
    search_db.place(x=200, y = 0)

    add_patient = Button (main_menu, text = "Новый Пациент/Визит", fg = "green", background = "snow", width = 27, height = 3, command = lambda: call_form(None))
    add_patient.place(x = 400, y = 0)
            #write to database

    atexit.register(on_termination)
    main_menu.mainloop()


mainwin();
