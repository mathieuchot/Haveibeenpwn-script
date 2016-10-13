#!/usr/bin/env python
# coding: utf8
#Evil pwner

import sys
import requests
import time
import json
import argparse

ascii_art='''\033[0;36m          
        .wwwwwwww.         
(⌒▽⌒) .w"  "WW"  "w.     
     ."   ~\  /~   ".   
    |\     O  O     /|  
    \|, ()__\/__() ,|/  ~(‾▿‾)~
     / \ \_v__v_/ / \   
    / | \________/ | \\
    >  \ mathieu  /  <
,`  \   \   ""   /   /  
     \,  \ chot /  ,/   ٩(͡๏̯͡๏)۶
----,________________,-------`'-
    |   EVIL PWNER   |  
    |   28/09/2016   |
    `----------------'  \033[0;0m
'''
print ascii_art

usage_help="\033[0;32mExemple with -n:\033[0;36m {} -n 'mathieu'\
 'chot-plassot' [-s '1337'] [-p 'protonmail.com']\n\033[0;32mExemple with -u: \033[0;36m {} -u 'gentilkiwi'\
 [-p 'me.com']\033[0;0m".format(sys.argv[0],sys.argv[0])

parser = argparse.ArgumentParser(description="A simple mail checker")
parser.add_argument("-n", "--name", action="store", type=str, required=False,\
        help="[0]First name and [1]Lastname of the victim", nargs=2)
parser.add_argument("-u", "--username",action="store", default='', type=str, required=False,\
        help="Username of the victim")
parser.add_argument("-s", "--spec", action="store",type=str, default='', required=False,\
        help="Age, Birthdate, zipcode, something to add...")
parser.add_argument("-p", "--provider",action="store", type=str, required=False,\
        help="A mail provider to add")
params = parser.parse_args()
if len(sys.argv) < 2:
    print usage_help
    sys.exit()

headers = {'User-agent': 'mathieuchot haveibeenpwn script'}
providers=['hotmail.fr', 'free.fr', 'orange.fr', 'live.fr',\
        'sfr.fr', 'yahoo.fr','gmail.com', 'outlook.fr',\
        'hotmail.com', 'yahoo.com', 'laposte.net']

if params.provider:
    providers.append(params.provider)
def gen_mail(spec):
    mails=[]
    if params.name:
        firstname=params.name[0]
        lastname=params.name[1]
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
    elif params.username:
        for i in providers:
            mails.append("{}@{}".format(params.username, i))
        return mails
    else:
        print usage_help
        sys.exit()
if params.spec: 
    if params.username:
        print "\033[0;33m Skipping... -s is not compatible with -u\033[0;0m"
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
