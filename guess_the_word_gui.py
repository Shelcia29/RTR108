from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import time

global score 
score = {}

def draw():
	global root	
	root = Tk()
	root.title('Guess The Word! (by Shelcia Carolyns)')
	root.geometry("400x180")
	root.resizable(False, False)
	img = PhotoImage(file='mainimg.png')
	root.tk.call('wm', 'iconphoto', root._w, img)


def place_gui():
	global btn_start, btn_score, btn_help, lbl_word, enter_word, btn_check
	btn_start = Button(root, text="Start!", width = 12, activebackground = "#0091ff", activeforeground = "white", command = lambda: start())
	btn_score = Button(root, text="Score!", width = 12, activebackground = "#0091ff", activeforeground = "white", command = lambda: display_score(score))
	btn_help = Button(root, text="Help", width = 12, activebackground = "#0091ff", activeforeground = "white", command = lambda: help())
	lbl_word = Label(root, width = 15, height = 1, text = "Your Word Here!", font=("Courier", 20), bg= "white")
	enter_word = tk.Text(root, width = 20, height = 1, font=("Courier", 20), state = NORMAL)
	btn_check = Button(root, text="Check my letter!", width = 12, activebackground = "#0091ff", activeforeground = "white", command = lambda: check())
	
def griding():
	btn_start.grid(column = 0, row = 1, padx = 4, pady = 4)
	btn_score.grid(column = 1, row = 1, padx = 4, pady = 4)
	btn_help.grid(column = 2, row = 1, padx = 4, pady = 4)
	lbl_word.grid(columnspan = 3, row = 2, pady = 10, sticky ="NSWE")
	enter_word.grid(columnspan = 3, row = 3, sticky = "NSWE", padx = 6, pady = 5)
	btn_check.grid(row = 4, sticky = "N", padx = 2, pady = 2, columnspan = 3,)

def get_word():
	words = ["APPLE", "GREEN", "IORN MAN", "PYTHON"]
	return random.choice(words)

def start():
	global word, _try, name
	name = enter_word.get("1.0", END)
	name = name.rstrip()
	enter_word.delete("1.0", END)
	word = get_word()
	lbl_word.config(text = len(word) * "_ ")
	_try = len(word)
	enter_score(score, name)

def enter_score(dict, key):
	if key in dict:
		return
	else:
		dict[name] = 0
	print(dict)
	

def check():
	global _try	
	if _try == 0:
		lbl_word.config(text = "You Lost :(")
	else:
		user = []
		user_word = enter_word.get("1.0", END)
		user_word = user_word.rstrip()
		if word == user_word:
			lbl_word.config(text = "Correct guess! (Start):)")
			enter_word.delete("1.0", END)
			scoree = score[name]
			scoree = scoree + 1
			score.update({name : scoree})
		else:
			scoree = score[name]
			scoree = scoree - 1
			score.update({name : scoree})
			lbl_word.config(text = "Try again!")
			enter_word.delete("1.0", END)
			root.update()
			time.sleep(2)
			lbl_word.config(text = len(word) * "_ ")
		_try = _try - 1

def help():
	messagebox.showinfo("Help", "How to play this game!\n 1) Enter your name in the text box given\n 2) Click on Start each time you need a new word to guess\n 3) Type in the word you guess\n 4) Check your guess\n 5) You only get as much moves as the number of leeters in the word you are guessing\n 6) You get -1 for each failed attempts and +1 for sucessfull attempts.\n Best of luck :) \n By Shelcia")

def display_score(dict):
	for key,value in dict.items():
		messagebox.showinfo("Scores", "Name : {} Totol : {}".format(key, value))

draw()
place_gui()
griding()
root.mainloop()
