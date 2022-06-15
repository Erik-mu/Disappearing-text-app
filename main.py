import tkinter as tk

def countdown(time):
    if time == -1:
        window.destroy()
    else:
         window.after(1000, countdown, time-1)


from tkinter import *
window = Tk()
text = []
def timer(count):
    if count > 0:
        time = window.after(1000, timer, count-1)
    timer_label.config(text=count)


def read():
    txt = user_label.get()
    window.after(100, read)
    user_label.delete(0, END)
    text.append(txt)
    text_ = "".join(text)
    text_label.config(text=text_)
    if len(txt) == 0:
        countdown(5)


window.title("Self destroying app")
window.geometry("500x350")
timer_label = Label(text="")
timer_label.grid(column=0, row=0)
title_label = Label(text="When you stop typing you lose your work", font =("Courier", 14))
title_label.grid(column=0, row=1)
text_label = Label(text="", font =("Courier", 14))
text_label.grid(column=0, row=3)
user_label = Entry(width=80)
user_label.grid(column=0, row=2, columnspan=2)
user_words_label = Label(text="")
window.after(0, read)
window.mainloop()
