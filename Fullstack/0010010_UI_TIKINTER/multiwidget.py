from tkinter import *

window = Tk()

def convert():
    print(e1_value.get())
    grams = float(e1_value.get()) * 1000
    pounts = float(e1_value.get()) * 2.3
    ounces = float(e1_value.get()) * 35.7

    t1.insert(END, grams)
    t2.insert(END, pounts)
    t3.insert(END, ounces)


 

e0 =Label(window , text= "Kg" ,height =1, width= 10)
e0.grid(row=0, column = 0) 

e1_value=StringVar()
e1 =Entry(window , textvariable= e1_value)
e1.grid(row=0, column = 1)   

b1 = Button(window, text="Convert" , command = convert )
b1.grid(row=0, column = 2)


t1 =Text(window , height =1, width= 10)
t1.grid(row=1, column = 0)

t2 =Text(window , height =1, width= 10)
t2.grid(row=1, column = 1)

t3 =Text(window , height =1, width= 10)
t3.grid(row=1, column = 2)






window.mainloop()