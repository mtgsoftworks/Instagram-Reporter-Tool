# coding=utf-8
#!/usr/bin/env python3


__author__ = "mtg_softworks"
__license__ = "GPLv3"
__version__ = "1.0"
__status__ = "alfa"


import requests
import re
from time import time, sleep
from random import choice
from multiprocessing import Process

from libs.utils import CheckPublicIP, IsProxyWorking
from libs.utils import PrintStatus, PrintSuccess, PrintError
from libs.utils import PrintBanner, GetInput, PrintFatalError
from libs.utils import LoadUsers, LoadProxies, PrintChoices

from libs.instaclient import InstaClient

USERS = []
PROXIES = []

def MultiThread(username, userid, loginuser, loginpass, proxy, reasonid):
    client = None
    if (proxy != None):
        PrintStatus("[" + loginuser + "]", "Logging into the Account!")
        client = InstaClient(
            loginuser,
            loginpass,
            proxy["ip"],
            proxy["port"]
        )
    else:
        PrintStatus("[" + loginuser + "]", "Logging into the Account!")
        client = InstaClient(
            loginuser,
            loginpass,
            None,
            None
        )
        
    client.Connect()
    client.Login()
    client.Spam(userid, username, reasonid)
    print("")

def NoMultiThread():
    for user in USERS:
        client = None
        if (useproxy):
            proxy = choice(PROXIES)
            PrintStatus("[" + user["user"] + "]", "Logging into the Account!")
            client = InstaClient(
                user["user"],
                user["password"],
                proxy["ip"],
                proxy["port"]
            )
        else:
            proxy = choice(PROXIES)
            PrintStatus("[" + user["user"] + "]", "Logging into the Account!")
            client = InstaClient(
                user["user"],
                user["password"],
                None,
                None
            )
        
        client.Connect()
        client.Login()
        client.Spam(userid, username, reasonid)
        print("")

def get_instagram_user_id(username):

    profile_url = f"https://www.instagram.com/{username}/"

    response = requests.get(profile_url)

    page_source = response.text

    pattern = r"profilePage_([0-9]+)"
    match = re.search(pattern, page_source)

    if match:
        user_id = match.group(1)
        return user_id

    return None



if __name__ == "__main__":
    PrintBanner()
    PrintStatus("Loading users!")
    USERS = LoadUsers("./users.txt")
    PrintStatus("Loading Proxes!")
    PROXIES = LoadProxies("./proxy.txt")
    print("")

    username = GetInput("Account username:")
    userid = get_instagram_user_id(username)
    print("Instagram User ID:", userid)
    useproxy = GetInput("Do you want to use proxy? [Yes(Y) No(N)]:")
    if (useproxy.upper() == "Y"):
        useproxy = True
    elif (useproxy.upper() == "N"):
        useproxy = False
    else:
        PrintFatalError("Please just enter 'Y' or 'N'!")
        exit(0)
    usemultithread = GetInput("Do you want to use multithreading? [Yes / No] (Do not use this feature if you have too many users or if your computer is slow!):")
    
    if (usemultithread.upper() == "Y"):
        usemultithread = True
    elif (usemultithread.upper() == "N"):
        usemultithread = False
    else:
        PrintFatalError("Please just enter 'Y' or 'N'!")
        exit(0)
    
    PrintChoices()
    reasonid = GetInput("Please select one of the reasons for the above complaint (ex: 1 for spam):")

    
    print("")
    PrintStatus("Starting...")
    print("")

    if (usemultithread == False):
        NoMultiThread()
    else:
        for user in USERS:
            p = Process(target=MultiThread,
                args=(username,
                    userid,
                    user["user"],
                    user["password"],
                    None if useproxy == False else choice(PROXIES),
                    reasonid
                )
            )
            p.start() 
