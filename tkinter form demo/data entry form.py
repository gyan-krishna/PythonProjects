# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Wed Jun  9 11:55:01 2021
@author: Gyan Krishna

Topic:
"""

import tkinter as tk
from tkinter import ttk

def submit_callback():
    print("\n\ndata entered:: ")
    print("submitted")
    print("name     = ", name.get())
    print("email    = ", email.get())
    print("language = ", language.get())
    print("gender   = ", gender_var.get())
    print("software = ", pycharm.get(), spyder.get(), lab.get(), notebook.get())

    language.set("")
    name.set("")
    email.set("")
    gender_var.set(0)
    pycharm.set(0)
    spyder.set(0)
    lab.set(0)
    notebook.set(0)


win = tk.Tk()
win.geometry("600x400")

header = tk.Label(win, text = "Log in page: ")
header.grid(row = 0, column = 0)

####################################
name = tk.StringVar()

name_label = tk.Label(win, text = "Name :", fg = "Blue", height = 2)
name_label.grid(row = 1, column = 0, sticky = tk.W)

name_entry = tk.Entry(win, width = 30, textvariable = name)
name_entry.grid(row = 1, column = 1, sticky = tk.W)

####################################
email = tk.StringVar()

name_label = tk.Label(win, text = "Email :", fg = "Blue", height = 2)
name_label.grid(row = 2, column = 0, sticky = tk.W)

name_entry = tk.Entry(win, width = 30, textvariable = email)
name_entry.grid(row = 2, column = 1, sticky = tk.W)

####################################
language = tk.StringVar()

language_label = tk.Label(win, text = "Language :", fg = "Blue", height = 2)
language_label.grid(row = 3, column = 0, sticky = tk.W)

language_list =  ["C", "C++", "Java", "Python"]
language_selection = ttk.Combobox(win, values = language_list, width = 27, height = 2, textvariable = language)
language_selection.grid(row = 3, column = 1, sticky = tk.W)

####################################
gender_var = tk.IntVar()

gender_label = tk.Label(text = "Gender :", fg = "Blue")
gender_label.grid(row = 4, column = 0, sticky = tk.NW)

gender_male = tk.Radiobutton(win, text = "Male", value = 1, variable = gender_var)
gender_male.grid(row = 4, column = 1, sticky = tk.NW)

gender_female = tk.Radiobutton(win, text = "Female", value = 2, variable = gender_var)
gender_female.grid(row = 4, column = 2, sticky = tk.NW)
######################################
pycharm = tk.IntVar()
spyder = tk.IntVar()
lab = tk.IntVar()
notebook = tk.IntVar()

software = tk.Label( text="Software: ", fg = "Blue", height = 2 )
software.grid(row = 5, column = 0, sticky = tk.W)

softwareCheckbutton1 = tk.Checkbutton(win, text = "Pycharm", variable = pycharm)
softwareCheckbutton2 = tk.Checkbutton(win, text = "Spyder", variable = spyder)
softwareCheckbutton3 = tk.Checkbutton(win, text = "Jupyter Lab", variable = lab)
softwareCheckbutton4 = tk.Checkbutton(win, text = "Jupyter Notebook", variable = notebook)

softwareCheckbutton1.grid(row = 5, column = 1)
softwareCheckbutton2.grid(row = 5, column = 2)
softwareCheckbutton3.grid(row = 5, column = 3)
softwareCheckbutton4.grid(row = 5, column = 4)
######################################

submit_button = tk.Button(win, text = "Submit", width = 5, command = submit_callback)
submit_button.grid(row = 6, column = 0, columnspan  = 4, sticky = tk.EW)

win.mainloop()