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
