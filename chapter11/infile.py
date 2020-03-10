# 파일 대화상자 만드릭
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

readfile = askopenfilename()
if( readfile != None):
   infile = open(readFile, 'r')

for line in infile.readlines():
   line = line.strip()
   print(line)

infile.close()