#method returning the file name e.g.  http://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/ObjectiveC/ObjC.pdf will return objC.pdf
def targetname(url):
  return url.split('/')[-1]

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
    url=conn.recv(1024)
    print(url)
# request is used to download the url (http://docs.python-requests.org/en/latest/index.html)
    r=requests.get(url)
    targetfile=targetname(url)
    with open(targetfile,"wb") as code:  # writing to target file
     code.write(r.content);
     print 'page downloaded'
    conn.close()
s.close()
