import cv2
import socket
import sys
import pickle
import struct 
import json
import numpy as np
import base64 
import time
import json

def encode_to_string(img, img_format='.jpg'):
	'''encode uint8 image to byte string'''
	return cv2.imencode(img_format, img)[1].tobytes()



def decode_to_img(string):
	return cv2.imdecode(np.fromstring(string, np.uint8),cv2.IMREAD_COLOR)


HOST=''
PORT=8090

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')



s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn,addr=s.accept()

connectors = []

def check_user_and_add(iduser, connection):
	if len(connectors) > 0:
		for x in connectors:
			if x.keys()[0] == iduser:
				x[iduser] = connection 
			else:
				user = {iduser : connection}
				connectors.append(user)
	else:
		user = {iduser : connection}
		connectors.append(user)
		
	print(connectors)

def get_opponent(iduser):
	if len(connectors) > 0:
		for x in connectors:
			if x.keys()[0] == iduser:
				return x[iduser] 
			else:
				return 0 
	else:
		return 0


data = ""
payload_size = struct.calcsize("L") 
while True:
	while len(data) < payload_size:
		data += conn.recv(4096)
	packed_msg_size = data[:payload_size]
	data = data[payload_size:]
	msg_size = struct.unpack("L", packed_msg_size)[0]
	while len(data) < msg_size:
		data += conn.recv(4096)
	# print(len(data))

	tail_uzip = pickle.loads(data)
	tail_uzip_json = json.loads(tail_uzip)
	img_uzip = tail_uzip_json["client"]["frame"]

	user = tail_uzip_json["client"]["name"]
	user_to = tail_uzip_json["client"]["to"]
	check_user_and_add(user, conn)



	img_uzip = base64.b64decode(img_uzip)
	decode_image = decode_to_img(img_uzip)

	print(get_opponent(user_to))
	if get_opponent(user_to) != 0:
		answer = pickle.dumps("Answer")
		get_opponent(user_to).sendall(answer)


	# cv2.imshow('frame',decode_image)
	# cv2.waitKey(1)


	data = ""
	# frame_data = data[:msg_size]
	# data = data[msg_size:]
		###


	# tail_uzip = pickle.loads(data)
	# tail_uzip_json = json.loads(tail_uzip)
	# print(tail_uzip_json["client"]["name"])
		

	