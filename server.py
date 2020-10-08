import socket
import sys
import cv2
import pickle
import struct

HOST = '192.168.137.1'
PORT = 8000

while True:
    
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')
    s.bind((HOST, PORT))
    print('Socket bind complete')
    s.listen(5)
    print('Socket now listening')
    if break_flag == 1:
        print("ending")
        break
    conn, addr = s.accept()
    print("connected")

    

    while True:
       
        serverMessage = 'Hi'
        conn.send(serverMessage.encode(encoding = "gb2312"))
        
        data = b''
        payload_size = struct.calcsize("=L")

        while len(data) < payload_size:
            data += conn.recv(4096)
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]

        while len(data) < msg_size:
            data += conn.recv(4096)
        frame_data = data[:msg_size]
        data = data[msg_size:]

        frame_read=pickle.loads(frame_data)
        frame = cv2.cvtColor(frame_read, cv2.COLOR_BGR2RGB)

        cv2.imshow("frame", frame)
        cv2.waitKey(1)
    
conn.close()
