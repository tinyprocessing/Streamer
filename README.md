# SocketStreamVideo ![](https://img.shields.io/badge/version-v1.0-green) ![](https://img.shields.io/badge/python-3.0-orange)

---
 Stream video via socket in python
---

*Project shows how you can interect with video and frames using cv2. See requirements below.*

```python
import os 
import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new
import base64 
import time
```

*All main code is in send_img.py and server.py. I use cv2 and frame by frame convert to base64 format and send data.*

---

### Create byte array
```python
encode_to_string(img, img_format='.jpg')

#Add some tail and push

pickle.dumps(tail)

```


### Recieve data 

```python
while len(data) < payload_size:
			data += conn.recv(4096)
		packed_msg_size = data[:payload_size]
		data = data[payload_size:]
		msg_size = struct.unpack("L", packed_msg_size)[0]
		while len(data) < msg_size:
			data += conn.recv(4096)
		frame_data = data[:msg_size]
		data = data[msg_size:]
```

*We are using it to create back our tail 😎.*

