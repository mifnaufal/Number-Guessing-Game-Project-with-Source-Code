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
