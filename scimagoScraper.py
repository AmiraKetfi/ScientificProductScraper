from urllib.request import urlopen
from bs4 import BeautifulSoup

base_link = 'http://www.scimagojr.com/journalrank.php?page='
journals = []

def scrap_values(link):

    try :
        page = urlopen(link).read()
        soup = BeautifulSoup(page, 'html.parser')
        soup.text
        table = soup.find('table')
        rows = table.find_all('tr')

        # remove header
        rows.pop(0)

        for row in rows :
            tds = row.find_all('td')

            serial_number = tds[0].text
            title = tds[1].text
            type = tds[2].text
            sjr = tds[3].text
            h_index = tds[4].text
            total_docs = tds[5].text
            total_docs_3 = tds[6].text
            total_refs = tds[7].text
            total_cites = tds[8].text
            citable_docs_3 = tds[9].text
            cites_docs_2 = tds[10].text
            ref_doc = tds[11].text
            country = tds[12].find('img')['title']

            journal = [serial_number, title, type, sjr, h_index, total_docs, total_docs_3, total_refs, total_cites, citable_docs_3, cites_docs_2, ref_doc, country]
            journals.append(journal)

    except :
        pass


def fetch_all_jornals() :
    start_page = 0
    end_page = 28606

    for i in range(start_page, end_page + 1):
        link = base_link + str(i)

        print ("[Note] Scraping journals from ", link)
        scrap_values(link)

    print ("")
    print ("[Note] Writing output to CSV file ")

    import csv
    with open('output/scimago.csv', 'w') as csvfile:
        fields = ['serial_number',
            'title',
            'type',
            'sjr',
            'h index',
            'total docs 2016',
            'total docs 3 years',
            'total refs',
            'total cites 3 years',
            'citable docs 3 years',
            'cites / docs 2 years',
            'ref / doc',
            'country' ]
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()

        for journal in journals :
            # normalize title
            journal[1] = journal[1].encode("utf-8")

            # write output
            writer.writerow(dict(zip(fields, journal)))

    print ("[Note] Done writing CSV file")


fetch_all_jornals()
