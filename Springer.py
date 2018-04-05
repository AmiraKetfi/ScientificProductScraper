# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 12:43:03 2018

@author: pc
"""
import urllib.request,re
import bs4 as bs
def Springer_journals(url_deb):
    page=urllib.request.urlopen(url_deb).read()
    soup=bs.BeautifulSoup(page,'lxml')
    for p in soup.find_all('p'):
        if re.search("Editor-in-Chief:",p.text):print("L'editor-in-chief:\t"+p.text[17:])
    for p in soup.find_all('h1',attrs={'wicketpath': 'content_basic_productDescriptionContainer_title','class':'headline'}):print("Title:\t"+p.text)
    for p in soup.find_all('span',attrs={'wicketpath':'content_basic_productDescriptionContainer_productDescription_issnElectronic_content'}):print("ISSN:\t"+p.text)            
    for p in soup.find_all('li',attrs={'wicketpath':'rightColumn_forAuthorsAndEditorsPortlet_portletContent_impactFactor_impactFactor'}):print("L'impact factor"+p.text)
#url_deb='http://www.springer.com/journal/41114'        
#Springer_journals(url_deb)        
def Springer_journals_link(url_deb2):
    page=urllib.request.urlopen(url_deb2).read()
    soup=bs.BeautifulSoup(page,'lxml')
    for p in soup.find_all('a'):
        try:
            if re.search(r"/journal/\d*",p.get('href')):
                fichier = open("springer.txt", "a")
                fichier.write("http://www.springer.com"+p.get('href')+"\n")
                fichier.close()
            if p.get('class')[0]=='next':Springer_journals_link("http://www.springer.com"+p.get('href'))                
        except TypeError:        
            pass
#page contenant tous les journaux         
#url_deb2="http://www.springer.com/gp/product-search/discipline?topic=P22006,P22014,P22022,P22030,P22049,P22057,P22080,Q11009&disciplineId=astronomy&facet-type=type__journal&returnUrl=gp%2Fastronomy"            
#Springer_journals_link('http://www.springer.com//gp/products/proceedings/featured-series/10305792')           
def Springer_see_all(url_deb):
    page=urllib.request.urlopen(url_deb).read()
    soup=bs.BeautifulSoup(page,'lxml')
    for p in soup.find_all('a'):
        try:
            if re.match(r'\bhttp://www.springer.com/gp/.*\b',p.get('href')):
                Springer_see_all_step2(p.get('href'))
        except TypeError:
            pass
def Springer_see_all_step2(url_deb):
    c,page=0,urllib.request.urlopen(url_deb).read()
    soup=bs.BeautifulSoup(page,'lxml')
    for p in soup.find_all('a'):
        if p.text=="see all":
            if re.search(r".*type__journal.*",p.get('href')):
                fichier = open("Journales.txt", "a")
                fichier.write("http://www.springer.com/"+p.get('href')+"\n")
                fichier.close()
            if re.search(r".*categorybook__pcytextbook.*",p.get('href')):
                s="http://www.springer.com"+p.get('href')
                print(s)
                Springer_see_all_step3(s)
#Donne tous les liens de chaque domaine
#Done tous liens "see all" de tous les domaine             
def Springer_see_all_step3(url_deb3):
    page=urllib.request.urlopen(url_deb3).read()
    soup=bs.BeautifulSoup(page,'lxml')
    for p in soup.find_all('a',attrs={'class':'facet-link facet-link-lan__en','title':'Remove this filter'}):
        fichier = open("BooksTextbooks.txt", "a")
        fichier.write("http://www.springer.com"+p.get('href')+"\n")
        fichier.close()    
url_deb3='http://www.springer.com/gp/'
Springer_see_all(url_deb3)            