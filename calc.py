from tkinter import *
rt = Tk()
rt.title("Calculator")
rt.geometry("264x200")
rt.configure(bg="lightblue")
rt.resizable(width=False, height=False)
input = Text(rt, width=32, height=2, font="arial 11")
input.grid(row=1, column=0, columnspan=4)
class App:
    def __init__(self, master):
        self.master = master
    def add():
        input.insert(END, "+")
    def sub():
        input.insert(END, "-")
    def amp():
        input.insert(END, "*")
    def div():
        input.insert(END, "/")
    def n0():
        input.insert(END, "0")
    def n1():
        input.insert(END, "1")
    def n2():
        input.insert(END, "2")
    def n3():
        input.insert(END, "3")
    def n4():
        input.insert(END, "4")
    def n5():
        input.insert(END, "5")
    def n6():
        input.insert(END, "6")
    def n7():
        input.insert(END, "7")
    def n8():
        input.insert(END, "8")
    def n9():
        input.insert(END, "9")
    def clear():
        input.delete("1.0", END)
    cl = clear()
    def eq():
        txt = input.get("1.0", END)
        cl = ""
        input.insert(END, eval(txt))
    b0 = Button(rt, bg="pink", text="0", width=8, height=2, command=n0)
    b1 = Button(rt, bg="pink", text="1", width=8, height=2, command=n1)
    b2 = Button(rt, bg="pink", text="2", width=8, height=2, command=n2)
    b3 = Button(rt, bg="pink", text="3", width=8, height=2, command=n3)
    b4 = Button(rt, bg="pink", text="4", width=8, height=2, command=n4)
    b5 = Button(rt, bg="pink", text="5", width=8, height=2, command=n5)
    b6 = Button(rt, bg="pink", text="6", width=8, height=2, command=n6)
    b7 = Button(rt, bg="pink", text="7", width=8, height=2, command=n7)
    b8 = Button(rt, bg="pink", text="8", width=8, height=2, command=n8)
    b9 = Button(rt, bg="pink", text="9", width=8, height=2, command=n9)
    add = Button(rt, bg="pink", text="+", width=8, height=2, command=add)
    sub = Button(rt, bg="pink", text="-", width=8, height=2, command=sub)
    amp = Button(rt, bg="pink", text="*", width=8, height=2, command=amp)
    div = Button(rt, bg="pink", text="/", width=8, height=2, command=div)
    eq = Button(rt, bg="pink", text="=", width=8, height=2, command=eq)
    c = Button(rt, bg="pink", text="C", width=8, height=2, command=clear)
    b0.grid(row=5, column=1)
    b1.grid(row=4, column=0)
    b2.grid(row=4, column=1)
    b3.grid(row=4, column=2)
    b4.grid(row=3, column=0)
    b5.grid(row=3, column=1)
    b6.grid(row=3, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)
    add.grid(row=2, column=3)
    sub.grid(row=3, column=3)
    amp.grid(row=4, column=3)
    div.grid(row=5, column=3)
    eq.grid(row=5, column=2)
    c.grid(row=5, column=0)
rt.mainloop()