from paging import*

def main():
	top=Tk()
	top.geometry("500x500")
	my_frame = Frame(top)
	my_frame.place(relheight = 1.0, relwidth=1.0, x=100, y = 30)

	welcome = Label(top, bg = "dark green", fg = "white", text = "Welcome to the little Office Assistant!")
	welcome.place(height=30, width = 500, x = 0, y = 0)

	def browse_source():
		global source_folder
		source_folder = filedialog.askdirectory()
		msg = Label(my_frame, text = "Chose as source folder: "+ source_folder, bg = "white")
		msg.place(height = 50, width= 400, x = 0, y = 0)
		return source_folder

	def browse_destination():
		global destination_folder
		destination_folder=filedialog.askdirectory()
		msg = Label(my_frame, text = "Chose as destination folder: "+ destination_folder, bg = "white")
		msg.place(height = 50, width= 400, x = 0, y = 50)
		play_button = tkinter.Button(my_frame, text = "Move'em", command= lambda: relocate_my_files(source_folder, destination_folder))
		play_button.place(height = 50, width = 100, x = 150, y  = 120)
		return destination_folder

	def call_browse():
		for widget in my_frame.winfo_children():
			widget.destroy()
		#search for file
		#browsebutton0 = tkinter.Button(my_frame, text = "Choose a file with list of items", command = browse_source)
		#browsebutton1.place(height = 50, width= 400, x = 0, y = 0)
		#fname = tkFileDialog.askopenfilename(filetypes = (("Template files", "*.txt"), ("All files", "*")))

		browsebutton1 = tkinter.Button(my_frame, text = "Select source folder", command = browse_source)
		browsebutton1.place(height = 50, width= 400, x = 0, y = 0)
		browsebutton2 = tkinter.Button(my_frame, text = "Select destination folder", command = browse_destination)
		browsebutton2.place(height = 50, width= 400, x = 0, y = 50)

	def print_joke():
		#my_frame.pack_forget()
		for widget in my_frame.winfo_children():
			widget.destroy()
		my_text = random_joke()
		label = Message(my_frame, text = my_text, bg = "white", padx=15, justify = CENTER, aspect = 200)
		label.place(height = 150, width= 400, x = 0, y = 0)
		#label.pack()
		return

	def print_hover_message(msg):
		return

	def relocate_my_files(source_folder, destination_folder):
		files_to_relocate=open('C:/Users/ygarip/Desktop/python/FILES_TO_RELOCATE.txt')
		files = []
		files=files_to_relocate.read()
		files = files.split("\n")
		files_to_relocate.close()
		source_folder=str(source_folder+"/")
		destination_folder=str(destination_folder+"/")
		count = 0

		scrollbar = Scrollbar(my_frame)
		scrollbar.pack(side = RIGHT, fill=Y)
		listbox = Listbox(my_frame, selectmode = EXTENDED, yscrollcommand=scrollbar.set)
		scrollbar.config(command=listbox.yview)

		for file in files:
			src_path = Path(source_folder+file)
			if src_path.exists():
				dst_path = destination_folder+file
				shutil.move(src_path, dst_path)
				output_str=("Moved ", file, "to ", destination_folder)
				listbox.insert(END, ' '.join(output_str))
				#listbox.pack(fill=BOTH)
				#listbox.place(x=100, y = 30)
				count+=1
			else:
				output_str = (file, "NOT FOUND")
				listbox.insert(END, ' '.join(output_str))
				#listbox.pack(fill=BOTH)
				#listbox.place(x=100, y = 30)
		return_str = ("Moved ", str(count), "files")
		listbox.insert(END, ' '.join(return_str))
		listbox.place(width = 395, relheight = 0.9, x=0, y = 0)
		return count

	def analyze_lists():
		file_obj1  = open('C:/Users/ygarip/Desktop/python/list1.txt')
		file_obj2  = open('C:/Users/ygarip/Desktop/python/list2.txt')

		source1 = file_obj1.readlines()
		source2 = file_obj2.readlines()
		source1 = [x.strip() for x in source1]
		source2 = [x.strip() for x in source2]
			#iliminate duplicates
		un1=[]
		un2=[]
		common_values=[]
		scrollbar = Scrollbar(my_frame)
		scrollbar.pack(side = RIGHT, fill=Y)
		listbox = Listbox(my_frame, selectmode = EXTENDED, yscrollcommand=scrollbar.set)
		scrollbar.config(command=listbox.yview)

		for i in range(len(source1)):
			for m in range(len(source2)):
				if (source1[i]==source2[m]):
					common_values.append(source1[i])

		for i in source1:
			if i not in common_values:
				un1.append(i)
		for i in source2:
			if i not in common_values:
				un2.append(i)

		file_obj1.close()
		file_obj2.close()

		if not common_values:
			listbox.insert(END, ''.join("THERE ARE NO VALUES IN COMMON"))
		else:
			listbox.insert(END, ''.join("THE COMMON VALUES ARE:"))
			for i in common_values:
				listbox.insert(END, i)


		if not un1:
			listbox.insert(END, ''.join("THERE ARE NO UNIQUE VALUES IN THE FIRST LIST"))
		else:
			listbox.insert(END, ''.join("THE VALUES THAT ONLY THE FIRST LIST HAS:"))
			for i in un1:
				listbox.insert(END, ''.join(i))


		if not un2:
			listbox.insert(END, ''.join("THERE ARE NO UNIQUE VALUES IN THE SECOND LIST"))
		else:
			listbox.insert(END, ''.join("THE VALUES THAT ONLY THE SECOND LIST HAS:"))
			for i in un2:
				listbox.insert(END, ''.join(i))

		listbox.place(width = 395, relheight = 0.9, x=0, y = 0)
		return

	def list_analyzer():
		for widget in my_frame.winfo_children():
			widget.destroy()
		browsebutton1 = tkinter.Button(my_frame, text = "Compare 1-to-1 lists, as in Did I copy it right?", command=compare_lists)
		browsebutton1.place(height = 50, width= 400, x = 0, y = 0)
		browsebutton2 = tkinter.Button(my_frame, text = "See common values and differences", command = analyze_lists)
		browsebutton2.place(height = 50, width= 400, x = 0, y = 50)
		return


	button1=tkinter.Button(top, text="Compare lists", command = list_analyzer)
	button1.place(bordermode=OUTSIDE, height=50, width = 100, x=0, y=30)
	#msg = "Not available yet"
	#button1.bind('<Enter>', print_message(msg))
	#button1.bind('<Leave>', remove_message())

	button2=tkinter.Button(top, text="Rename files", command = rename_my_files)
	#button2.pack()
	button2.place(bordermode=OUTSIDE, height=50, width = 100, x=0, y=80)


	button3=tkinter.Button(top, text="Relocate files", command = call_browse)
	button3.place(height=50, width = 100, x=0, y=130)


	button0=tkinter.Button(top, text="How boring...", command = print_joke)
	#button0.pack()
	button0.place(height=50, width = 100, x=0, y=180)

	top.mainloop()

main();
