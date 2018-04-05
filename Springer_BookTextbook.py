# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 19:08:32 2018

@author: pc
"""
import urllib.request,re
import bs4 as bs
def Springer_Book_Textbook_information(url_deb):
    page=urllib.request.urlopen(url_deb).read()
    soup=bs.BeautifulSoup(page,'lxml')
    x1=soup.find_all('dl',attrs={'class':'cms-col small-6 medium-4 columns'})[0].text.splitlines()
    x2=soup.find_all('dl',attrs={'class':'cms-col small-6 medium-4 columns'})[1].text.splitlines()
    x3=soup.find_all('dl',attrs={'class':'cms-col small-6 medium-4 columns'})[2].text.splitlines()
    return x1,x2,x3
#url_deb="http://www.springer.com/gp/book/9783319327464"            
#Springer_Book_Textbook_information(url_deb)
def Springer_journals_link(url_deb2):
    page=urllib.request.urlopen(url_deb2).read()
    soup=bs.BeautifulSoup(page,'lxml')
    for p in soup.find_all('a'):
        try:
            if re.search(r"/book/\d*",p.get('href')):
                fichier = open("springer_Book.txt", "a")
                fichier.write("http://www.springer.com"+p.get('href')+"\n")
                fichier.close()
            if p.get('class')[0]=='next':Springer_journals_link("http://www.springer.com"+p.get('href'))                
        except TypeError:        
            pass
#Donne tous les book and textbook
#url_deb2="http://www.springer.com/gp/product-search/discipline?disciplineId=astronomy&facet-categorybook=categorybook__pcytextbook&facet-type=type__book&returnUrl=gp%2Fastronomy&topic=P22006%2CP22014%2CP22022%2CP22030%2CP22049%2CP22057%2CP22080%2CQ11009"        
#Springer_journals_link(url_deb2)        