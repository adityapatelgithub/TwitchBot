"""This file was used to create a database and a table of commands. It contains functions to
interact with the database"""

import sqlite3

conn = sqlite3.connect('Commands.db')

c = conn.cursor()

# code below was used to create a table with two columns: Custom_Command, Reply text
# c.execute("""CREATE TABLE commands (
#            Custom_Command text,
#            Reply text)""")

#c.execute("INSERT INTO commands VALUES ('!!goodmorning', 'Good Morning! Hope you have a great Day')")
def get_command(cmd):
    """
    Return the command accociated with given keyword
    :param cmd: keyword
    :return: command associated with this keyword
    """
    with conn:
        c.execute("SELECT * FROM commands WHERE Custom_Command = ?", (cmd,))
        my_list = c.fetchall()
        if len(my_list) == 0:
            return False
        return my_list[0][1]

def add_command(cmd, text):
    """
    Add the keyword and command to the database
    :param cmd: keyword
    :text: command associated with this keyword
    :return: None
    """
    with conn:
        c.execute("SELECT * FROM commands WHERE Custom_Command = ?", (cmd,))
        my_list = c.fetchall()
        if len(my_list) == 0:
            c.execute("INSERT INTO commands VALUES (?, ?)", (cmd, text))
        else:
            c.execute("DELETE FROM commands WHERE Custom_Command = ?", (cmd,))
            c.execute("INSERT INTO commands VALUES (?, ?)", (cmd, text))

def delete_command(cmd):
    """
    Return the command accociated with given keyword
    :param cmd: keyword
    :return: command associated with this keyword
    """
    with conn:
        c.execute("DELETE FROM commands WHERE Custom_Command = ?", (cmd,))

def list_command():
    """
    :return: A dictionary of keyword: command pairs.
    """
    c.execute("SELECT * FROM commands")
    my_list = c.fetchall()
    return dict(my_list)

conn.commit()

