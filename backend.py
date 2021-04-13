from cryptography.fernet import Fernet
import random, base64, string, json, os, pickle, io, shutil, re
import datetime

def generateSessionToken(username):
    #---- Generates random string for session, sessionToken gets stored as cookie Value ----
    sessionToken = ''.join(random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation) for _ in range(120))
    #---- Stores encrypted sessionToken into dictionary and uses encrypted sessionToken as Cookie Value ----
    return encryption(sessionToken,username)

def encryption(text, Member):
    #---- Changes string to byte format ----
    bytetext = str.encode(text)
    #--- Generates a special key ----
    key = Fernet.generate_key()
    encryption_type = Fernet(key)
    #---- Makes Token string an encrypted fernet with the generated key for the byte string ----
    token = encryption_type.encrypt(bytetext)
    #---- Updates the password dictionary in this file so easily can grab the data and decrypt the fernet key without public key ----
    password.update({Member: (token, key)})
    #---- Returns encrypted text text format ----
    return token

def encryptedtext(value):
    #---- Returns encrypted Token ----
    try:
        return password.get(value)[0]
    except TypeError:
        return "doesn't exist"

def checkUserid(userid):
    with open('userid.txt') as f:
        records = f.read().splitlines()
    for x in records:
        if x.split(",")[0] == userid:
            return True
    return False

password = {}
with open("information.json") as secretinformation:
    data = json.load(secretinformation)