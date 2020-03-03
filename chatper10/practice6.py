from tkinter import *
import random

window=Tk()

gaps=''


def change_img_rock():
    imagel1.configure(image=pRock)
    imagel1.image = pRock
    computer_turn()
    who_win(pRock)


def change_img_gawi():
    imagel1.configure(image=pGawi)
    imagel1.image = pGawi
    computer_turn()
    who_win(pGawi)


def change_img_bo():
    imagel1.configure(image=pBo)
    imagel1.image = pBo
    computer_turn()
    who_win(pBo)


def computer_turn():
    global gaps
    gaps=random.choice([pBo,pGawi,pRock])
    imagel2.configure(image=gaps)
    imagel2.image = gaps


def who_win(user_p):
    if user_p==gaps:
        l3['text']='========\n비겼습니다!'
    elif (user_p==pRock and gaps==pGawi) or (user_p==pGawi and gaps==pBo) or (user_p==pBo and gaps==pRock):
        l3['text']='>>>>>>>\n이겼습니다!'
    else:
        l3['text']='X ㅡ X\n하찮은 패배자!'


pUser=PhotoImage(file="../assets/Lenna.png")
pCom=PhotoImage(file="../assets/CoinBack.gif")
pBo=PhotoImage(file="../assets/bo.png")
pGawi=PhotoImage(file="../assets/gawi.png")
pRock=PhotoImage(file="../assets/rock.png")

l1=Label(window,text='user')
l2=Label(window,text='computer')
l3=Label(window,font=('Times New Roman', 20, 'bold'))
imagel1=Label(window, image=pUser)
imagel2=Label(window, image=pCom)

l1.grid(row=0,column=0)
l2.grid(row=0,column=2)
l3.grid(row=1,column=1)
imagel1.grid(row=1,column=0)
imagel2.grid(row=1,column=2)

b1=Button(window,text="바위",command=change_img_rock)
b2=Button(window,text="가위",command=change_img_gawi)
b3=Button(window,text="보",command=change_img_bo)

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)


window.mainloop()
