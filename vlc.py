import urllib2
import sys
import re
import base64
from urlparse import urlparse
from urllib import urlencode
import serial

ser = serial.Serial("/dev/ttyUSB0")


def query(req):
    username = ''
    password = 'hello'            # a very bad password
    base64string = base64.encodestring(
                    '%s:%s' % (username, password))[:-1]
    authheader =  "Basic %s" % base64string
    req.add_header("Authorization", authheader)
    try:
        handle = urllib2.urlopen(req)
    except IOError, e:
        print "It looks like the username or password is wrong."
        sys.exit(1)


def sendcommand(command):        
    theurl = 'http://localhost:8080/requests/status.xml'
    values=dict({'command':command})
    data = urlencode(values)
    req = urllib2.Request(theurl+"?"+data)
    query(req)
    
#thepage = handle.read()
def changevolume(UorD):
    theurl = 'http://localhost:8080/requests/status.xml'
    if UorD:
        values=dict({'command':'volume','val':'+30'})
    else:
        values=dict({'command':'volume','val':'-30'})
    data = urlencode(values)
    req = urllib2.Request(theurl+"?"+data)
    query(req)

def seek(ForB):
    theurl = 'http://localhost:8080/requests/status.xml'
    if ForB:
        values=dict({'command':'seek','val':'+0H:2M'})
    else:
        values=dict({'command':'seek','val':'-0H:2M'})
    data = urlencode(values)
    req = urllib2.Request(theurl+"?"+data)
    query(req)


while True:
    input1=ser.readline()
    if input1=="77E120B2\r\n":
        sendcommand('pl_pause')
    elif input1=="77E1D0B2\r\n":
        changevolume(True)
    elif input1=="77E1E0B2\r\n":
        #sendcommand('pl_next')
        seek(True)
    elif input1=="77E1B0B2\r\n":
        changevolume(False)
    elif input1=="77E110B2\r\n":
        #sendcommand('pl_previous')
        seek(False)
    elif input1=="77E140B2\r\n":
        sendcommand('fullscreen')