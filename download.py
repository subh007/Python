import urllib
import sys
sys.path.append('/home/subhash/subh/python/requests')
import requests
print sys.argv[1]
r=requests.get(sys.argv[1])
with open(sys.argv[2],"wb") as code:
 code.write(r.content)
