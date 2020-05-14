"""
This is Student manager 
requires 
student name , department
year , ID
User can view all the records 
search ,add,update,delete
"""
from tkinter import *
window = Tk()
l1 = Label(window, text="Name")
l1.grid(row=0, column=0)

l2 = Label(window, text="Department")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="SID")
l4.grid(row=1, column=2)


name_text = StringVar()
e1 = Entry(window, textvariable=name_text)
e1.grid(row=0, column=1)

department_text = StringVar()
e2 = Entry(window, textvariable=department_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

sid_text = StringVar()
e4 = Entry(window, textvariable=sid_text)
e4.grid(row=1, column=3)
list1 = Listbox(window, height=7, width=40)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window,text ="view all ", width=12)
b1.grid(row =2,column=3)

b2 = Button(window,text ="Search entry", width=12)
b2.grid(row =3,column=3)

b3 = Button(window,text =" Add entry ", width=12)
b3.grid(row =4,column=3)

b4 = Button(window,text ="Update ", width=12)
b4.grid(row =5,column=3)

b5 = Button(window,text ="Delete ", width=12)
b5.grid(row =6,column=3)

b6 = Button(window,text ="Close ", width=12)
b6.grid(row =7,column=3)

window.mainloop()
