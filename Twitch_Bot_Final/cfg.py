"""This file contains configuration for the bot"""

###Don't edit these:

SERVER = "irc.twitch.tv"  # server (Twitch)
PORT = 6667  # port for Twitch
PASS = "oauth:znua6mmf0pn8fle5zltqd7vd1pqtbk"  # bot password can be found on https://twitchapps.com/tmi/
BOT = "pythonbot_2"  # Bot's name [NO CAPITALS]
OWNER = "aditya_patel"  # Owner's name [NO CAPITALS]

file = open('channel.txt', 'r').readlines()
chan = file[0]

CHANNEL = chan.lower()  # Channal name [NO CAPITALS]
