"""
This is Student manager
requires
student name , department
year , ID
User can view all the records
search ,add,update,delete
"""
from tkinter import *  # this will get tk which is used to render

import back


def getselectedrow(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])


def viewcommand():  # view function present with button
    list1.delete(0, END)
    for row in back.view():
        list1.insert(END, row)


def searchcommand():  # search fumction which we calls with button
    list1.delete(0, END)
    for row in back.search(name_text.get(), department_text.get(), year_text.get(), sid_text.get()):
        list1.insert(END, row)


def addcommand():
    back.insert(name_text.get(), department_text.get(),
                year_text.get(), sid_text.get())
    list1.delete(0, END)
    list1.insert(END, (name_text.get(), department_text.get(),
                       year_text.get(), sid_text.get()))


def deletecommand():


    back.delete(selected_tuple[0])


def update_command():
    

    back.update(selected_tuple[0], name_text.get(), department_text.get(),
                year_text.get(), sid_text.get()))


window=Tk()
l1=Label(window, text = "Name")
l1.grid(row = 0, column = 0)

l2=Label(window, text = "Department")
l2.grid(row = 0, column = 2)

l3=Label(window, text = "Year")
l3.grid(row = 1, column = 0)

l4=Label(window, text = "SID")
l4.grid(row = 1, column = 2)


name_text=StringVar()
e1=Entry(window, textvariable = name_text)
e1.grid(row = 0, column = 1)

department_text=StringVar()
e2=Entry(window, textvariable = department_text)
e2.grid(row = 0, column = 3)

year_text=StringVar()
e3=Entry(window, textvariable = year_text)
e3.grid(row = 1, column = 1)

sid_text=StringVar()
e4=Entry(window, textvariable = sid_text)
e4.grid(row = 1, column = 3)
list1=Listbox(window, height = 7, width = 40)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)
sb1=Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6)
list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)
# bind to select from the list box and get id
list1.bind('<<ListboxSelect>>', getselectedrow)

b1=Button(window, text = "view all ", width = 12, command = viewcommand)
b1.grid(row = 2, column = 3)

b2=Button(window, text = "Search entry", width = 12, command = searchcommand)
b2.grid(row = 3, column = 3)

b3=Button(window, text = " Add entry ", width = 12, command = addcommand)
b3.grid(row = 4, column = 3)

b4=Button(window, text = "Update ", width = 12)
b4.grid(row = 5, column = 3)

b5=Button(window, text = "Delete ", width = 12, command = deletecommand)
b5.grid(row = 6, column = 3)

b6=Button(window, text = "Close ", width = 12)
b6.grid(row = 7, column = 3)

window.mainloop()
