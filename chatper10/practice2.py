from tkinter import *

window=Tk()

total=0

def sum():
    s1=int(e1.get())
    global total
    total+=s1
    second_label['text']=str(total)


def m():
    m1=int(e1.get())
    global total
    total-=m1
    second_label['text']=str(total)


def clear():
    e1.delete(0,END)
    second_label['text']=0


first_Label=Label(window,text="현재 합계:")
second_label=Label(window,text=total)
first_Label.grid(row=0,column=0)
second_label.grid(row=0,column=1)


e1=Entry(window)
e1.grid(row=1,column=0,columnspan=3)


b1=Button(window,text="더하기(+)",command=sum)
b2=Button(window,text="빼기(-)",command=m)
b3=Button(window,text="초기화",command=clear)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)


window.mainloop()