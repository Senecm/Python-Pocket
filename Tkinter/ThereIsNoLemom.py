from tkinter import *

win = Tk()
win.geometry("500x500") #setting the dimesions of the window
win.title("Lemon Machine") #title of the application

lbl = Label(win, text="big", font=("Arial Bold", 50)) #label
lbl.grid(column=0, row=0) #giving label a location

def OnClick(): #button1
    lbl.configure(text="I SAID DONT CLICK", font=("Comic Sans MS", 35))
    lbla = Label(win, text="Write an apology, NOW!", font=("Times New Roman (Times)", 20))
    lbla.grid(column=0, row=2)
    txt = Entry(win, width=50) #creating a text box
    txt.grid(column=0, row=4)
    APO = txt.get() 
    btna = Button(win, text="Send Apology :)", command=SendApo)
    btna.grid(column=0, row=6)
    return APO

def SendApo(): #button2
    lblb = Label(win, text=APO)
    lblb.grid(column=0, row=5)

btn = Button(win, text="Don't Click", bg="yellow", fg="green", command=OnClick) #fg = forground bg = background
btn.grid(column=0, row=1)

win.mainloop()