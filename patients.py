#/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

#----INTERFACE FILE---WINDOWS
from patients2 import *



def mainwin():
    main_menu = Tk()
    main_menu.geometry("620x580")
    frame = Frame(main_menu, width=620, height=500, background = "#ffffff")
    frame.place(x=0, y=60)
    #frame.grid(sticky='news')
    main_menu.winfo_toplevel().title("Мои Пациенты")
    connection=create_connection()

#    image2 =Image.open("1.jpg")
#    img1 = PhotoImage(file = image2)
#    bg_label = Label(frame, image = img1)
#    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def clear_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()
        return

    #function to call as the main button is pressed (search database)
    #creates entries for search

    def print_output(connection, myframe1, last_name, first_name, birthyear, visit_date, diagnosis, code):
        #creates window for display scrollable
        #every entry on a new line
        clear_frame(myframe1)
        list_of_found_entries.clear()

        exec_string = search_args_to_command(connection, last_name, first_name, birthyear, visit_date, diagnosis, code)
        output = look_db(connection, exec_string)
        if len(output)!=0:
            report_label = Label(frame, text = "Найдено записей: %d" % (len(output)), background = "#ffffff")
            report_label.grid(row = 6, column = 0)

            for i in output:
                m = convert_db_entry_to_class(i, "visits")
                list_of_found_entries.append(m)

            determined_width = find_longest(list_of_found_entries)

            #create new scrollable
            #myframe1 = new_frame(frame, (len(list_of_found_entries)+1)*23, 8, 6, 350, 100, (len(list_of_found_entries)+1)*23)
            vari =  (len(list_of_found_entries)+1)*25
            mycanvas = Canvas(frame, width=600, height=350, scrollregion=(0,0,100, vari))
            mycanvas.grid(row=8, column=0, columnspan = 6, sticky="nsew")

            myframe1 = Frame(mycanvas, width=600, height=vari, background = "#ffffff")
            myframe1.grid(row = 8, column = 0, columnspan = 6)
            myframe1.rowconfigure(0, weight=1)
            myframe1.columnconfigure(0, weight=1)
            mycanvas.create_window(20, 5, width=determined_width*10, height = vari, window = myframe1, anchor = NW)

            canvbar = Scrollbar(frame, orient = "vertical", command = mycanvas.yview)
            canvbar.grid(row = 8, column = 7, sticky="ns")
            mycanvas.configure(yscrollcommand = canvbar.set)
            mycanvas.configure(scrollregion=mycanvas.bbox("all"))

            canvbar2 = Scrollbar(frame, orient = "horizontal", command = mycanvas.xview)
            canvbar2.grid(row = 9, column = 0, columnspan = 7, sticky="ew")
            mycanvas.configure(xscrollcommand = canvbar2.set)
            mycanvas.configure(scrollregion=mycanvas.bbox("all"))



            name_label1 = Label(myframe1, text="Фамилия", background = "lime green", fg = "white")
            name_label2 = Label(myframe1, text="Имя", background = "lime green", fg = "white")
            birthyear_label = Label(myframe1, text="Год Рождения", background = "lime green", fg = "white")
            visit_date_label = Label(myframe1, text="Дата визита", background = "lime green", fg = "white")
            diagnosis_label = Label(myframe1, text="Диагноз основной", background = "lime green", fg = "white")
            code_label = Label(myframe1, text="Код МКБ", background = "lime green", fg = "white")

            name_label1.grid(row=0, column = 1)
            name_label2.grid(row=0, column = 2)
            birthyear_label.grid(row = 0, column = 3)
            visit_date_label.grid(row=0, column = 4)
            diagnosis_label.grid(row = 0, column = 5)
            code_label.grid(row = 0, column = 6)


            row = 1
            for i in range(len(list_of_found_entries)):
                find_label0 = Label(myframe1, text = list_of_found_entries[i].last_name, background = "#ffffff")
                find_label1 = Label(myframe1, text = list_of_found_entries[i].first_name, background = "#ffffff")
                find_label2 = Label(myframe1, text = list_of_found_entries[i].birthyear, background = "#ffffff")
                find_label3 = Label(myframe1, text = list_of_found_entries[i].visit_date, background = "#ffffff")
                find_label4 = Label(myframe1, text = list_of_found_entries[i].diagnosis_main, background = "#ffffff")
                find_label5 = Label(myframe1, text = list_of_found_entries[i].code, background = "#ffffff")
                open_button = Button(myframe1, text = ">",background = "#ffffff", fg = "green", width = 1, command = lambda i=i: call_form(list_of_found_entries[i]) )

                find_label0.grid(row =row, column = 1)
                find_label1.grid(row = row, column = 2)
                find_label2.grid(row = row, column = 3)
                find_label3.grid(row = row, column = 4)
                find_label4.grid(row = row, column = 5)
                find_label5.grid(row = row, column = 6)
                open_button.grid(row = row, column = 0)

                myframe1.grid_columnconfigure(0, minsize=30)
                myframe1.grid_columnconfigure(1, minsize=83)
                myframe1.grid_columnconfigure(2, minsize=83)
                myframe1.grid_columnconfigure(3, minsize=83)
                myframe1.grid_columnconfigure(4, minsize=83)
                myframe1.grid_columnconfigure(5, minsize=83)
                myframe1.grid_columnconfigure(6, minsize=83)
            #    myframe1.grid_rowconfigure(row, minsize = 5)
                row+=1

        else:
            report_label = Label(frame, text = "Ничего не найдено", background = "#ffffff")
            report_label.grid(row = 6, column = 0)
        return



    def call_search_tab():
        clear_frame(frame)
        #ALL INPUT LABELS
        name_label1 = Label(frame, text="Фамилия", background = "#ffffff")
        name_label2 = Label(frame, text="Имя", background = "#ffffff")
        birthyear_label = Label(frame, text="Год Рожд.", background = "#ffffff")
        visit_date_label = Label(frame, text="Дата визита", background = "#ffffff")
        diagnosis_label = Label(frame, text="Диагноз основной", background = "#ffffff")
        code_label = Label(frame, text="Код МКБ", background = "#ffffff")

        #ALL ENTRIES, OPTIONS AND DEFAULTS
        name_entry1 = Entry(frame, width = 33)
        name_entry2 = Entry(frame, width = 33)
        birthyear = Entry(frame,  width = 33)
        visit_date = Entry(frame, width = 33)
        #visit_date.insert(0, "dd/mm/yyyy")

        diagnosis = Entry(frame, width = 33)
        code = Entry(frame, width = 33)

        #GRID ALL
        name_label1.grid(row=0, column = 0, sticky = W)
        name_entry1.grid(row=0, column = 1, columnspan=2)
        name_label2.grid(row=0, column = 3, sticky = W)
        name_entry2.grid(row=0, column = 4, columnspan=2)
        birthyear_label.grid(row = 1, column = 0, sticky = W)
        birthyear.grid(row=1, column =1, columnspan=2, sticky = W)
        visit_date_label.grid(row=1, column = 3, sticky = W)
        visit_date.grid(row=1, column=4, columnspan=2)

        diagnosis_label.grid(row = 3, column = 0, sticky = W)
        diagnosis.grid(row = 3, column = 1, columnspan=2)
        code_label.grid(row = 3, column = 3, sticky = W)
        code.grid(row = 3, column = 4, columnspan=2)

        myframe1 = new_frame(frame, 100, 8, 6, 350, 100, 100)
        #BUTTON Calls search_db function
        search_button = Button(frame, text = "Поиск", fg = "green", background = "#ffffff",
        command = lambda: print_output(connection, myframe1, name_entry1.get().strip().strip(), name_entry2.get().strip().strip(), birthyear.get().strip().strip(),
        visit_date.get().strip().strip(), diagnosis.get().strip().strip(), code.get().strip().strip())).grid(row=4, column = 0, rowspan =2, columnspan = 6)
        return


    #saves Visit class object to the saved_for_later list
    #is called when save_for_later button is pressed
    def save_and_report(table_name, visit_id_in, from_table, last_name, first_name, birthyear,
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
            report_text = "Карта сохранена!"
            process=', '.join(process_characteristic)
            if visit_id_in == None or from_table!=table_name:
                add_patient_to_db(connection, table_name, last_name, first_name, birthyear,
                                        birthmonth,  birthday, visit_date,
                                        visit_type, directed, complaints, sicktime, prev_treatment,
                                        other_illness, diabetes, infect, allergy, drug_allergy,
                                        heredity, medicaments, addictions, blood_donor, loc_stat,
                                        process, skin_of, symptoms, dermographism1, dermographism2,
                                        mucous_membranes, mucous_membranes2, lymph, lymph_description,
                                        lymph_description1, lymph_description2, lymph_description4,
                                        lymph_description6, lymph_description5, hair_description,
                                        hair_description2, nails_of, nails_desc, additional_symp,
                                        tkvr, diagnosis_main, form, stage, code, diagnosis2,
                                        complication, treatment, treatment2, treatment3, treatment4,
                                        treatment5, treatment6, recomm, recomm2, recomm3,
                                        recomm4, recomm5, recomm6, comeback, doctor)
                delete_and_clear(connection, "not_finished", visit_id_in)
            else:
                overwrite_patient(connection, table_name, visit_id_in, last_name, first_name, birthyear,
                                        birthmonth,  birthday, visit_date,
                                        visit_type, directed, complaints, sicktime, prev_treatment,
                                        other_illness, diabetes, infect, allergy, drug_allergy,
                                        heredity, medicaments, addictions, blood_donor, loc_stat,
                                        process, skin_of, symptoms, dermographism1, dermographism2,
                                        mucous_membranes, mucous_membranes2, lymph, lymph_description,
                                        lymph_description1, lymph_description2, lymph_description4,
                                        lymph_description6, lymph_description5, hair_description,
                                        hair_description2, nails_of, nails_desc, additional_symp,
                                        tkvr, diagnosis_main, form, stage, code, diagnosis2,
                                        complication, treatment, treatment2, treatment3, treatment4,
                                        treatment5, treatment6, recomm, recomm2, recomm3,
                                        recomm4, recomm5, recomm6, comeback, doctor)
            clear_frame(frame)
            messagebox.showinfo("Ok", report_text)
        else:
            messagebox.showerror("Проблема", "Нужна фамилия и дата визита, чтобы сохранить и не запутаться!")
        return


    def create_and_report_pdf(visit_id, last_name, visit_date, visit_type, directed, complaints, sicktime, prev_treatment,
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

        create_pdf(visit_id, last_name, visit_date, visit_type, directed, complaints, sicktime, prev_treatment,
        other_illness, diabetes, infect, allergy, drug_allergy,
        heredity, medicaments, addictions, blood_donor, loc_stat,
        process, skin_entry, symptoms, dermographism1, dermographism2,
        mucous_membranes, mucous_membranes2, lymph, lymph_description,
        lymph_description1, lymph_description2, lymph_description4,
        lymph_description6, lymph_description5, hair_description,
        hair_description2, nails_of, nails_desc, additional_symp,
        tkvr, diagnosis_main, form, stage, code, diagnosis2,
        complication, treatment, treatment2, treatment3, treatment4,
        treatment5, treatment6, recomm, recomm2, recomm3,
        recomm4, recomm5, recomm6, comeback, doctor)
        return

    def delete_and_clear(connection, table_name, visit_id_in):
        delete_entry_from_db(connection, table_name, visit_id_in)
        clear_frame(frame)
        return


#sets defaults entries to the form: new patient or not
    def call_form(visit_instance):
        clear_frame(frame)
        myframe1 = new_frame(frame, 1230, 0, 1, 500, 680, 500)
            #LABELS
        name_label1 = Label(myframe1, text="Фамилия", background = "#ffffff")
        name_label2 = Label(myframe1, text="Имя", background = "#ffffff")
        birthdate_label = Label(myframe1, text="Дата Рождения", background = "#ffffff")
        visit_date_label = Label(myframe1, text="Дата визита", background = "#ffffff")
        visit_type_label = Label(myframe1, text="Тип визита", background = "#ffffff")
        directed_label = Label(myframe1, text = "Направлен", background = "#ffffff")
        complaints_label = Label(myframe1, text = "Жалобы", background = "#ffffff")
        sicktime = Label(myframe1, text="Болен", background = "#ffffff")
        prev_treatment_label = Label(myframe1, text = "Лечение/Самолечение", background = "#ffffff")
        other_illness_label = Label(myframe1, text = "Сопутствующие заболевания", background = "#ffffff")
        diabetes_label = Label(myframe1, text = "Сахарный диабет", background = "#ffffff")
        infect_label = Label(myframe1, text = "Инфекционные заболевания", background = "#ffffff")
        allergy_label = Label(myframe1, text = "Пищевая аллергия", background = "#ffffff")
        drug_allergy_label = Label(myframe1, text = "Лекарственная непереносимость", background = "#ffffff")
        inher_label = Label(myframe1, text = "Наследственность", background = "#ffffff")
        med_label = Label(myframe1, text = "Постоянно принимает препараты", background = "#ffffff")
        addict_label = Label(myframe1, text ="Вредные привычки", background = "#ffffff")
        blood_donor_label = Label(myframe1, text = "Донором крови", background = "#ffffff")
        loc_stat_label = Label(myframe1, text = "Локальный статус", background = "#ffffff")
        process_label = Label(myframe1, text = "Кожный патологический процесс", background = "#fffafd")
        process_char_label = Label(myframe1, text = "Характер процесса", background = "#ffffff")
        skin = Label(myframe1, text = "На коже", background = "#ffffff")
        symptoms_label = Label(myframe1, text="Высыпания представлены", background = "#ffffff")
        derm_label = Label(myframe1, text = "Дермографизм", background = "#ffffff")
        surf_label = Label(myframe1, text = "Слизистые оболочки", background = "#ffffff")
        lymph_label = Label(myframe1, text = "Лимфатические узлы", background = "#ffffff")
        hair_label = Label(myframe1, text = "Оволосение по типу:", background = "#ffffff")
        h_label = Label(myframe1, text = "Волосы", background = "#ffffff")
        n_label = Label(myframe1, text = "Ногтевые пластины", background = "#ffffff")
        add_symp_label = Label(myframe1, text = "Дополнительные симптомы", background = "#ffffff")
        comm_label = Label(myframe1, text = "На момент осм. чесотка и педикулез", background = "#ffffff")
        diagnosis_label = Label(myframe1, text="Диагноз основной", background = "#ffffff")
        form_label = Label(myframe1, text="Форма", background = "#ffffff")
        stage_label = Label(myframe1, text="Стадия", background = "#ffffff")
        code_label = Label(myframe1, text="Код МКБ", background = "#ffffff")
        diagnosis2_label = Label(myframe1, text="Диагноз сопутствующий", background = "#ffffff")
        complications_label = Label(myframe1, text="Осложнения", background = "#ffffff")
        treatment_label = Label(myframe1, text="План обследования", background = "#ffffff")
        recomm_label = Label(myframe1, text="Рекомендации", background = "#ffffff")
        comeback_label = Label(myframe1, text="Повторная явка", background = "#ffffff")
        doctor_label = Label(myframe1, text="Врач", background = "#ffffff")
        name_entry1 = Entry(myframe1, width = 30)
        name_entry2 = Entry(myframe1, width = 30)
        tkvar_y = IntVar(myframe1)
        tkvar_m = IntVar(myframe1)
        tkvar_d = IntVar(myframe1)
        tkvar_y = StringVar(myframe1)
        birthyear = OptionMenu(myframe1, tkvar_y, *years)
        birthyear.config(bg = "#ffffff")
        tkvar_m = StringVar(myframe1)
        birthmonth = OptionMenu(myframe1, tkvar_m, *months)
        birthmonth.config(bg = "#ffffff")
        tkvar_d = StringVar(myframe1)
        birthday = OptionMenu(myframe1, tkvar_d, *days)
        birthday.config(bg = "#ffffff")
        visit_date = Entry(myframe1, width = 30)
        tkvar_visit_type = StringVar(myframe1)
        visit_type = OptionMenu(myframe1, tkvar_visit_type, *visit_types)
        visit_type.config(bg = "#ffffff")
        directed =Entry(myframe1, width = 30)
        complaints=Entry(myframe1, width = 30)
        sicktime_entry1 = Entry(myframe1, width = 30)
        other_illness = Entry(myframe1, width = 30)
        diabetes_var=StringVar(myframe1)
        diabetes = OptionMenu(myframe1, diabetes_var, *diabetes_options)
        diabetes.config(bg = "#ffffff")
        infect = Entry(myframe1, width = 30)
        allergy = Entry(myframe1, width = 30)
        drug_allergy = Entry(myframe1, width = 30)
        inher = Entry(myframe1, width = 30)
        med = Entry(myframe1, width = 30)
        addict = Entry(myframe1, width = 30)
        tkvar_blood_donor = StringVar(myframe1)
        blood_donor = OptionMenu(myframe1, tkvar_blood_donor, *donor)
        blood_donor.config(bg = "#ffffff")
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
        dermm.config(bg = "#ffffff")
        tkvar_derm2 = StringVar(myframe1)
        dermm2 = OptionMenu(myframe1, tkvar_derm2, *derm2)
        dermm2.config(bg = "#ffffff")
        tkvar_surf = StringVar(myframe1)
        surff = OptionMenu(myframe1, tkvar_surf, *surf)
        surff.config(bg = "#ffffff")
        tkvar_surf2 = StringVar(myframe1)
        surff2 = OptionMenu(myframe1, tkvar_surf2, *surf2)
        surff2.config(bg = "#ffffff")
        lymph = Entry(myframe1, width = 30)
        tkvar_l3 = StringVar(myframe1)
        ll3 = OptionMenu(myframe1, tkvar_l3, *l3)
        ll3.config(bg = "#ffffff")
        tkvar_l4 = StringVar(myframe1)
        ll4 = OptionMenu(myframe1, tkvar_l4, *l4)
        ll4.config(bg = "#ffffff")
        tkvar_l5 = StringVar(myframe1)
        ll5 = OptionMenu(myframe1, tkvar_l5, *l5)
        ll5.config(bg = "#ffffff")
        tkvar_l7 = StringVar(myframe1)
        ll7 = OptionMenu(myframe1, tkvar_l7, *l7)
        ll7.config(bg = "#ffffff")

        tkvar_nails = StringVar(myframe1)
        tkvarparts = OptionMenu(myframe1, tkvar_nails, *parts)
        tkvarparts.config(bg = "#ffffff")
        nails = Entry(myframe1, width = 30)
        add_symp = Entry(myframe1, width = 30)
        tkvr = StringVar(myframe1)
        var8 = OptionMenu(myframe1, tkvr, *choices)
        var8.config(bg = "#ffffff")
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

        if visit_instance==None:
            #set all variables to the new defaults
            #current date
            visit_id_in = None
            from_table = None

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
            inher.insert(0,"не отягощена")
            med.insert(0,"отрицает")
            addict.insert(0,"отрицает")
            ll1 = ttk.Combobox(myframe1, values = values_for_ll1)
            ll2 = ttk.Combobox(myframe1, values = values_for_ll2)
            ll6 = ttk.Combobox(myframe1, values = values_for_ll6)
            hair3 = ttk.Combobox(myframe1, values = values_for_hair)
            nails.insert(0, "не изменены")
            treatment.insert(0, "1.")
            treatment2.insert(0, "2.")
            recomm.insert(0, "1. Режим")
            recomm2.insert(0, "2. Диета")
            doctor.insert(0, "Большева А. А.")
        else:
            visit_id_in = visit_instance.visit_id
            from_table = visit_instance.from_table
            #set to the existing values
            name_entry1.insert(0, visit_instance.last_name)
            name_entry2.insert(0, visit_instance.first_name)
            tkvar_y.set(visit_instance.birthyear)
            tkvar_m.set(visit_instance.birthmonth)
            tkvar_d.set(visit_instance.birthday)
            visit_date.insert(0, visit_instance.visit_date)
            tkvar_visit_type.set(visit_instance.visit_type)
            directed.insert(0, visit_instance.directed)
            complaints.insert(0, visit_instance.complaints)
            sicktime_entry1.insert(0, visit_instance.sicktime)
            a = visit_instance.prev_treatment
            #check if the value exists
            curr_ind = check_dupli(values_for_prev_treatment, a)
            prev_treatment = ttk.Combobox(myframe1, values = values_for_prev_treatment)
            prev_treatment.current(curr_ind)
            other_illness.insert(0, visit_instance.other_illness)
            diabetes_var.set(visit_instance.diabetes)
            infect.insert(0, visit_instance.infect)
            allergy.insert(0, visit_instance.allergy)
            drug_allergy.insert(0, visit_instance.drug_allergy)
            inher.insert(0, visit_instance.heredity)
            med.insert(0, visit_instance.medicaments)
            addict.insert(0, visit_instance.addictions)
            tkvar_blood_donor.set(visit_instance.blood_donor)
            loc_stat.insert(0, visit_instance.loc_stat)

            list_var = visit_instance.process_characteristic.split(", ")
            for i in range(len(process)):
                if  process[i] in list_var:
                    process_char.select_set(i)

            symptoms.insert(0, visit_instance.symptoms)
            tkvar_derm.set(visit_instance.dermographism1)
            tkvar_derm2.set(visit_instance.dermographism2)
            tkvar_surf.set(visit_instance.mucous_membranes)
            tkvar_surf2.set(visit_instance.mucous_membranes2)
            lymph.insert(0, visit_instance.lymph)
            tkvar_l3.set(visit_instance.lymph_description)
            a1 = visit_instance.lymph_description1
            current_index1 = check_dupli(values_for_ll1, a1)
            ll1 = ttk.Combobox(myframe1, values = values_for_ll1)
            ll1.current(current_index1)
            a2 = visit_instance.lymph_description2
            current_index2 = check_dupli(values_for_ll2, a2)
            ll2 = ttk.Combobox(myframe1, values = values_for_ll2)
            ll2.current(current_index2)
            tkvar_l4.set(visit_instance.lymph_description4)
            current_index6 = check_dupli(values_for_ll6, visit_instance.lymph_description6)
            ll6 = ttk.Combobox(myframe1, values = values_for_ll6)
            ll6.current(current_index6)
            tkvar_l5.set(visit_instance.lymph_description5)
            tkvar_l7.set(visit_instance.hair_description)
            current_index_h = check_dupli(values_for_hair, visit_instance.hair_description2)
            hair3 = ttk.Combobox(myframe1, values = values_for_hair)
            hair3.current(current_index_h)
            tkvar_nails.set(visit_instance.nails_of)
            nails.insert(0, visit_instance.nails_desc)
            add_symp.insert(0, visit_instance.additional_symp)
            tkvr.set(visit_instance.scabies_comment)
            diagnosis.insert(0, visit_instance.diagnosis_main)
            form.insert(0, visit_instance.form)
            stage.insert(0, visit_instance.stage)
            code.insert(0, visit_instance.code)
            diagnosis2.insert(0, visit_instance.diagnosis2)
            complication.insert(0, visit_instance.complication)

            treatment.insert(0, visit_instance.treatment)
            treatment2.insert(0, visit_instance.treatment2)
            treatment3.insert(0, visit_instance.treatment3)
            treatment4.insert(0, visit_instance.treatment4)
            treatment5.insert(0, visit_instance.treatment5)
            treatment6.insert(0, visit_instance.treatment6)

            recomm.insert(0, visit_instance.recomm)
            recomm2.insert(0, visit_instance.recomm2)
            recomm3.insert(0, visit_instance.recomm3)
            recomm4.insert(0, visit_instance.recomm4)
            recomm5.insert(0, visit_instance.recomm5)
            recomm6.insert(0, visit_instance.recomm6)

            comeback.insert(0, visit_instance.comeback)

            doctor.insert(0, visit_instance.doctor)
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

#BUTTON CONTROL

        #conditional Buttons

        if from_table != "visits":
            save_button = Button(myframe1, text = "Сохранить на потом", fg = "green", background = "#fcddcf",
            command = lambda: save_and_report("not_finished", visit_id_in, from_table, name_entry1.get().strip().strip(), name_entry2.get().strip().strip(),
            tkvar_y.get().strip().strip(),tkvar_m.get().strip(),tkvar_d.get().strip(),
            visit_date.get().strip(),tkvar_visit_type.get().strip(),directed.get().strip(),
            complaints.get().strip(),sicktime_entry1.get().strip(),
            prev_treatment.get().strip(),other_illness.get().strip(),
            diabetes_var.get().strip(),infect.get().strip(),allergy.get().strip(),
            drug_allergy.get().strip(),inher.get().strip(),med.get().strip(),
            addict.get().strip(),tkvar_blood_donor.get().strip(),loc_stat.get().strip(),
            read_selected_items(), skin_entry.get().strip(),
            symptoms.get().strip(),tkvar_derm.get().strip(),tkvar_derm2.get().strip(),
            tkvar_surf.get().strip(),tkvar_surf2.get().strip(),
            lymph.get().strip(),tkvar_l3.get().strip(),
            ll1.get().strip(),ll2.get().strip(),tkvar_l4.get().strip(),ll6.get().strip(),
            tkvar_l5.get().strip(),tkvar_l7.get().strip(),hair3.get().strip(),tkvar_nails.get().strip(), nails.get().strip(),
            add_symp.get().strip(),tkvr.get().strip(),diagnosis.get().strip(),
            form.get().strip(),stage.get().strip(),code.get().strip(),
            diagnosis2.get().strip(),complication.get().strip(),treatment.get().strip(), treatment2.get().strip(),
            treatment3.get().strip(),treatment4.get().strip(),treatment5.get().strip(),treatment6.get().strip(),
            recomm.get().strip(),recomm2.get().strip(),recomm3.get().strip(),
            recomm4.get().strip(),recomm5.get().strip(),recomm6.get().strip(),
            comeback.get().strip(),doctor.get().strip())).grid(row=1, column = 2)

        if from_table == "visits":
            save_as_new_button = Button(myframe1, text = "Сохранить как новую", fg = "green", background = "#fcddcf",
            command = lambda: save_and_report(from_table, None, from_table, name_entry1.get().strip().strip(), name_entry2.get().strip().strip(),
            tkvar_y.get().strip().strip(),tkvar_m.get().strip(),tkvar_d.get().strip(),
            visit_date.get().strip(),tkvar_visit_type.get().strip(),directed.get().strip(),
            complaints.get().strip(),sicktime_entry1.get().strip(),
            prev_treatment.get().strip(),other_illness.get().strip(),
            diabetes_var.get().strip(),infect.get().strip(),allergy.get().strip(),
            drug_allergy.get().strip(),inher.get().strip(),med.get().strip(),
            addict.get().strip(),tkvar_blood_donor.get().strip(),loc_stat.get().strip(),
            read_selected_items(), skin_entry.get().strip(),
            symptoms.get().strip(),tkvar_derm.get().strip(),tkvar_derm2.get().strip(),
            tkvar_surf.get().strip(),tkvar_surf2.get().strip(),
            lymph.get().strip(),tkvar_l3.get().strip(),
            ll1.get().strip(),ll2.get().strip(),tkvar_l4.get().strip(),ll6.get().strip(),
            tkvar_l5.get().strip(),tkvar_l7.get().strip(),hair3.get().strip(),tkvar_nails.get().strip(), nails.get().strip(),
            add_symp.get().strip(),tkvr.get().strip(),diagnosis.get().strip(),
            form.get().strip(),stage.get().strip(),code.get().strip(),
            diagnosis2.get().strip(),complication.get().strip(),treatment.get().strip(), treatment2.get().strip(),
            treatment3.get().strip(),treatment4.get().strip(),treatment5.get().strip(),treatment6.get().strip(),
            recomm.get().strip(),recomm2.get().strip(),recomm3.get().strip(),
            recomm4.get().strip(),recomm5.get().strip(),recomm6.get().strip(),
            comeback.get().strip(),doctor.get().strip())).grid(row=1, column = 2)

        if from_table != None:
            delete_button = Button(myframe1, text = "Удалить картy", fg = "red", background = "#ffffff", command = lambda: delete_and_clear(connection, from_table, visit_instance.visit_id))
            delete_button.grid(row = 2, column = 2)


        #ALWAYS BUTTONS
        print_pdf_button = Button(myframe1, text = "Создать PDF", fg = "green", background = "#fcddcf", width = 20,
        command = lambda: create_pdf(name_entry1.get().strip(), visit_date.get().strip(), tkvar_visit_type.get().strip(),
        directed.get().strip(), complaints.get().strip(),sicktime_entry1.get().strip(),
        prev_treatment.get().strip(),other_illness.get().strip(),
        diabetes_var.get().strip(),infect.get().strip(),allergy.get().strip(),
        drug_allergy.get().strip(),inher.get().strip(),med.get().strip(),
        addict.get().strip(),tkvar_blood_donor.get().strip(),loc_stat.get().strip(),
        read_selected_items(), skin_entry.get().strip(),
        symptoms.get().strip(),tkvar_derm.get().strip(),tkvar_derm2.get().strip(),
        tkvar_surf.get().strip(),tkvar_surf2.get().strip(),
        lymph.get().strip(),tkvar_l3.get().strip(),
        ll1.get().strip(),ll2.get().strip(),tkvar_l4.get().strip(),ll6.get().strip(),
        tkvar_l5.get().strip(),tkvar_l7.get().strip(),hair3.get().strip(),tkvar_nails.get().strip(), nails.get().strip(),
        add_symp.get().strip(),tkvr.get().strip(),diagnosis.get().strip(),
        form.get().strip(),stage.get().strip(),code.get().strip(),
        diagnosis2.get().strip(),complication.get().strip(),treatment.get().strip(), treatment2.get().strip(),
        treatment3.get().strip(),treatment4.get().strip(),treatment5.get().strip(),treatment6.get().strip(),
        recomm.get().strip(),recomm2.get().strip(),recomm3.get().strip(),
        recomm4.get().strip(),recomm5.get().strip(),recomm6.get().strip(),
        comeback.get().strip(),doctor.get().strip())).grid(row=52, column = 0, columnspan = 3)

        save_todb_button = Button(myframe1, text="Сохранить в базу данных",fg = "green", background = "#fcddcf", width = 20,
        command = lambda: save_and_report("visits", visit_id_in, from_table, name_entry1.get().strip(), name_entry2.get().strip(),
        tkvar_y.get().strip(),tkvar_m.get().strip(),tkvar_d.get().strip(),
        visit_date.get().strip(),tkvar_visit_type.get().strip(),directed.get().strip(),
        complaints.get().strip(),sicktime_entry1.get().strip(),
        prev_treatment.get().strip(),other_illness.get().strip(),
        diabetes_var.get().strip(),infect.get().strip(),allergy.get().strip(),
        drug_allergy.get().strip(),inher.get().strip(),med.get().strip(),
        addict.get().strip(),tkvar_blood_donor.get().strip(),loc_stat.get().strip(),
        read_selected_items(), skin_entry.get().strip(),
        symptoms.get().strip(),tkvar_derm.get().strip(),tkvar_derm2.get().strip(),
        tkvar_surf.get().strip(),tkvar_surf2.get().strip(),
        lymph.get().strip(),tkvar_l3.get().strip(),
        ll1.get().strip(),ll2.get().strip(),tkvar_l4.get().strip(),ll6.get().strip(),
        tkvar_l5.get().strip(),tkvar_l7.get().strip(),hair3.get().strip(),tkvar_nails.get().strip(), nails.get().strip(),
        add_symp.get().strip(),tkvr.get().strip(),diagnosis.get().strip(),
        form.get().strip(),stage.get().strip(),code.get().strip(),
        diagnosis2.get().strip(),complication.get().strip(),treatment.get().strip(), treatment2.get().strip(),
        treatment3.get().strip(),treatment4.get().strip(),treatment5.get().strip(),treatment6.get().strip(),
        recomm.get().strip(),recomm2.get().strip(),recomm3.get().strip(),
        recomm4.get().strip(),recomm5.get().strip(),recomm6.get().strip(),
        comeback.get().strip(),doctor.get().strip()))
        save_todb_button.grid(row=53, column = 0, columnspan = 3)
        return


    def call_saved_for_later_tab():
        clear_frame(frame)
        append_saved_for_later(connection)
        myframe1 = new_frame(frame, (len(saved_for_later)+1)*100, 0, 1, 500, 680, 500)
        for i in range(len(saved_for_later)):
            name_button = Button(myframe1, text = saved_for_later[i].last_name, background = "#ffffff", command= lambda i=i: call_form(saved_for_later[i]))
            name_button.pack()
        return


#------------------ MAIN MENU BUTTONS ------------

    todays_patients = Button(main_menu, text = "Незавершенные карты", fg = "green", background = "#ffd2bd", width = 27, height = 3, command = call_saved_for_later_tab)
    todays_patients.place(x=0, y=0)

    search_db_button = Button (main_menu, text = "Поиск", fg = "green",  background = "#ffd2bd",  width = 27, height = 3, command = call_search_tab)
    search_db_button.place(x=200, y = 0)

    add_patient = Button (main_menu, text = "Новый Пациент/Визит", fg = "green", background = "#ffd2bd", width = 27, height = 3, command=lambda: call_form(None))
    add_patient.place(x = 400, y = 0)
            #write to database

    atexit.register(lambda: on_termination(connection))
    main_menu.mainloop()


mainwin();
