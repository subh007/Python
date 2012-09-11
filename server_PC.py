import sys
import socket
sys.path.append('/home/subhash/subh/python/requests')
import requests
s=socket.socket()
hostname=socket.gethostname()
port=9595
s.bind((hostname,port))
s.listen(5)
while True:
    print 'server started'
    conn,addr=s.accept()
    data=conn.recv(1024)
    print(data)
    r=requests.get(data)
    with open('downloded.pdf',"wb") as code:
     code.write(r.content);
     print 'page downloaded'
    conn.close()
s.close()
