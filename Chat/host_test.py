import socket
import threading

#---------------------------------------------------#
#---------INITIALIZE CONNECTION VARIABLES-----------#
#---------------------------------------------------#
#Initiate socket and bind port to host PC
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostname()
PORT = 8011
conn = ''
s.bind((HOST, PORT))

#---------------------------------------------------#
#----------------CONNECTION MANAGEMENT--------------#
#---------------------------------------------------#
def GetConnected():
    s.listen(1)
    global conn
    conn, addr = s.accept()
    
    while 1:
        try:
            data = conn.recv(1024)
            print(data)
            print('notificacao')
        except:
            print('parceiro desconectou')
            GetConnected()

    conn.close()
    
t = threading.Thread(target=GetConnected)
t.start()
