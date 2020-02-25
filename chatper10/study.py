import tkinter
#1.버튼이 있는 윈도우를 생성하기
def study1():
    window = tkinter.Tk()
    button=tkinter.Button(window,text="클릭하세요!")
    button.pack()

    window.mainloop()

#2. 엔트리와 레이블 위젯
def study2():
    window=tkinter.Tk()

    l1=tkinter.Label(window, text="화씨")
    l2=tkinter.Label(window, text="섭씨")
    l1.pack()
    l2.pack()

    e1=tkinter.Entry(window)
    e2=tkinter.Entry(window)
    e1.pack()
    e2.pack()

    b1=tkinter.Button(window,text="화씨->섭씨")
    b2=tkinter.Button(window,text="섭씨->화씨")
    b1.pack()
    b2.pack()

    window.mainloop()

#격자 배치관리자(grid geomentry manager) 이용하기
def study3():
    window=tkinter.Tk()

    l1=tkinter.Label(window,text="화씨")
    l2=tkinter.Label(window,text="섭씨")
    l1.grid(row=0, column=0)
    l2.grid(row=1, column=0)

    e1=tkinter.Entry(window)
    e2=tkinter.Entry(window)
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)

    b1=tkinter.Button(window, text="화씨->섭씨")
    b2=tkinter.Button(window, text="섭씨->화씨")
    b1.grid(row=2,column=0)
    b2.grid(row=2,column=1)

    window.mainloop()

#버튼 이벤트 처리하기(command의 이용)
def study4():
    def process():
        print("안녕하세요")

    window=tkinter.Tk()
    button=tkinter.Button(window,text="클릭하세요",command=process)
    button.pack()
    window.mainloop()


#버튼 이벤트 처리하기(command의 이용2)
def study5():
    def process():
        e2.insert(0,"100")

    window = tkinter.Tk()

    l1 = tkinter.Label(window, text="화씨")
    l2 = tkinter.Label(window, text="섭씨")
    l1.grid(row=0, column=0)
    l2.grid(row=1, column=0)

    e1 = tkinter.Entry(window)
    e2 = tkinter.Entry(window)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    b1 = tkinter.Button(window, text="화씨->섭씨",command=process)
    b2 = tkinter.Button(window, text="섭씨->화씨")
    b1.grid(row=2, column=0)
    b2.grid(row=2, column=1)

    window.mainloop()

def study6():
    #버튼을 두번 누르면 결과값이 두개 출력된다... 고칠수가 없음.
    def process1():
        temperature1=float(e1.get())
        mytemp1=(temperature1-32)*5/9
        e2.delete(0, len(e2.get()))
        e2.insert(0,str(mytemp1))

    def process2():
        temperature2=float(e2.get())
        mytemp2=temperature2*9/5+32
        e1.delete(0, len(e2.get()))
        e1.insert(0,str(mytemp2))

    window = tkinter.Tk()

    l1 = tkinter.Label(window, text="화씨")
    l2 = tkinter.Label(window, text="섭씨")
    l1.grid(row=0, column=0)
    l2.grid(row=1, column=0)

    e1 = tkinter.Entry(window)
    e2 = tkinter.Entry(window)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    b1 = tkinter.Button(window, text="화씨->섭씨",command=process1)
    b2 = tkinter.Button(window, text="섭씨->화씨",command=process2)
    b1.grid(row=2, column=0)
    b2.grid(row=2, column=1)

    window.mainloop()

#위젯의 색상과 폰트 변경하기
def study7():
    def process1():
        temperature1=float(e1.get())
        mytemp1=(temperature1-32)*5/9
        e2.delete(0, len(e2.get()))
        e2.insert(0,str(mytemp1))

    def process2():
        e2.insert(0,"")
        temperature2=float(e2.get())
        mytemp2 = temperature2 * 9 / 5 + 32
        e1.delete(0, len(e2.get()))
        e1.insert(0,str(mytemp2))

    window = tkinter.Tk()

    l1 = tkinter.Label(window, text="화씨",font='helvetica 16 italic')
    l2 = tkinter.Label(window, text="섭씨",font='helvetica 16 italic')
    l1.grid(row=0, column=0)
    l2.grid(row=1, column=0)

    e1 = tkinter.Entry(window,bg='yellow',fg='black')
    e2 = tkinter.Entry(window,bg='yellow',fg='black')
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    b1 = tkinter.Button(window, text="화씨->섭씨",command=process1)
    b2 = tkinter.Button(window, text="섭씨->화씨",command=process2)
    b1.grid(row=2, column=0)
    b2.grid(row=2, column=1)

    window.mainloop()

#절대 위치 배치 관리자(place geometry manager)
def study8():
    window=tkinter.Tk()

    a=tkinter.Label(window,text='박스#1',bg='red',fg='white')
    a.place(x=0,y=0)

    a=tkinter.Label(window,text='박스#2',bg='blue',fg='white')
    a.place(x=10,y=10)

    a=tkinter.Label(window,text='박스#3',bg='green',fg='white')
    a.place(x=20,y=20)

    a=tkinter.Label(window,text='박스#4',bg='pink',fg='white')
    a.place(x=30,y=30)

    a=tkinter.Label(window,text='박스#5',bg='black',fg='white')
    a.place(x=40,y=40)

    window.mainloop()


def study9():
    def change_img():
        path=inputBox.get()
        img=tkinter.PhotoImage(file=path)
        imageLabel.configure(image=img)
        imageLabel.image=img

    window=tkinter.Tk()

    photo=tkinter.PhotoImage(file="../assets/Lenna.png")
    imageLabel=tkinter.Label(window, image=photo)
    imageLabel.pack()

    inputBox=tkinter.Entry(window)
    inputBox.pack()

    button=tkinter.Button(window, text='Submit',command=change_img)
    button.pack()

    window.mainloop()


study9()
