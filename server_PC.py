#method returning the file name e.g.  http://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/ObjectiveC/ObjC.pdf will return objC.pdf
# run using : python server_PC.py IP_ADDRESS_SERVER
def targetname(url):
  return url.split('/')[-1]

import sys
import socket
sys.path.append('/Users/subh/subh_mac/github/request/requests')
import requests


def main(argv):
   s=socket.socket()
   hostname=socket.gethostname()
   serverIP=argv[0]
   port=9595

   print 'server started at  %',serverIP
   s.bind((serverIP,port))
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
      conn.send("downloading completed")
      conn.close()
   s.close()

if __name__=='__main__':
   if len(sys.argv)<2:
       print 'pass server IP'
   else:
       main(sys.argv[1:])
