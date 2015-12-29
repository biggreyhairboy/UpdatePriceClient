from socket import *
from WindPy import w
from datetime import *

w.start()
host = '128.199.165.107'
port = 9001
bufsize = 1024
addr = (host,port)
client = socket(AF_INET,SOCK_STREAM)
client.connect(addr)
while True:
    #data = input("price: ")
    data = w.wsq("AG1606.SHF", "rt_last")
    #print data
    realtimeprice = data.Data[0][0]
    print realtimeprice
    print('\r\n')
    if not data or data=='exit':
        break
    client.send('%s\r\n' % realtimeprice)
    data = client.recv(bufsize)
    if not data:
        break
client.close()
