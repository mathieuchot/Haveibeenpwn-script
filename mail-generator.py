#!/usr/bin/env python
#mail generator
#blog.mathieu.chot-plassot.com

import sys
import requests
import time
import json
import argparse

parser = argparse.ArgumentParser(description="A simple mail checker",\
        epilog="Exemple: {} -f 'mathieu' -l 'chot-plassot' -s '1337' -p 'protonmail.com'".format(sys.argv[0]))
parser.add_argument("-f", "--firstname",action="store", type=str, required=True,\
        help="Firstname of the victim")
parser.add_argument("-l", "--lastname",action="store", type=str, required=True,\
        help="Lastname of the victim")
parser.add_argument("-s", "--spec", action="store",type=str, default='', required=False,\
        help="Age, Birthdate, zipcode, something to add...")
parser.add_argument("-p", "--provider",action="store", type=str, required=False,\
        help="A mail provider to add")
params = parser.parse_args()


headers = {'User-agent': 'mathieuchot haveibeenpwn script'}
providers=['hotmail.fr', 'free.fr', 'orange.fr', 'live.fr',\
        'sfr.fr', 'yahoo.fr','gmail.com', 'outlook.fr',\
        'hotmail.com', 'yahoo.com', 'laposte.net']

if params.provider:
    providers.append(params.provider)
firstname=params.firstname
lastname=params.lastname
def gen_mail(spec):
    mails=[]
    for i in providers:
        mails.append("{}{}{}@{}".format(lastname,firstname,spec,i))
        mails.append("{}{}{}@{}".format(firstname,lastname,spec,i))
        mails.append("{}{}{}@{}".format(lastname[:1],firstname,spec,i))
        mails.append("{}{}{}@{}".format(firstname,lastname[:1],spec,i))
        mails.append("{}{}{}@{}".format(firstname[:1],lastname,spec,i))
        mails.append("{}.{}{}@{}".format(lastname,firstname,spec,i))
        mails.append("{}_{}{}@{}".format(lastname,firstname,spec,i))
        mails.append("{}-{}{}@{}".format(lastname,firstname,spec,i))
        mails.append("{}.{}{}@{}".format(firstname,lastname,spec,i))
        mails.append("{}_{}{}@{}".format(firstname,lastname,spec,i))
        mails.append("{}-{}{}@{}".format(firstname,lastname,spec,i))
        mails.append("{}{}{}@{}".format(firstname,lastname[:3],spec,i))
        mails.append("{}{}{}@{}".format(firstname,lastname[:4],spec,i))
        mails.append("{}.{}{}@{}".format(firstname,lastname[:3],spec,i))
        mails.append("{}.{}{}@{}".format(firstname,lastname[:4],spec,i))
        mails.append("{}_{}{}@{}".format(firstname,lastname[:3],spec,i))
        mails.append("{}_{}{}@{}".format(firstname,lastname[:4],spec,i))
        mails.append("{}-{}{}@{}".format(firstname,lastname[:3],spec,i))
        mails.append("{}-{}{}@{}".format(firstname,lastname[:4],spec,i))
        mails.append("{}{}{}@{}".format(lastname[:3],firstname,spec,i))
        mails.append("{}{}{}@{}".format(lastname[:4],firstname,spec,i))
        mails.append("{}.{}{}@{}".format(lastname[:4],firstname,spec,i))
        mails.append("{}.{}{}@{}".format(lastname[:3],firstname,spec,i))
    return mails

if params.spec: 
    result=gen_mail(params.spec)
    result2=gen_mail('')
    for i in result2:
        result.append(i)
else:
    result=gen_mail(params.spec)


print result
rep=raw_input("\033[0;33m Do you want to Save the list (y/n)?\033[0;0m")
if rep=="yes" or rep=="y":
    with open("{}/{}{}{}.txt".format(sys.path[0], firstname, lastname, params.spec), 'w+') as f:
        for i in result:
            f.write(i+"\n")
rep=raw_input("\033[0;33m Would you like to check if those emails have been pwned (y/n)?\033[0;0m")
if rep=="yes" or rep=="y":
    for j in result:
        try:
            r = requests.get("https://haveibeenpwned.com/api/v2/breachedaccount/"+j, headers)
            #print r.text 
            #print r.status_code
            if r.status_code == 429:    #API rate limit excedeed
                break
            if r.status_code == 404:    #nothing found
                time.sleep(2)
                continue
            infos = json.loads(r.text)
            print "\n-----------"+j+"-------------\n"
            for sites in range(0, (len(infos))):
                print "{}PWNED on {} the {}{}".format('\033[93m', infos[sites]['Title'], \
                        infos[sites]['BreachDate'], '\033[0m')
        except Exception as x:
            print "\n {}       ERROR -- {} \n".format(j, x ) 
        time.sleep(2)
else:
    print "\nok bye...\n"
    sys.exit()
