"""This file contains the function to return socket connectiob object"""

import socket
from cfg import SERVER, PORT, PASS, BOT, CHANNEL

def openSocket():
    """
    This function creates a socket object
    :return: Socket object
    """
    s_prep = socket.socket()
    s_prep.connect((SERVER, PORT))
    s_prep.send(("PASS " + PASS + "\r\n").encode())         #endocde() converts byte to string
    s_prep.send(("NICK " + BOT + "\r\n").encode())
    s_prep.send(("JOIN #" + CHANNEL + "\r\n").encode())
    return s_prep