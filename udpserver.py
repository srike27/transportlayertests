import socket
import random
import pickle
import csv
import time

localIP     = "192.168.1.6"

localPort   = 20001

bufferSize  = 1024

counter = 0
complete = 3600

msgFromServer       = "Hello UDP Client"

bytesToSend         = str.encode(msgFromServer)

start_time = time.time()
abs_start_time = start_time
print(start_time)

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

 

print("UDP server up and listening")

 

# Listen for incoming datagrams

while(True):
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
    list = [f0,f1,f2,f3,f4,f5,f6,f7,i1,i2,i3,counter]
    payload = pickle.dumps(list)
    counter = counter + 1
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]
    msg = message
    msg = pickle.loads(msg)
    
    with open('datarxfrobot.csv', 'a', newline='') as csv_1:
        csv_out = csv.writer(csv_1)
        csv_out.writerow(msg)
    with open('datatxfserver.csv', 'a', newline='') as csv_2:
        csv_out = csv.writer(csv_2)
        csv_out.writerow(list)
    print(msg)
    
    

    # Sending a reply to client

    UDPServerSocket.sendto(payload, address)
    if counter == complete:
        end_time = time.time()
        print(end_time)
        exit()