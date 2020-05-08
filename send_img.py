import cv2
import socket
import sys
import pickle
import struct 
import json
import numpy as np
import base64 
import time


clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('localhost',8090))


def encode_to_string(img, img_format='.jpg'):
	'''encode uint8 image to byte string'''
	return cv2.imencode(img_format, img)[1].tobytes()



def decode_to_img(string):
	return cv2.imdecode(np.fromstring(string, np.uint8),cv2.IMREAD_COLOR)

cap=cv2.VideoCapture(1)
while True:

	while cap.isOpened():
		time.sleep(0.1) #Delay Normalize Traffic
		ret,frame=cap.read()
		img = frame 
		# img_data = base64.b64encode(pickle.dumps(img))

		string_encode = encode_to_string(img)

		string_encode = base64.b64encode(string_encode)



		# print(jpg_as_text)


		tail = """

		{
		   "client":{
			  "name":"89998394665",
			  "version":"0.01",
			  "to":"89998394667",
			  "frame":" """ + string_encode + """ "
		   }
		}

		"""
		tail_data = pickle.dumps(tail)
		print(len(tail_data))
		msg = struct.pack('L', len(tail_data)) + tail_data
		clientsocket.sendall(msg) ### new code

		# tail_uzip = pickle.loads(tail_data)
		# tail_uzip_json = json.loads(tail_uzip)

		# img_uzip = tail_uzip_json["client"]["frame"]

		# img_uzip = base64.b64decode(img_uzip)
		# decode_image = decode_to_img(img_uzip)

		# try:
		# 	cv2.imshow('frame',decode_image)
		# 	cv2.waitKey(1)
		# except KeyboardInterrupt:
		# 		cv2.destroyAllWindows()
		
