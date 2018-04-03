from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_journalEditors(link) :

    try :
         page= urlopen(link).read()
         soup = BeautifulSoup(page, 'html.parser')
    #print(soup.prettify().encode('utf-8'))
         elements = soup.find_all('div', attrs={'class':'publication-editors'})
         #print(element)
         for element in elements :
             links = element.find_all('a')
             editors=[]
             for linke in links :
                 #print(linke)
                 editors.append(linke.get('title'))
                 #print(editors)
             
             print(editors)
    except :
         print('Suprise MF!!')

def get_journalEditBoard(link) :

    try :
        page= urlopen(link).read()
        soup = BeautifulSoup(page, 'html.parser')
    #print(soup.prettify().encode('utf-8'))
        elements = soup.find('div', attrs={'class':'publication-editor-board'})
        links = elements.find('a').get('href')
        #print(links)
        #editB= urlopen(links).read()
        #soup = BeautifulSoup(editB,'html.parser')

    except :
        print('SUPRISE MF!')
    return links

def get_ExecutiveEditors(link) :
    
    try :
        #links=get_journalEditBoard(link)
        page = urlopen(link).read()
        soup = BeautifulSoup(page,'html.parser')
        #print(soup.encode('utf-8'))
        dic = {'Name':'','Affiliation':''}
        elements = soup.find_all('div',attrs={'class':'publication-editor'})
        editors= []
        for element in elements :
       #print(element.encode('utf-8'))
            name = element.find('div',attrs={'class':'publication-editor-name'})
            name = name.get_text()
            #print(name)
            dic['Name']=name
            affiliation = element.find('span',attrs={'class':'publication-editor-affiliation'}).get_text()
            #print(affiliation.encode('utf-8'))
            dic['Affiliation']= affiliation.encode('utf-8')
            #print(dic)
            editors.append(list(dic.values()))
        for editor in editors :
            #print(list(editor.values()))
            print(editor)
   
    except :
        print('SUPRISE MF!')
    return editors

def get_BooksEditors(link) :

    try :
        page= urlopen(link).read()
        soup = BeautifulSoup(page, 'html.parser')
        element = soup.find('div',attrs={'class':'book-info-column'})
        #print(element)
        editors=[]
        infos = element.find_all('span', {'class' : 'inline weak editor'}, limit=None)
        #print(infos)
        for info in infos :
            editors.append(info.get_text())
        #for editor in editors :
            #print(editor)
    except:
        print('SUPRISE MF!')
    return editors
    


#link =get_journalEditBoard('https://www.journals.elsevier.com/aquaculture-reports')
#JournalEditors = get_ExecutiveEditors(link)
#BookEditors= get_BooksEditors('https://www.elsevier.com/books/multimodal-behavior-analysis-in-the-wild/alameda-pineda/978-0-12-814601-9')
import csv

with open('resultat.csv', newline='',encoding='latin-1') as csvfile:
    spamreader = csv.DictReader(csvfile,delimiter=',',quotechar='|')
    editors=[]
    for row in spamreader:
        print(row['link'])
        editors=[]
        if row['ProductType'] == 'Book':
            editors=get_BooksEditors(row['link'])
        print('The Editors of ',row['title'],':',editors)