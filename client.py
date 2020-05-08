import cv2
import numpy as np
import socket
import sys
import pickle
import struct ### new code
import json


tail = "{ 'client':{ 'name' : '89998394668', 'version' : '0.01', 'to' : '89998394667' } }"

cap=cv2.VideoCapture(1)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('localhost',8088))
while True:
    ret,frame=cap.read()
    data = pickle.dumps(frame) ### new code
    clientsocket.sendall(struct.pack("L", len(data))+data) ### new code