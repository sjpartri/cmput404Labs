#!/usr/bin/env python

import os,json, cgi

print "Content-type: text/html"
print 
print "<HTML><BODY><H1>Hello, WORLD!</H1>"
print "<FORM method='POST'><INPUT name = 'x'></FORM>"
form = cgi.FieldStorage()

print "<P>X was: " + cgi.escape(str(form.getvalue('x')))

#makes data look cleaner
#print json.dumps(dict(os.environ), indent=4)
print "</BODY></HTML>"
