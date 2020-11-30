#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 12:25:48 2020

@author: pierre
"""

import requests
from bs4 import BeautifulSoup
import json
import pickle
import pandas as pd
import re
from ScrapFunc import GetPage

def GetTitle(Soup):
    return Soup.find('h1',{'id':'firstHeading'}).text


def ScrapLink(Soup):
    # /wiki/
    liste1=Soup.find('div',{'class':"mw-parser-output"}).find_all('a',{'href': re.compile(r'^((?!wikibooks|wikisource|Aide|Portail|veaction=edit).)*$'),'title':True})
    liste=Soup.find('div',{'class':"mw-parser-output"}).find_all('a',{'href': re.compile(r'/wiki/\w'),'title':True})    
    Listepages1=[item.attrs for item in set(liste1)]
    return Listepages1

def save_liste(title,liste):
    with open(f'{title}.txt','w'):
# def RecurScrap(entryURL,Depth):
#     for i in range(Depth):
                


entryURL="https://fr.wikipedia.org/wiki/Math%C3%A9matiques"
Liste_Linked_URL=ScrapLink(GetPage(entryURL))
print(Liste_Linked_URL)

for url in Liste_Linked_URL:
    Liste_Linked_URL=ScrapLink(GetPage(url))
    save_liste



