"""This file contains utility functions to send messages and parse received messages"""

from cfg import CHANNEL

def sendMessage(s, message):
    """
    This function sends message to the chat
    :param s: Socket
    :param message: Message to send
    :return: None
    """
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send((messageTemp + "\r\n").encode())

def Console(line):
    """
    This function returns True if the message was sent by Twitch and False if the message was sent by user
    :param line: Message
    :return: Boolean
    """
    if "PRIVMSG" in line:
        return False
    else:
        return True

def getUser(line):
    """
    This function gets the name of the user
    :param line: Message
    :return: Name of User
    """
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user


def getMessage(line):
    """
    This function returns the message sent by the user
    :param line: message
    :return: the message sent by the user
    """
    global message
    try:
        separate = line.split(":", 2)
        message = separate[2]
    except:
        message = ""
    return message



