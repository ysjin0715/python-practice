from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

window = Tk()
window.title('notepad')
text = Text(window, height = 40, width = 60)
text.pack()


def save():
   file = filedialog.asksaveasfile(parent=window, mode = 'w')
   if file != None:
      line = text.get('1.0',END+'-1c')           # text에 저장된 내용을 가져올 때 '첫번째 줄 0번째 문자부터' '마지막에서 1글자를 뺀 나머지까지' 가져오라는 뜻이다
      file.write(line)
      file.close()
      print('파일 저장이 완료되었습니다!')


def open():
   file = filedialog.askopenfile(parent = window, mode = 'r')
   if file != None:
      line = file.read()
      text.insert('1.0',line)
      file.close()


def exit():
   if messagebox.askokcancel('Quit','종료하시겠습니까?'):
      window.destroy()


def about():
   label = messagebox.showinfo('About','tkinter is very ...')


menu = Menu(window)
window.config (menu = menu)
filemenu = Menu(menu)
menu.add_cascade(label = '파일',menu=filemenu)
filemenu.add_command (label = '열기',command=open)
filemenu.add_command (label='저장하기',command=save)
filemenu.add_command (label = '종료',command=exit)

helpmenu = Menu(menu)
menu.add_cascade(label = '도움말',menu = helpmenu)
helpmenu.add_command(label = '프로그램 정보',command = about)
window.mainloop()