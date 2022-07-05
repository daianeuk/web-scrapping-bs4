import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://pt.wikipedia.org/wiki/Quadro_de_medalhas_dos_Jogos_Olímpicos')

#print(page.status_code) 
#print(page.content) 

#soup = BeautifulSoup(page.content, 'html.parser') 
#print(soup.prettify())

wiki_text = page.text

soup = BeautifulSoup(wiki_text, 'html.parser')

#print(len(soup.find_all('table')))

tab = soup.find("table",{"class":"wikitable sortable"})

#print(tab)


header_tags = tab.find_all('th')
headers = [header.text.strip() for header in header_tags]
print(headers)

rows = []

data_rows = tab.find_all('tr')

for row in data_rows:
    value = row.find_all('td')
    beautiful_value = [dp.text.strip() for dp in value]
    print(beautiful_value)

    if len(beautiful_value) == 0:
        continue

    rows.append(beautiful_value)


with open('olympics.csv', 'w', newline="") as output:
    writer  = csv.writer(output)
    writer.writerow(headers)
    writer.writerows(rows)