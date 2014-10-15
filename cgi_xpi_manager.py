#!/usr/bin/python
# -*- coding:utf-8 -*-
import ast, json, os
import sets, copy, re, sys
import cgi, cgitb
cgitb.enable()
print "Content-Type: text/html\n\n"

def generate_xpi(dir):
	command = "sh ./generate_xpi.sh " + dir
	#print command
	os.system(command)
	files = os.listdir("/var/www/html/xpi")
        return getXPIFiles(files) 
        
def getXPIFiles(files) :
    result = ""
    f = open('/var/www/html/xpi_manager/index.html', 'r')
    h = f.read()
    files.reverse()
    #print files
    count=1
    for file in files:
	if file == "None":
            continue
	result += "<li><a href=\"http://172.16.20.112/xpi/"+file+"\">" + file + "</li>"
        count += 1  
        if(count > 5):    
            break 
    h.replace("MISC",result)
    f.close();
    print h,'<br><br><br>',result
    #return result

if __name__=="__main__":
   form = cgi.FieldStorage()
   if (form.has_key("dir")):
          tmp = generate_xpi(form["dir"].value)
          print tmp
 
