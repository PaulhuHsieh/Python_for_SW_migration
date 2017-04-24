import pycurl
import xml.dom.minidom
from StringIO import StringIO

buffer = StringIO()
c = pycurl.Curl()
c.setopt(c.USERNAME, 'admin')
c.setopt(c.PASSWORD, 'admin')
c.setopt(c.HTTPHEADER, ["Accept:application/xml"])
c.setopt(c.URL, 'http://192.168.10.142:8181/dlux/index.html#/topology')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
doc = xml.dom.minidom.parseString(body)
print "yee"
print body
for node in doc.getElementsByTagName("node"):
	print "Hello my ID is: " + node.firstChild.firstChild.nodeValue 
