import threading
import socket
import pickle
import time 
import random
import csv

global start_time_threaded1
global start_time_thread2
start_time_thread1 = time.time()
start_time_thread2 = time.time()
current_time_thread1 = time.time()
current_time_thread2 = time.time()
absstarttime = time.time()
elapsed_time_thread1 = current_time_thread1 - start_time_thread1
elapsed_time_thread2 = current_time_thread2 - start_time_thread2
global counter
HOST = '192.168.1.6'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
global server_socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))
global conn
global addr
counter = 0

"""
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
"""
    

def rx():
    while True:
        #print("thread1")
        global start_time_thread1
        global client_address
        global counter
        current_time_thread1 = time.time()
        elapsed_time_thread1 = current_time_thread1 - start_time_thread1
        if(elapsed_time_thread1 > 0.05):
            #receive data here
            message = conn.recv(1024)
            msg = message
            msg = pickle.loads(msg)
            #print(msg)
            with open('datatcprxfrobot.csv', 'a', newline='') as csv_1:
                csv_out = csv.writer(csv_1)
                csv_out.writerow(msg)
            start_time_thread1 = time.time()
        

def tx():
    while True:
        #print("thread2")
        global client_address
        global counter
        global start_time_thread2
        current_time_thread2 = time.time()
        elapsed_time_thread2 = current_time_thread2 - start_time_thread2
        if(elapsed_time_thread2 > 0.05):
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
            try:
                #send data here
                conn.sendall(payload)
                counter = counter + 1
                with open('datatcptxfserver.csv', 'a', newline='') as csv_2:
                    csv_out = csv.writer(csv_2)
                    csv_out.writerow(list)
                start_time_thread2 = time.time()
            except Exception as e:
                print(e)
        
        
try:
    print("Waiting for client")
    server_socket.listen()
    conn, addr = server_socket.accept()
    print("Client connected")

    t1 = threading.Thread(target = rx)
    t2 = threading.Thread(target = tx)
    # starting threads
    t1.start()
    t2.start()

except:
    print("Unable to open threads")

while(True):
    curtime = time.time()
    etime = curtime - absstarttime
    if(etime > 1800):
        exit()
