"""The main file of this project"""

from utils import sendMessage, Console, getUser, getMessage
from Initialize import joinchat
from Socket import openSocket
from database_sql import *



def main():
    """
    Main function of this project!!! Respond to chat messages and ban users
    """
    s = openSocket()   #call opensocket function
    joinchat(s)        #join chat
    readbuffer = ""
    commands = list_command()    #get a dictionary of custom commands stored in  database

    while True:
        readbuffer = s.recv(1024)
        readbuffer = readbuffer.decode()
        temp = readbuffer.split("\n")
        readbuffer = readbuffer.encode()
        readbuffer = temp.pop()
        for line in temp:
            print(line)
            if line == "":      #if there is nothing, break
                break
            # So twitch doesn't timeout the bot.
            if "PING" in line and Console(line):        #respond to ping message with a pong message
                msgg = "PONG tmi.twitch.tv\r\n".encode()
                s.send(msgg)
                print(msgg)
                break
            # get user
            user = getUser(line)    #get username
            # get message send by user
            message = getMessage(line)    #get password
            # for you to see the chat from CMD
            print(user + " > " + message)    #doesn't print in the chat!
            # sends private msg to the user (start line)
            PMSG = "/w " + user + " "
            # commands below
            for i in commands:   # parse dicctionary of custom commands
                if i in message:   # check if user typed custon command
                    sendMessage(s, commands[i])
if __name__ == '__main__':
    main()