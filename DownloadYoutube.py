import tkinter
from tkinter import *
import pytube
def download():
    url=str(x.get())
    pytube.YouTube(url).streams.get_highest_resolution().download()
page=tkinter.Tk()
x=Entry(page,width="50")
x.pack(side = LEFT)
b=Button(page,text="download",command=download,bg='lightblue')
#b.grid(row=1,column=0)
b.pack(side = LEFT)
page.mainloop()