#!/usr/bin/env python
#mathieuchot-plassot.com

import requests
import sys 
import json 
import time

providers=['hotmail.fr', 'free.fr', 'orange.fr', 'live.fr', 'sfr.fr', 'yahoo.fr',\
           'gmail.com', 'outlook.fr', 'hotmail.com', 'yahoo.com', 'laposte.net']
headers = {'User-agent': 'mathieuchot haveibeenpwn script'}

for i in providers:
    account = "{}@{}".format(sys.argv[1], i)
    try:
        r = requests.get("https://haveibeenpwned.com/api/v2/breachedaccount/"+account, headers)
        #print r.text 
        #print r.status_code
        if r.status_code == 429:    #API rate limit excedeed
                break
        if r.status_code == 404:    #nothing found
            time.sleep(2)
            continue
        infos = json.loads(r.text)
        print "\n-----------"+account+"-------------\n"
        for sites in range(0, (len(infos))):
            print "{}PWNED on {} the {}{}".format('\033[93m', infos[sites]['Title'], \
                    infos[sites]['BreachDate'], '\033[0m')
    except Exception as j:
        print "\n {}       ERROR -- {} \n".format(account, j ) 
    time.sleep(2)
