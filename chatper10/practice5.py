from tkinter import *
import sys

window=Tk()
file={"양승진": ["무직", "대한민국"]}


def quit():
    sys.exit()


l1=Label(window,text="이름")
l2=Label(window,text="직업")
l3=Label(window,text="국적")
l1.grid(row=0,column=0,columnspan=2)
l2.grid(row=1,column=0,columnspan=2)
l3.grid(row=2,column=0,columnspan=2)


e1=Entry(window)
e2=Entry(window)
e3=Entry(window)
e1.grid(row=0,column=3)
e2.grid(row=1,column=3)
e3.grid(row=2,column=3)


b1=Button(window,text="Show")
b2=Button(window,text="Quit",command=quit)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)


window.mainloop()
