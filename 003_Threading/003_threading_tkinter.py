#!/usr/bin/env python3
# -*- coding: UTF-8 -*-



'''

Thread Beispiel 

'''



##############################################################################################
#
# 				import modules
#
##############################################################################################

import tkinter as tk
import time
from random import randint
import threading



##############################################################################################
#
# 				functions
#
##############################################################################################

def five_seconds():
	print('five_seconds started')
	my_button1.configure(state='disabled')
	my_label1.configure(text='thread is running')
	time.sleep(5)
	my_label1.configure(text='thread is not running')
	
	my_button1.configure(state='normal')
	return()
	
def start_thread1():
	print('thread started')
	threading.Thread(target=five_seconds).start()
	return()

def random_number():
	number = randint(0,100)
	my_label2.configure(text=f'Random number: {number}')
	return()



##############################################################################################
#
# 				tkinter  GUI
#
##############################################################################################

# tkinter window
root = tk.Tk()
root.title("Counting Seconds")
root.geometry('500x400')



# tkinter widgets 
a = 100
my_label1	=	tk.Label(root, text='thread is not running')
my_label2	=	tk.Label(root, text='Random number:')

my_button1	=	tk.Button(root, text='Start_Threading_5 secs', command=start_thread1)
my_button2	=	tk.Button(root, text='get random', command=random_number)

# tkinter widget grid
my_label1.grid(		row=0, column=0, padx=5, pady=5)
my_button1.grid(	row=1, column=0, padx=5, pady=5)
my_button2.grid(	row=2, column=0, padx=5, pady=5)
my_label2.grid(		row=2, column=1, padx=5, pady=5)



##############################################################################################
#
# 				Main
#
##############################################################################################

root.mainloop()

