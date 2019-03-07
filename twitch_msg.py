import socket, string

# Set all the variables necessary to connect to Twitch IRC
HOST = "irc.twitch.tv"
NICK = "USERNAME"
PORT = 6667
PASS = "TWITCH OAUTH"
readbuffer = ""
MODT = False

# Connecting to Twitch IRC by passing credentials and joining a certain channel
s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS " + PASS + "\r\n")
s.send("NICK " + NICK + "\r\n")

message = "Sample Message"

channel = {
	'$Channels you want to message',
  '$Another Channel You want to MSG'
    }

for i in channel:
    s.send("JOIN " + i + "\r\n")
    s.send("PRIVMSG #" + i + " :" + message + "\r\n")
