#Pick a random number 1 to 10
import random
import tkinter as tk 
#Ask player to guess a number
class NumberGuessing:
    def __init__(self, master):
        self.master = master
        master.title("Number Guessing Game")

        self.number = random.randint(1,10)

        self.laber = tk.labe(master, text="Input a number from 1-10:")
        self.label.pack()
        self entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(master, text="Prediction", command=self.guess_right)
        self.guess_button.pack()
        self.feedback = tk.label (master, text+"")
        self.feedback.pack()
        self.play_again_button = tk.Button(master, text="Play Again", command=self.play_again)
        self.play_again_button.pack()
        self.play_again_button.config(state="disabled")
    def guess_checker(self): 
        try:
            guess + int(self.entry.get())
        except ValueError:
            self.feedback.config(text="Please enter a valid number!")
            return
        if guess == self.number:
            self.feedback.config(text="Correct!")
            self.guess_button.config(state="disabled")
            self.play_again_button.config(state="normal")
        elif guess < self.number:
            self.feedback.config(text="Taas pa onti!")
        else:
            self.feedback.config(text="babaan mo lang!")
    def isa_pa(self):
                
        
        