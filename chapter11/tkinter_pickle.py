from tkinter import *
from pickle import *

# 함수 만들기
## 주소를 pickle형식으로 저장하는 함수
def change_adress():
   adress = e1.get()
   file = open('adress.txt','wb')
   dump(adress,file)
   file.close()

def change_pickle():
   file = open('adress.txt','rb')
   l1.configure(text=load(file))
   file.close()


# tkinter UI 만들기

window = Tk()
window.title('변환')

e1 = Entry(window)
e1.grid(row = 0, column = 0, columnspan = 5)

l1 = Label(window,text = "")
l1.grid(row = 1, column = 0, columnspan = 5)

b1 = Button(window, text = '변환',command = change_adress)
b2 = Button(window, text = '출력',command = change_pickle)
b1.grid(row = 2, column = 0)
b2.grid(row = 2, column = 4)

window.mainloop()

