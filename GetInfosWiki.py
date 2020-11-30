#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:46:59 2020

@author: pierre
"""

import requests
URL = "https://en.wikipedia.org/w/api.php"
def GetWikiInfos(title):
    PARAMS = {
        "action": "query",
        "titles": f"{title}",
        "prop":"revisions",
        "rvlimit":"1",
        "rvprop":"timestamp",
        "rvdir":"newer",
        "format": "json"
    }

    R = requests.get(url=URL, params=PARAMS)
    DATA = R.json()
    PAGES = DATA["query"]["pages"]
    ["revisions"]
    print(PAGES)
GetWikiInfos('physics')