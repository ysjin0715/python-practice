from tkinter import *
import random

window = Tk()
subject=""

def regame():
    global n
    n=random.randrange(0,100)
    e1.delete(0,END)
    global subject
    subject='숫자를 입력해주세요(0-100)'
    l1['text']=subject

def guess():
    p=int(e1.get())
    if n>p:
        subject="너무 낮아요!!"
        l1['text']=subject
    elif n<p:
        subject="너무 높아요!!"
        l1['text']=subject
    else:
        subject="정답입니다!"
        l1['text']=subject

e1=Entry(window)
e1.grid(row=1,column=0,columnspan=2)

b1=Button(window,text="숫자를 입력",command=guess)
b1.grid(row=2,column=0)
b2=Button(window,text="게임을 다시 실행",command=regame)
b2.grid(row=2,column=1)

l1=Label(window,text=subject)
l1.grid(row=0,column=0,columnspan=2)


regame()
window.mainloop()