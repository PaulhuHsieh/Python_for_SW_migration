#!/usr/bin/python

import urllib2
import subprocess
import sys
import signal
import os

from time import sleep

td_str = "port 49850"
p2 = subprocess.Popen(["tcpdump", "-i", "eth5", td_str ], stdout=subprocess.PIPE )

#f = open("tcpdump.txt","w")

#for row in iter(p2.stdout.readline, b''):
	#print row.rstrip()
 	#f.write(row.rstrip())

sleep(1)

#subprocess.Popen(["kill, p2.pid"])

#output,err = p2.communicate()

os.kill(p2.pid, signal.SIGKILL)

output,err = p2.communicate()

f = open("tcpdump.txt","w")

f.write(output)

f.close();

