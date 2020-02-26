import tkinter

mycolor='blue'


def paint(event):
    x1,y1=(event.x),(event.y)
    x2,y2=(event.x),(event.y)
    canvas.create_oval(x1, y1, x2, y2, fill=mycolor)


def change_color():
    global mycolor
    mycolor="red"


window=tkinter.Tk()
canvas=tkinter.Canvas(window)
canvas.pack()
canvas.bind("<B1-Motion>",paint)
button=tkinter.Button(window,text="빨간색",command=change_color)
button.pack()
print(mycolor)
window.mainloop()
