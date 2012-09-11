import socket
sock=socket.socket()
hostname=socket.gethostname()
port=9595
sock.connect((hostname,port))
sock.send('http://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/ObjCRuntimeGuide.pdf')
sock.close()

