from bottle import route, post, run, request, static_file, get, response, template, error
from datetime import datetime, timedelta
import json
import backend
import re
import os
import time

def getuserId():
    with open('userid.txt') as f:
        records = f.read().splitlines()
    for x in records:
        if request.get_cookie("isUser" + re.sub('[^A-Za-z0-9]+','',str(backend.encryptedtext(x.split(",")[0])))) is "1":
            return x.split(",")[0].strip(), x.split(",")[1].strip()

@route('/viewReport')
def viewReport():
    return template("static/viewReport.tpl",)

@post('/reportCredentials')
def reportviewable():
    firstName = request.forms.get("firstName") 
    lastName = request.forms.get("lastName")
    userId = request.forms.get("userid")
    if backend.checkUserid(userId):
        backend.generateSessionToken(userId)
        backend.generateSessionToken(firstName+ lastName)
        response.set_cookie("isUser" + str(re.sub('[^A-Za-z0-9]+','',str(backend.encryptedtext(userId)))), "1", expires=time.mktime((datetime.now() + timedelta(hours=1)).timetuple()))
        return '''<meta http-equiv="refresh" content="0; URL='/report/''' + str(re.sub('[^A-Za-z0-9]+','',str(backend.encryptedtext(firstName+lastName)))) + ''''" />'''
    return '''<meta http-equiv="refresh" content="0; URL='https://matrixdiagnostics.org/'" />'''

@route('/report/<reportid>')
def reportViewContent(reportid):
    userid, filename = getuserId()
    print("filename")
    filenamedict = {'filename': "/pdf/" + filename}
    if request.get_cookie("isUser" + re.sub('[^A-Za-z0-9]+','',str(backend.encryptedtext(userid)))) is "1":
        return template("static/viewPDF.tpl", filenamedict)
    else:
        return '''<meta http-equiv="refresh" content="0; URL='https://matrixdiagnostics.org/'" />'''

@route('/images/<filename>')
def serverImages(filename):
    return static_file(filename, root=os.path.abspath('images'))

@route('/pdf/<filename>')
def serverarchive(filename):
    userid, filename = getuserId()
    if request.get_cookie("isUser" + re.sub('[^A-Za-z0-9]+','',str(backend.encryptedtext(userid)))) is "1":
        return static_file(filename, root=os.path.abspath('pdf'))
    else:
        return '''<meta http-equiv="refresh" content="0; URL='https://matrixdiagnostics.org/'" />'''

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=os.path.abspath('static'))

@error(500)
def error500(error):
    return '''<meta http-equiv="refresh" content="0; URL='https://matrixdiagnostics.org/'" />'''

@error(404)
def error404(error):
    return '''<meta http-equiv="refresh" content="0; URL='https://matrixdiagnostics.org/'" />'''
    
with open("information.json") as secretinformation:
    data = json.load(secretinformation)
run(host=data.get("webserver")[0:data.get("webserver").find(":")], port=os.environ.get('PORT', 5000), debug=True)