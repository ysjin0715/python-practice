from tkinter import *

window=Tk()

change=str(0)


def change1():
    p=e1.get()
    global change
    change='{:.3f}'.format(float(p)*2.54)
    l4['text']=change+" 센티미터"


l1=Label(window,text='인치를 센티미터로 변환하는 프로그램:')
l2=Label(window,text='인치를 입력하시오:')
l3=Label(window,text='변환결과: ')
l4=Label(window,text=change+" 센티미터")
l1.grid(row=0,column=0,columnspan=2)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)
l4.grid(row=2,column=1)

e1=Entry(window)
e1.grid(row=1,column=1)

b1=Button(window,text='변환!',command=change1)
b1.grid(row=3,column=1)

window.mainloop()