
from urllib.request import urlopen
from bs4 import BeautifulSoup

def journal_info(link) :
        data = []
#    try :
        page= urlopen(link).read()
        soup = BeautifulSoup(page, 'html.parser')
        #print(soup.prettify().encode('utf-8'))
        journals = soup.find_all('div', attrs={'class': 'listing-products-info'})
        for journal in journals :
            #print(journal.encode('utf-8'))
            strin = journal.find('img')['alt']
            #print(strin[16:])
            title = strin[16:]
            link = journal.find('a')['href']
            #print(link)
            product = journal.find_all('strong')
            final_list = []
            Volume=''
            for p in product:
                products= p.next_sibling
                #print(products)
                final_list += products.splitlines()
                #print("jhgjgjgj",l)
                #print('final list', final_list[0])
                #print(final_list.pop())
                try :
                    ProductType= final_list[0]
                    Edition= final_list[1]
                    Volume=final_list[2]
                    FirstPublished= final_list[3]
                    Hardcover= final_list[4]
                except : 
                        ProductType= ''
                        Edition= ''
                        FirstPublished= ''
                        Hardcover= ''
                #ProductType = final_list[0]
            #listee += final_list
        #print('final list', final_list)
        info = [title, link, ProductType, Edition, Volume, FirstPublished, Hardcover]
            

        print ("[DEBUG] ", info)
        data.append(info)
        print(data)
#    except :
#        print('suprise mf')
        return data


def fetch_all_jornals() :
    '''
    This function is used to fetch all journal links from a page.
    Elsevier returns only 20 journal links in a page.
    start : http://www.elsevier.com/journals/title/all?start_rank=1
    end : http://www.elsevier.com/journals/title/all?start_rank=3141
    :return: list of links to pages containing links to journals
    '''

    base_link = 'https://www.elsevier.com/catalog?page='
    start_rank = 1
    end_rank = 2
    step = 20

    data = []
    for i in range(start_rank, end_rank + 1, step):
        link = base_link + str(i)

        print ("[INFO] Fetching journals from ", link)
        data.extend(journal_info(link))

    print ("")
    print ("[INFO] Writing all output to CSV file ")

    import csv
    with open(r'C:\Users\pc\Desktop\resultat.csv', 'w') as csvfile:
        fields = ['title', 'link', 'ProductType', 'Edition', 'FirstPublished', 'Hardcover']
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()

        for d in data :
            writer.writerow({fields[0] : d[0], fields[1] : d[1], fields[2] : d[2], fields[3] : d[3],fields[4] : d[4],fields[5] : d[5]})

    print ("[INFO] Done writing CSV file")

fetch_all_jornals()