#coding:utf-8
import tkinter
from tkinter import messagebox

def imc(mass, height):
    imc = mass/(height*height)
    if imc < 18.5:
        return "Underweight"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Overweight"
    elif 30 <= imc < 35:
        return "Obese"
    else:
        return "Extremley Obese"

def buttonFct(): 
    if not is_number(entMass.get()) or not is_number(entHeight.get()):
        messagebox.showerror("ERROR","You did not enter the correct values !")
    else:
        labRep.config(text=f"{imc(float(entMass.get()),float(entHeight.get()))}")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

app = tkinter.Tk()
app.geometry("300x260")

background = tkinter.PhotoImage(file = "back.png")
backLab = tkinter.Label(app, image=background)
backLab.place(x=0, y=0, relwidth=1, relheight=1)

labMass = tkinter.Label(app, text="Weight(kg)", font=("Courier", 24))
labMass.place(x=5, y=0)

entMass = tkinter.Entry(app, width=20)
entMass.place(x=5, y=50)

labHeight = tkinter.Label(app, text="Size(m)", font=("Courier", 24))
labHeight.place(x=5, y=75)

entHeight = tkinter.Entry(app, width=20)
entHeight.place(x=5, y=125)

but = tkinter.Button(app, text="Result", command=buttonFct, font=("Courier", 16))
but.place(x=5, y=160)

labRep = tkinter.Label(app, text="Response", font=("Courier", 24))
labRep.place(x=5, y=210)

app.mainloop()
