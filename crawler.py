#!/usr/bin/env python

import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "controltechnology.co.za"

with open("/root/Downloads/dirs_wordlist.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        #test_url = word + "." + target_url                 #For subdomains
        test_url = target_url + "/" + word                  #For directores
        response = request(test_url)
        if response:
            #print("[+] Discovered subdomain --> " + test_url)
            print("[+] Discovered url --> " + test_url)
