import tkinter as tk
from Message import enc
from tkinter import *
window = tk.Tk()
window.title("S-Des Encryption")

def run():
    Data1=Enter1.get()
    Data2=Enter2.get()
    label33['text']=f"{enc(Data1,Data2)}"

label1=tk.Label(window, text="Plain text: ").grid(row=0,column=0)
Enter1=tk.Entry(window, bd =5)
Enter1.grid(row=0,column=1)
#Data1=Enter1.get()
label2=tk.Label(window, text="Key: ").grid(row=2,column=0)
Enter2=tk.Entry(window, bd =5)
Enter2.grid(row=2,column=1)
#Data2=Enter2.get()
label33=tk.Label(window, text="the Output: ")
label33.grid(row=4,column=0)
label33=tk.Label(window, text="")
label33.grid(row=4,column=1)
Data3=Enter1.get()
#############
label3=tk.Label(window, text="Plain text").grid(row=6,column=0)
Enter3=tk.Entry(window, bd =5)
Enter3.grid(row=6,column=1)
Data3=Enter1.get()
label4=tk.Label(window, text="Decrypt").grid(row=8,column=0)
Enter4=tk.Entry(window, bd =5)
Enter4.grid(row=8,column=1)
button=Button(window, text="Encrypt", command=run)
button.grid(row=9,column=0)
Data4=Enter2.get()


window.mainloop()