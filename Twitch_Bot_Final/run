"""This file contains the GUI interdace to help user modify the databse"""

import database_sql
from tkinter import *

root = Tk() # create a Tk root window

w = 500 # width for the Tk root
h = 500 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
#title
title = Label(root, text = "TwitchBot Settings", padx = 2, pady = 2, bd = 2, fg = "red",
                  font=('arial', 20, 'bold'), width = 14, height = 1).grid(row = 0, column = 1)
empty_label = Label(root).grid(row = 1)  # empty row
#row 1
label_custom_command = Label(root, text = "Enter Command Keyword", padx = 2, pady = 2, bd = 2, fg = "black",
                  font=('arial', 10, 'bold'), width = 20, height = 1).grid(row = 2, column = 0)
user_entered_custom = StringVar()
label_user_entered_custom = Entry(root, textvariable = user_entered_custom)
label_user_entered_custom.grid(row = 2, column = 1)
#row 2
empty_label_2 = Label(root).grid(row = 3)
label_command = Label(root, text = "Enter Command", padx = 2, pady = 2, bd = 2, fg = "black",
                  font=('arial', 10, 'bold'), width = 20, height = 1).grid(row = 4, column = 0)
user_entered_command = StringVar()
label_user_entered_custom = Entry(root, textvariable = user_entered_command)
label_user_entered_custom.grid(row = 4, column = 1)

#enter command to database button
empty_label_2 = Label(root).grid(row = 5)
button = Button(root, text = "Enter to Database", padx = 2, pady = 2, bd = 2, fg = "black",
                  font=('arial', 10, 'bold'), width = 20, height = 1, command = lambda: database_sql.add_command(user_entered_custom.get(), user_entered_command.get())).grid(row = 6, column = 1)

root.mainloop() # starts the mainloop