import socket, cv2, pickle,struct,imutils
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:',host_ip)
port = 1313
sa = (host_ip,port)
ss.bind(sa)
ss.listen(5)
print("LISTENING AT:",sa)

while True:
    cs,client_address = ss.accept()
    print('GOT CONNECTION FROM:',client_address)
    if cs:
        vid = cv2.VideoCapture(0)

        while(vid.isOpened()):
            img,photo = vid.read()
            photo = imutils.resize(photo,width=320)
            a = pickle.dumps(photo)
            video = struct.pack("Q",len(a))+a
            cs.sendall(video)

            cv2.imshow('CONNECTION_1 VIDEO',photo)
            key = cv2.waitKey(1) & 0xFF
            if key ==ord('q'):
                cs.close()
