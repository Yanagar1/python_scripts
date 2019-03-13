import os
import glob
import shutil
from pathlib import Path
import random
from tkinter import *
import tkinter
from tkinter import filedialog

def random_joke():
	jokes_list = open('C:/Users/ygarip/Desktop/python/jokes.txt', encoding = "utf8")
	jokes = jokes_list.readlines()
	jokes=[x.strip() for x in jokes]
	jokes_list.close()
	x=random.randint(0, (len(jokes)-1))
	return jokes[x]

def compare_lists():
	file_obj1  = open('C:/Users/ygarip/Desktop/python/list1.txt')
	file_obj2  = open('C:/Users/ygarip/Desktop/python/list2.txt')

	source1 = file_obj1.readlines()
	source2 = file_obj2.readlines()
	source1 = [x.strip() for x in source1]
	source2 = [x.strip() for x in source2]
	errors =[]
	for i in range(len(source1)):
		if (source1[i]!=source2[i]):
			errors.append(i+1)
	if len(errors)==None:
		print("All CORRECT")
	else:
		print("Errors count: ", len(errors))
		print("ASSUMING INDEX STARTS WITH 1:")
		print("Errors at values:", errors)
	file_obj1.close()
	file_obj2.close()
	return errors

def rename_my_files():

	source_folder = filedialog.askdirectory()
	filenames=open('C:/Users/ygarip/Desktop/python/filenames.txt')
	list=[]
	list=filenames.read()
	list.splitlines()
	list=list.split("|")
	filenames.close()
	my_str = '*'+ str(format)
	#files = glob.glob(my_str)
	count = 0
	print(list)
	i=0
	while i<len(list):
		print("Rename: ",file, "to ", list[i+1])
		os.rename(file, list[i+1])
		count+=1
		i+=2
	print("RENAMED TOTAL: ", count, "FILES")
	return count
