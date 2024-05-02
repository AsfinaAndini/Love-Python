from tkinter import *
import random
root = Tk()
# Defining the size, width=400, height=240
root.geometry('400x240')
# Title 
root.title('Love Calculator❤️❤️')

def calculate_love():
    # value will contain digits between 0-9
    st = '0123456789'
    # result will be in double digits
    digit = 2
    temp = "".join(random.sample(st, digit))
    result.config(text=temp)

# Heading on Top
heading = Label(root, text='Love Calculator????')
heading.pack()

