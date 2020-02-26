from tkinter import *

window=Tk()

first_LB=Label(window,width=100,text='간단한 GUI프로그램!')
# first_LB.grid(row=0,column=0)

b1=Button(window,text='환영합니다.')
b2=Button(window,text='종료')
# b1.grid(row=1,column=0)
# b2.grid(row=1,column=1)

first_LB.pack()
b1.pack()
b2.pack()

window.mainloop()

