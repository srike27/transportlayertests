import threading
import socket
import pickle
import time 
import random
import csv

serverAddressPort   = ("192.168.1.6", 20001)
bufferSize          = 1024
global counter
counter = 0
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
global start_time_thread1
global start_time_thread2
start_time_thread1 = time.time()
start_time_thread2 = time.time()
current_time_thread1 = time.time()
current_time_thread2 = time.time()
elapsed_time_thread1 = current_time_thread1 - start_time_thread1
elapsed_time_thread2 = current_time_thread2 - start_time_thread2

def rx():
    while True:
        global counter
        global start_time_thread1
        #print("thread1")
        current_time_thread1 = time.time()
        elapsed_time_thread1 = current_time_thread1 - start_time_thread1
        if(elapsed_time_thread1 > 0.05):
            #
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
            msg = msgFromServer[0]
            msg = pickle.loads(msg)
            with open('datarxfserver.csv', 'a', newline='') as csv_2:
                csv_out = csv.writer(csv_2)
                csv_out.writerow(msg)
            print(msg)
            start_time_thread1 = time.time()

def tx():
    while True:
        global counter
        global start_time_thread2
        #print("thread2")
        current_time_thread2 = time.time()
        elapsed_time_thread2 = current_time_thread2 - start_time_thread2
        if(elapsed_time_thread2 > 0.05):
            #
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
            UDPClientSocket.sendto(payload, serverAddressPort)
            with open('datatxfrobot.csv', 'a', newline='') as csv_1:
                csv_out = csv.writer(csv_1)
                csv_out.writerow(list)
            start_time_thread2 = time.time()

try:
    t1 = threading.Thread(target = rx)
    t2 = threading.Thread(target = tx)
    # starting threads
    t1.start()
    t2.start()

except:
    print("Unable to open threads")

while(True):
    pass