import socket
import pickle
import time 
import random
import csv


msgFromClient       = "Hello UDP Server"

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("192.168.1.6", 20001)

bufferSize          = 1024
counter = 0
complete = 3600
 

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
start_time = time.time()
abs_start_time = start_time
print(start_time)

while True:
    current_time = time.time()
    
    elapsed_time = current_time - start_time
    if elapsed_time > 0.05:
        f1 = random.random()
        f2 = random.random()
        f3 = random.random()
        f4 = random.random()
        f5 = random.random()
        f6 = random.random()
        f7 = random.random()
        f0 = random.random()
        i0 =  random.randint(-32000, 32000)
        i1 =  random.randint(-32000, 32000)
        i2 =  random.randint(-32000, 32000)
        i3 =  random.randint(-32000, 32000)
        i4 =  random.randint(-32000, 32000)
        i5 =  random.randint(-32000, 32000)
        list = [f0,f1,f2,f3,f4,i0,i1,i2,i3,i4,counter]
        payload = pickle.dumps(list)
        counter = counter + 1
        start_time = current_time
        UDPClientSocket.sendto(payload, serverAddressPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        msg = msgFromServer[0]
        msg = pickle.loads(msg)
        with open('datatxfrobot.csv', 'a', newline='') as csv_1:
            csv_out = csv.writer(csv_1)
            csv_out.writerow(msg)
        with open('datarxfserver.csv', 'a', newline='') as csv_2:
            csv_out = csv.writer(csv_2)
            csv_out.writerow(list)
        print(msg)
    if counter == complete:
        end_time = time.time()
        print(end_time)
        exit()

"""
172.105.35.19
"""