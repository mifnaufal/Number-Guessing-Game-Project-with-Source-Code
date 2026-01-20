import tkinter as tk
from tkinter import *
import random

win = tk.Tk()
win.geometry("750x750")
win.title("PythonGeeks")

num = random.randint(1, 50)
hint = StringVar()
score = IntVar()
final_score = IntVar()
guess = IntVar()

score.set(5)
final_score.set(score.get())
hint.set("Guess a number between 1 to 50")

def fun():
    if score.get() <= 0:
        hint.set("Game Over You Lost")
        return

    x = guess.get()

    if x > 50 or x < 1:
        hint.set("Out of range. You lost 1 chance.")
        score.set(score.get() - 1)

    elif num == x:
        hint.set("Congratulations, YOU WON!")
        
    elif num > x:
        hint.set("Your guess is too low. Guess higher.")
        score.set(score.get() - 1)

    elif num < x:
        hint.set("Your guess is too high. Guess lower.")
        score.set(score.get() - 1)

    final_score.set(score.get())

Entry(win, textvariable=guess, width=3, font=('Ubuntu', 50), relief=GROOVE).place(relx=0.5, rely=0.3, anchor=CENTER)
Entry(win, textvariable=hint, width=50, font=('Courier',15), relief=GROOVE, bg='orange').place(relx=0.5, rely=0.7, anchor=CENTER)
Entry(win, textvariable=final_score, width=2, font=('Ubuntu', 24), relief=GROOVE).place(relx=0.61, rely=0.85, anchor=CENTER)

Label(win, text='I challenge you to guess the number', font=("Courier", 25)).place(relx=0.5, rely=0.09, anchor=CENTER)
Label(win, text='Score out of 5', font=("Courier", 25)).place(relx=0.3, rely=0.85, anchor=CENTER)

Button(win, width=8, text='CHECK', font=('Courier', 25), command=fun, relief=GROOVE, bg='light blue').place(relx=0.5, rely=0.5, anchor=CENTER)

win.mainloop()
