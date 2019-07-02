#----INTERFACE FILE---
from patients2 import *

def main():
    main_menu = Tk()
    main_menu.geometry("700x580")
    frame = Frame(main_menu, width=680, height=500)
    frame.place(x=0, y=60)
    #frame.grid(sticky='news')
    main_menu.winfo_toplevel().title("Мои Пациенты")

    def clear_frame():
        for widget in frame.winfo_children():
            widget.destroy()
        return

    def edit_visit():
        return

    def call_search():
        clear_frame()
        return

    def save_for_later(last_name, first_name,  birthyear,
                            birthmonth,  birthday, visit_date,
                            visit_type, directed, complaints, sicktime, prev_treatment,
                            other_illness, diabetes, infect, allergy, drug_allergy,
                            heredity, medicaments, addictions, blood_donor, loc_stat,
                            process_characteristic, symptoms, dermographism1, dermographism2,
                            mucous_membranes, mucous_membranes2, lymph, lymph_description,
                            lymph_description1, lymph_description2, lymph_description4,
                            lymph_description6, lymph_description5, hair_description,
                            hair_description2, nails_of, nails_desc, additional_symp,
                            tkvr, diagnosis_main, form, stage, code, diagnosis2,
                            complication, treatment, treatment2, treatment3, treatment4,
                            treatment5, treatment6, recomm, recomm2, recomm3,
                            recomm4, recomm5, recomm6, comeback, doctor):
        saved_for_later.append(Visit(last_name, first_name,  birthyear,
                                birthmonth,  birthday, visit_date,
                                visit_type, directed, complaints, sicktime, prev_treatment,
                                other_illness, diabetes, infect, allergy, drug_allergy,
                                heredity, medicaments, addictions, blood_donor, loc_stat,
                                process_characteristic, symptoms, dermographism1, dermographism2,
                                mucous_membranes, mucous_membranes2, lymph, lymph_description,
                                lymph_description1, lymph_description2, lymph_description4,
                                lymph_description6, lymph_description5, hair_description,
                                hair_description2, nails_of, nails_desc, additional_symp,
                                tkvr, diagnosis_main, form, stage, code, diagnosis2,
                                complication, treatment, treatment2, treatment3, treatment4,
                                treatment5, treatment6, recomm, recomm2, recomm3,
                                recomm4, recomm5, recomm6, comeback, doctor))
        clear_frame()
        report = Label(frame, text = "Карта сохранена на потом", height = 10, width = 20)
        report.grid(row = 0, column = 1)
        return

    def call_new_patient_form():
        clear_frame()
        #canvas, frame, window, scroll
        mycanvas = Canvas(frame, width=680, height=500, scrollregion=(0,0,680, 500))
        mycanvas.grid(row=0, column=0, sticky="nsew")

        myframe = Frame(mycanvas, width=680, height=500)
        myframe.grid(row = 0, column = 0)
        myframe.rowconfigure(0, weight=1)
        myframe.columnconfigure(0, weight=1)
        mycanvas.create_window(0, 0, width = 680, height = 1350, window = myframe, anchor = NW)

        canvbar = Scrollbar(frame, orient = "vertical", command = mycanvas.yview)
        canvbar.grid(row = 0, column = 1, sticky="ns")
        mycanvas.configure(yscrollcommand = canvbar.set)
        mycanvas.configure(scrollregion=mycanvas.bbox("all"))

        #LABELS
        name_label1 = Label(myframe, text="Фамилия")
        name_label2 = Label(myframe, text="Имя")
        birthdate_label = Label(myframe, text="Дата Рождения")
        visit_date_label = Label(myframe, text="Дата визита")
        visit_type_label = Label(myframe, text="Тип визита")
        directed_label = Label(myframe, text = "Направлен")
        complaints_label = Label(myframe, text = "Жалобы")
        sicktime = Label(myframe, text="Болен")
        prev_treatment_label = Label(myframe, text = "Лечение/Самолечение")
        other_illness_label = Label(myframe, text = "Сопутствующие заболевания")
        diabetes_label = Label(myframe, text = "Сахарный диабет")
        infect_label = Label(myframe, text = "Инфекционные заболевания")
        allergy_label = Label(myframe, text = "Пищевая аллергия")
        drug_allergy_label = Label(myframe, text = "Лекарственная непереносимость")
        inher_label = Label(myframe, text = "Наследственность")
        med_label = Label(myframe, text = "Постоянно принимает препараты")
        addict_label = Label(myframe, text ="Вредные привычки")
        blood_donor_label = Label(myframe, text = "Донором крови")
        loc_stat_label = Label(myframe, text = "Локальный статус")
        process_label = Label(myframe, text = "Кожный патологический процесс")
        process_char_label = Label(myframe, text = "Характер процесса")
        symptoms_label = Label(myframe, text="Симптомы/описание")
        derm_label = Label(myframe, text = "Дермографизм")
        surf_label = Label(myframe, text = "Слизистые оболочки")
        lymph_label = Label(myframe, text = "Лимфатические узлы")
        hair_label = Label(myframe, text = "Оволосение по типу:")
        h_label = Label(myframe, text = "Волосы")
        n_label = Label(myframe, text = "Ногктевые пластины")
        add_symp_label = Label(myframe, text = "Дополнительные симптомы")
        comm_label = Label(myframe, text = "На момент осмотра чесотка и педикулез")
        diagnosis_label = Label(myframe, text="Диагноз основной")
        form_label = Label(myframe, text="Форма")
        stage_label = Label(myframe, text="Стадия")
        code_label = Label(myframe, text="Код МКБ")
        diagnosis2_label = Label(myframe, text="Диагноз сопутствующий")
        complications_label = Label(myframe, text="Осложнения")
        treatment_label = Label(myframe, text="План обследования")
        recomm_label = Label(myframe, text="Рекомендации")
        comeback_label = Label(myframe, text="Повторная явка")
        doctor_label = Label(myframe, text="Врач")

        name_label1.grid(row=0, column = 0, sticky = W)
        name_entry1 = Entry(myframe)
        name_entry1.grid(row=0, column = 1)

        name_label2.grid(row=1, column = 0, sticky = W)
        name_entry2 = Entry(myframe)
        name_entry2.grid(row=1, column = 1)

        tkvar_y = IntVar(myframe)
        tkvar_m = IntVar(myframe)
        tkvar_d = IntVar(myframe)
        birthdate_label.grid(row = 2, column = 0, sticky = W)
        birthyear = OptionMenu(myframe, tkvar_y, *years)
        birthyear.grid(row=2, column =1,sticky = W)
        birthmonth = OptionMenu(myframe, tkvar_m, *months)
        birthmonth.grid(row=2, column =1)
        birthday = OptionMenu(myframe, tkvar_d, *days)
        birthday.grid(row=2, column =1,sticky = E)

        visit_date_label.grid(row=3, column = 0, sticky = W) #default today
        year=datetime.date.today().year
        month=datetime.date.today().month
        day=datetime.date.today().day
        date_str = StringVar(myframe, value = "{}/{}/{}".format(day, month, year))
        visit_date = Entry(myframe, textvariable = date_str)
        visit_date.grid(row=3, column=1)

        visit_type_label.grid(row=4, column = 0, sticky = W)
        tkvar_visit_type = StringVar(myframe)
        visit_type = OptionMenu(myframe, tkvar_visit_type, *visit_types)
        visit_type.grid(row=4, column = 1)

        directed_label.grid(row=5, column = 0, sticky = W)
        dir_str=StringVar(myframe, value = "самостоятельно")
        directed =Entry(myframe, textvariable = dir_str)
        directed.grid(row=5, column = 1)

        complaints_label.grid(row=6, column = 0, sticky = W)
        complaints=Entry(myframe)
        complaints.grid(row=6, column = 1)

        sicktime.grid(row=7, column = 0, sticky = W)
        sicktime_entry1 = ttk.Combobox(myframe, values = ["находится на лечении", "1 месяц"])
        sicktime_entry1.grid(row=7, column = 1)

        prev_treatment_label.grid(row=8, column = 0, sticky = W)
        prev_treatment = ttk.Combobox(myframe, values=['отрицает','с положительной динамикой', 'с отрицательной динамикой', 'без эффекта'])
        prev_treatment.grid(row=8, column = 1)

        other_illness_label.grid(row=10, column = 0, sticky = W)
        un_str = StringVar(myframe, value = "полностью не обследован")
        other_illness = Entry(myframe, textvariable = un_str)
        other_illness.grid(row=10, column = 1)

        diabetes_label.grid(row=11, column = 0, sticky = W)
        diabetes_var=StringVar(myframe)
        options = {"отрицает", "первого типа", "второго типа"}
        diabetes = OptionMenu(myframe, diabetes_var, *options)
        diabetes.grid(row=11, column = 1)

        infect_label.grid(row=12, column = 0, sticky = W)
        deny_str2=StringVar(myframe, value = "отрицает")
        infect = Entry(myframe, textvariable = deny_str2)
        infect.grid(row=12, column = 1)

        allergy_label.grid(row=13, column = 0, sticky = W)
        deny_str3=StringVar(myframe, value = "отрицает")
        allergy = Entry(myframe, textvariable = deny_str3)
        allergy.grid(row=13, column = 1)

        drug_allergy_label.grid(row=14, column = 0, sticky = W)
        deny_str4=StringVar(myframe, value = "отрицает")
        drug_allergy = Entry(myframe, textvariable = deny_str4)
        drug_allergy.grid(row=14, column = 1)

        inher_label.grid(row=15, column = 0, sticky = W)
        inher_str=StringVar(myframe, value = "не отягощяна")
        inher = Entry(myframe, textvariable = inher_str)
        inher.grid(row=15, column = 1)

        med_label.grid(row=16, column = 0, sticky = W)
        deny_str5=StringVar(myframe, value = "отрицает")
        med = Entry(myframe, textvariable = deny_str5)
        med.grid(row=16, column = 1)

        addict_label.grid(row=17, column = 0, sticky = W)
        deny_str6=StringVar(myframe, value = "отрицает")
        addict = Entry(myframe, textvariable = deny_str6)
        addict.grid(row=17, column = 1)

        blood_donor_label.grid(row=18, column = 0, sticky = W)
        tkvar_blood_donor = StringVar(myframe)
        blood_donor = OptionMenu(myframe, tkvar_blood_donor, *donor)
        blood_donor.grid(row=18, column = 1)

        loc_stat_label.grid(row=19, column = 0, sticky = W)
        loc_stat = Entry(myframe)
        loc_stat.grid(row=19, column = 1)

        process_label.grid(row = 20, columnspan = 3)
        process_char_label.grid(row = 21, column = 0, sticky = W)
        scroll = Scrollbar(myframe)
        process_char = Listbox(myframe, selectmode = MULTIPLE, yscrollcommand = scroll.set, height = 3, width = 25)
        for item in process:
            process_char.insert(END, item)
        scroll.config(command = process_char.yview)
        scroll.grid(row = 21, column = 2, sticky = W)
        process_char.grid(row = 21, column = 1)

        def read_selected_items():
            selected_items = []
            for i in process_char.curselection():
                selected_items.append(process_char.get(i))
            return selected_items

        symptoms_label.grid(row = 23, column = 0, sticky = W)
        symptoms = Entry(myframe)
        symptoms.grid(row = 23, column = 1)

        derm_label.grid(row = 24, column = 0, sticky = W)
        tkvar_derm = StringVar(myframe)
        dermm = OptionMenu(myframe, tkvar_derm, *derm)
        dermm.grid(row=24, column = 1)
        tkvar_derm2 = StringVar(myframe)
        dermm2 = OptionMenu(myframe, tkvar_derm2, *derm2)
        dermm2.grid(row=24, column = 2)

        surf_label.grid(row = 25, column = 0, sticky = W)
        tkvar_surf = StringVar(myframe)
        surff = OptionMenu(myframe, tkvar_surf, *surf)
        surff.grid(row=25, column = 1)
        tkvar_surf2 = StringVar(myframe)
        surff2 = OptionMenu(myframe, tkvar_surf2, *surf2)
        surff2.grid(row=25, column = 2)

        lymph_label.grid(row = 26, column = 0, sticky = W)
        lymph = Entry(myframe)
        lymph.grid(row = 26, column = 1)

        tkvar_l3 = StringVar(myframe)
        ll3 = OptionMenu(myframe, tkvar_l3, *l3)
        ll3.grid(row=26, column = 2)

        ll1 = ttk.Combobox(myframe, values =['не увеличены','увеличены до'])
        ll1.grid(row=27, column = 1)

        ll2 = ttk.Combobox(myframe, values = ['симметрично','не симметрично'])
        ll2.grid(row=28, column = 1)

        tkvar_l4 = StringVar(myframe)
        ll4 = OptionMenu(myframe, tkvar_l4, *l4)
        ll4.grid(row=27, column = 2)

        ll6 = ttk.Combobox(myframe, values = ['неспаянные','спаянные'])
        ll6.grid(row=29, column = 1)

        tkvar_l5 = StringVar(myframe)
        ll5 = OptionMenu(myframe, tkvar_l5, *l5)
        ll5.grid(row=28, column = 2)


        hair_label.grid(row = 30, column = 0, sticky = W)
        tkvar_l7 = StringVar(myframe)
        ll7 = OptionMenu(myframe, tkvar_l7, *l7)
        ll7.grid(row=30, column = 1)

        h_label.grid(row = 31, column = 0, sticky=W)
        hair3 = ttk.Combobox(myframe, values = ['без зменений', 'изменены'])
        hair3.grid(row = 31, column = 1)

        n_label.grid(row = 32, column = 0, sticky = W)
        tkvar_nails = StringVar(myframe)
        parts = {'кистей', 'стоп', 'кистей и стоп'}
        tkvarparts = OptionMenu(myframe, tkvar_nails, *parts)
        tkvarparts.grid(row = 32, column = 1)
        nails = ttk.Combobox(myframe, values = ["не изменены"])
        nails.grid(row = 32, column = 2)

        add_symp_label.grid(row = 35, column = 0, sticky = W)
        add_symp = Entry(myframe)
        add_symp.grid(row = 35, column = 1)

        comm_label.grid(row = 36, column = 0, columnspan=2, sticky = W)
        tkvr = StringVar(myframe)
        choices = {'не выявлены', 'выявлены'}
        var8 = OptionMenu(myframe, tkvr, *choices)
        var8.grid(row = 36, column = 1, sticky = E)

        diagnosis_label.grid(row = 37, column = 0, sticky = W)
        diagnosis = Entry(myframe)
        diagnosis.grid(row = 37, column = 1)

        form_label.grid(row = 38, column = 0, sticky = W)
        form = Entry(myframe)
        form.grid(row = 38, column = 1)

        stage_label.grid(row = 39, column = 0, sticky = W)
        stage = Entry(myframe)
        stage.grid(row = 39, column = 1)

        code_label.grid(row = 40, column = 0, sticky = W)
        code = Entry(myframe)
        code.grid(row = 40, column = 1)

        diagnosis2_label.grid(row = 41, column = 0, sticky = W)
        diagnosis2 = Entry(myframe)
        diagnosis2.grid(row = 41, column = 1)

        complications_label.grid(row = 43, column = 0, sticky = W)
        complication = Entry(myframe)
        complication.grid(row = 43, column = 1)

        treatment_label.grid(row=44, column = 1)
        treatment = Entry(myframe)
        treatment.grid(row = 45, column = 0)
        treatment.insert(0, "1.")
        treatment2 = Entry(myframe)
        treatment2.grid(row = 45, column = 1)
        treatment2.insert(0, "2.")
        treatment3 = Entry(myframe)
        treatment3.grid(row = 45, column = 2)
        treatment3.insert(0, "3.")
        treatment4 = Entry(myframe)
        treatment4.grid(row = 46, column = 0)
        treatment4.insert(0, "4.")
        treatment5 = Entry(myframe)
        treatment5.grid(row = 46, column = 1)
        treatment5.insert(0, "5.")
        treatment6 = Entry(myframe)
        treatment6.grid(row = 46, column = 2)
        treatment6.insert(0, "6.")

        recomm_label.grid(row=47, column = 1)
        recomm = Entry(myframe)
        recomm.grid(row = 48, column = 0)
        recomm.insert(0, "1. Режим")
        recomm2 = Entry(myframe)
        recomm2.grid(row = 48, column = 1)
        recomm2.insert(0, "2. Диета")
        recomm3 = Entry(myframe)
        recomm3.grid(row = 48, column = 2)
        recomm3.insert(0, "3.")
        recomm4 = Entry(myframe)
        recomm4.grid(row = 49, column = 0)
        recomm4.insert(0, "4.")
        recomm5 = Entry(myframe)
        recomm5.grid(row = 49, column = 1)
        recomm5.insert(0, "5.")
        recomm6 = Entry(myframe)
        recomm6.grid(row = 49, column = 2)
        recomm6.insert(0, "6.")

        comeback_label.grid(row=50, column = 0)
        comeback = Entry(myframe)
        comeback.grid(row = 50, column = 1)

        doctor_label.grid(row=51, column = 0)
        doctor = Entry(myframe)
        doctor.grid(row = 51, column = 1)
        doctor.insert(0, "Большева А. А.")

        save_button = Button(myframe, text = "Сохранить на потом", fg = "red",
        command = lambda: save_for_later(name_entry1.get(),name_entry2.get(),
        tkvar_y.get(),tkvar_m.get(),tkvar_d.get(),
        visit_date.get(),tkvar_visit_type.get(),directed.get(),
        complaints.get(),sicktime_entry1.get(),
        prev_treatment.get(),other_illness.get(),
        diabetes_var.get(),infect.get(),allergy.get(),
        drug_allergy.get(),inher.get(),med.get(),
        addict.get(),tkvar_blood_donor.get(),loc_stat.get(),
        read_selected_items(),
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

        mycanvas.configure(scrollregion=mycanvas.bbox("all"))
        return


    def call_saved_for_later():
        clear_frame()
        mycanvas = Canvas(frame, width=680, height=500, scrollregion=(0,0,680, 500))
        mycanvas.grid(row=0, column=0, sticky="nsew")

        myframe = Frame(mycanvas, width=680, height=500)
        myframe.grid(row = 0, column = 0)
        myframe.rowconfigure(0, weight=1)
        myframe.columnconfigure(0, weight=1)
        mycanvas.create_window(0, 0, width = 680, height = 1350, window = myframe, anchor = NW)

        canvbar = Scrollbar(frame, orient = "vertical", command = mycanvas.yview)
        canvbar.grid(row = 0, column = 1, sticky="ns")
        mycanvas.configure(yscrollcommand = canvbar.set)
        mycanvas.configure(scrollregion=mycanvas.bbox("all"))

        for i in range(len(saved_for_later)):
            name_button = Label(myframe, text = saved_for_later[i].last_name)
            name_button.pack()
        return




#------------------MAIN MENU BUTTONS------------

    todays_patients = Button(main_menu, text = "Незавершенные карты", fg = "green", width = 25, height = 3, command = call_saved_for_later)
    todays_patients.place(x=0, y=0)

    search_db = Button (main_menu, text = "Поиск", fg = "green",  width = 25, height = 3, command = call_search)
    search_db.place(x=223, y = 0)

    add_patient = Button (main_menu, text = "Новый Пациент/Визит", fg = "green", width = 25, height = 3, command = call_new_patient_form)
    add_patient.place(x = 446, y = 0)
            #write to database

    main_menu.mainloop()


main();
