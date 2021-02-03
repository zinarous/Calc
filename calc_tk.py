from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import math
import sys

root = Tk() 
root.title("Калькулятор")
root.configure(bg="lightblue")
root.resizable(width=False, height=False)
root.geometry('310x300')

path = "Apps-Calc-icon.png"
img = ImageTk.PhotoImage(Image.open(path))

btns = [
"7", "8", "9", "÷", "C", 
"4", "5", "6", "×", "±",
"1", "2", "3", "-", "xⁿ",
"0", ".", "=", "+", "Exit",
"e", "π", "sin", "cos",
"n!", "(", ")","√2", ]


r = 1
c = 0
for i in btns:
    rel = ""
    cmd=lambda x=i: calc(x)
    top_padding = 5
    btn = Button(root, text=i, command = cmd, width = 7, height = 2, bg="white")
    btn.grid(row = r, column = c, pady=2, padx = 1, sticky = E)
    c += 1
    if c > 4:
        c = 0
        r += 1

calc_entry = Entry(root, width = 50, justify = RIGHT)
calc_entry.grid(row=0, column=0, columnspan=5, pady = 2, padx = 3)

#логика калькулятора
def calc(key):
    if key == "=":
#исключение написания слов
        str1 = "-+0123456789.×÷)(" 
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "Это не выглядит как число, введи число!")
            messagebox.showerror("ОШИБКА!!!", "Это не является числом!")
#исчисления
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")

    #очищение поля ввода
    elif key == "C":
        calc_entry.delete(0, END)
        
    elif key == "×":
        calc_entry.insert(END, "*")

    elif key == "÷":
        calc_entry.insert(END, "/")    

    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass

    elif key == "π":
        calc_entry.insert(END, math.pi)

    elif key == "e":
        calc_entry.insert(END, math.e)

    elif key == "Exit":
        root.after(1,root.destroy)
        sys.exit

    elif key == "xⁿ":
        calc_entry.insert(END, "**")

    elif key == "sin":
        calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))
    elif key == "cos":
        calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))

    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")

    elif key == "n!":
        calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))

    elif key == "√2":
        calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))
        
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

root.mainloop()