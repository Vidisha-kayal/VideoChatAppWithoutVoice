import socket,cv2, pickle,struct
cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# We will have to paste server ip address here
host_ip = '' 
port = 1313
cs.connect((host_ip,port)) 
data = b""
payload_size = struct.calcsize("Q")
while True:
    while len(data) < payload_size:
        packet = cs.recv(4*1024) # 4K
        if not packet:
            break
        data+=packet
    pms = data[:payload_size]
    data = data[payload_size:]
    ms= struct.unpack("Q",pms)[0]

    while len(data) < ms:
        data += cs.recv(4*1024)
    video_data = data[:ms]
    data  = data[ms:]
    video = pickle.loads(video_data)
    cv2.imshow("CONNECTION_2 VIDEO",video)
    key = cv2.waitKey(1) & 0xFF
    if key  == ord('q'):
        break
cs.close()
