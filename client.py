import cv2
import numpy as np
import socket
import sys
import pickle
import struct
#import smbus

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('192.168.137.1', 8000))
#bus = smbus.SMBus(1)
#address = 0x04
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    data = pickle.dumps(frame)
    clientsocket.sendall(struct.pack("=L", len(data)) + data)
    
    bufsize = 1024  # 指定要接收的數據大小
    data_recieve = clientsocket.recv(bufsize)  # 接收遠端主機傳來的數據
    print(data_recieve)
    if (data_recieve) == b'hi':
        print(data_recieve)
    