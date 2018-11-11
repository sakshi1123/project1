from tkinter import *
from tkinter import ttk
def search1():
    pass

def clear1():
    pass

def exit1():
    pass
root1=Tk()

root1.title("College Search Criteria")
root1.geometry()
lab1= Label(root1, text="Location").grid(row=7, column=7, sticky=W)
lab2= Label(root1, text="12th %").grid(row=9, column=7, sticky=W)
lab3= Label(root1, text="Budget(Yearly)").grid(row=11, column=7, sticky=W)
lab4= Label(root1, text="Course in 12th").grid(row=13, column=7, sticky=W)
lab5= Label(root1, text="Course requirement").grid(row=13, column=7,sticky=W)
root1.combo1=ttk.Combobox(root1, text= "Select location", width=15)
root1.combo2=ttk.Combobox(root1, width=15, )
root1.combo3=ttk.Combobox(root1, width=15)
root1.combo4=ttk.Combobox(root1,width=15)
root1.combo5=ttk.Combobox(root1, width=15)
root1.combo1['values']=("Delhi","Bangalore","Mumbai","U.P","Kolkata","Chennai","Kerala")
root1.combo2['values']=("above 90", "above 80", "above 70", "above 65")
root1.combo3['values']=("Above 5 Lacs", "Above 4 Lacs","Above 3 Lacs","Above 2 Lacs","Above 1 lacs","Above 50 thousands")
root1.combo4['values']=("BCA", " BBA","B.Com","Btech in CS", "B.tech in ME","B.tech in AM")
root1.combo1.grid(row=7, column=8)
root1.combo2.grid(column=8, row=9 )
root1.combo3.grid(column=8, row=11)
root1.combo4.grid(column=8, row=13)
but1 = Button(root1, text="Search ", width=6, command=search1).grid(row=20, column=7, sticky=W)
but2 = Button(root1, text="Clear", width=6, command=clear1).grid(row=20,column=8,sticky=W)
but3 = Button(root1, text="Exit", width=6, command=exit1).grid(row=20, column=9, sticky=W)

root1.mainloop()





