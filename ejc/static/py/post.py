#!/usr/bin/python

import cgi, cgitb 
cgitb.enable()  # for troubleshooting

#the cgi library gets vars from html
data = cgi.FieldStorage()
#this is the actual output
print "Content-Type: text/html\n" + data["txAssunto"]