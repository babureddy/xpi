#!/usr/bin/python
# -*- coding:utf-8 -*-
import ast, json, os, datetime, time
import sets, copy, re, sys
import cgi, cgitb
cgitb.enable()
print "Content-Type: text/html\n\n"

def generate_xpi(dir):
	#command = "sh ./generate_xpi.sh " + dir
	#print command
	#os.system(command)
        os.chdir(dir)
	dt = time.strftime("%Y%m%d%H%M%S")
	os.system("zip -r /var/www/html/xpi/install_" + dt + ".xpi *")
	files = os.listdir("/var/www/html/xpi")
        return getXPIFiles(files) 
        
def getXPIFiles(files) :
    result = ""
    f = open('/var/www/html/xpi_manager/index.html', 'r')
    h = f.read()
    #print files
    count=1
    for file in files:
	if file == "None":
            continue
	result += "<li><a href=\"http://172.16.20.112/xpi/"+file+"\">" + str(count) + " " + file + "</li>"
        count += 1  
        #if(count > 5):    
        #    break 
    h.replace("MISC",result)
    f.close();
    print h,'<br><br><br>',result
    #return result

if __name__=="__main__":
   form = cgi.FieldStorage()
   if (form.has_key("dir")):
          tmp = generate_xpi(form["dir"].value)
          #print tmp
 
