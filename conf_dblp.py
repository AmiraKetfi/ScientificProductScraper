# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 23:01:40 2018

@author: pc
"""

import scholarly,re,urllib.request,nltk
import bs4 as bs
# =============================================================================
# #Probléme les derniere conf ne se rajoute pas 
# =============================================================================
def find_ComputerScienceConferences_Workshops_names_DBLP(url_deb):
    page=urllib.request.urlopen(url_deb).read()
    c,soup=0,bs.BeautifulSoup(page,'lxml')
    for p in soup.find_all('a'):
        if c==1 and p.text!="[previous 100 entries]": 
            print(p.text)
#            s1=p.get("href")
#            if re.search(r"http://dblp.uni-trier.de/db/conf/.",s1): 
#                publication_conf_dblp(s1)
        if p.text=="[next 100 entries]": 
            c,s=1,p.get("href")             
            url_a="http://dblp.uni-trier.de/db/conf/"+s
        if (p.text=="[previous 100 entries]")and(c==1):   find_ComputerScienceConferences_Workshops_names_DBLP(url_a)      

def Timeline_of_conferences(url_deb):
    page=urllib.request.urlopen(url_deb).read()
    soup=bs.BeautifulSoup(page,'lxml')
    last_s=""
    for q in soup.find_all('a'):    
        s=q.get("href")       
        if re.search(r"http://dblp.uni-trier.de/db/conf/.*/.*\.html",s): 
           if last_s!=s:
                fichier = open("Lien_de_toutes_les_conf.txt", "a")
                fichier.write("\n"+s)  
                fichier.close()
                last_s=s
def publication_conf_dblp(url):
    fichier = open("conf.txt", "w")
    fichier.close()
    fichier = open("publisher.txt", "w")
    fichier.close()
    fichier = open("Date.txt", "w")
    fichier.close()
    fichier = open("isbn.txt", "w")
    fichier.close()
    page=urllib.request.urlopen(url).read()
    soup=bs.BeautifulSoup(page,'lxml')
    c=0
    for p in soup.find_all('span'):
        s1=p.get("class")
        try:
            if s1[0]=='title':
                 fichier = open("conf.txt", "a")
                 fichier.write("\n"+p.text)  
                 fichier.close()
        except TypeError:
            print("\t")
        s2=p.get("itemprop")
        try:
            if s2=="publisher":
                 fichier = open("publisher.txt", "a")
                 fichier.write("\n"+p.text)  
                 fichier.close()
            if s2=="datePublished":
                 fichier = open("Date.txt", "a")
                 fichier.write("\n"+p.text)  
                 fichier.close()
            if s2=="isbn":
                 fichier = open("isbn.txt", "a")
                 fichier.write("\n"+p.text)  
                 fichier.close()
            if s2=="pagination":
                 fichier = open("pages.txt", "a")
                 fichier.write("\n"+p.text)  
                 fichier.close()                 
        except TypeError:
            print("\t")
#            pass
url_deb='https://dblp.uni-trier.de/db/conf/' 
url_deb2='http://dblp.uni-trier.de/db/conf/3dim/3dimpvt2012.html'  
url_deb3='http://dblp.uni-trier.de/db/conf/3dpvt/'
#Timeline_of_conferences(url_deb2)
publication_conf_dblp(url_deb3)
#find_ComputerScienceConferences_Workshops_names_DBLP(url_deb)            