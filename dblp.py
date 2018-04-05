# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 12:26:22 2018

@author: pc
"""
import scholarly,re,urllib.request,nltk
import bs4 as bs,codecs
def find_Authors_Edithors_names_DBLP(url_deb):
    page=urllib.request.urlopen(url_deb).read()
    c,soup=0,bs.BeautifulSoup(page,'lxml')
    for p in soup.find_all('a'):
        if c==1 and p.text!="[previous 300 entries]": 
#            fichier = open("Authors_Editors_names.txt", "a")
#            fichier.write("\n"+p.text)
#            fichier.close()             
            print (p.text)
        if p.text=="[next 300 entries]": 
            c,s=1,p.get("href")             
            url_a="http://dblp.dagstuhl.de/pers/"+s
        if (p.text=="[previous 300 entries]")and(c==1):  find_Authors_Edithors_names_DBLP(url_a)      
#url_deb='http://dblp.uni-trier.de/pers/'
#find_Authors_Edithors_names_DBLP(url_deb)
def find_Publication_DBLP(nom,prenom):
    c=0
    url="https://dblp.dagstuhl.de/pers/hd/"+nom[0].lower()+"/"+nom+":"+prenom
    page=urllib.request.urlopen(url).read()
    soup=bs.BeautifulSoup(page,'lxml')
    for p in soup.find_all('span'):
        if c<=9: c=c+1
        if c==10 :    print(p.string)
                
find_Publication_DBLP("A=","Mohammed_Saaqib")        