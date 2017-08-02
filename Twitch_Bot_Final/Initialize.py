"""This file contains the functions to connect to he chat"""

from cfg import CHANNEL
from utils import sendMessage

def loadingCompleted(line):
    """
    Return True if loading is complete and False otherwise. Don't use this function outside of this file
    :param line: message
    :return: Boolean
    """
    if ("End of /NAMES list" in line):  #end of line
        return False
    else:
        return True

def joinchat(s):
    """
    This function connects the Bot with the live chat
    :param s: Socket
    :return: None
    """
    readbuffer_join = "".encode()
    Loading = True
    while Loading:
        readbuffer_join = s.recv(1024)
        readbuffer_join = readbuffer_join.decode()
        temp = readbuffer_join.split("\n")
        readbuffer_join = readbuffer_join.encode()
        readbuffer_join = temp.pop()
        for line in temp:
            Loading = loadingCompleted(line)
    sendMessage(s, "Chat room joined! Hey everyone! Hope you are having a great day.")
    print("Bot has joined " + CHANNEL + " Channel!")

