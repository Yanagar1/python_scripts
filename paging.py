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
