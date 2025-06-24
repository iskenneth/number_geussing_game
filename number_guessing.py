#Pick a random number 1 to 10
import random
import tkinter as tk 
#Ask player to guess a number
class NumberGuessing:
    def __init__(self, master):
        self.master = master
        master.title("Number Guessing Game")

        self.number = random.randint(1,10)
