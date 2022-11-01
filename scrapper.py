#Choose scirocco / lancer x
#Scrape it
#make it look nice
#store it in DB
import requests
from bs4 import BeautifulSoup

def finding_last_page(URL):
    request = requests.get(URL)
    soup = BeautifulSoup(request.content, 'html5lib')
    div = soup.find('div', attrs = {'class':'ooa-1oll9pn e19uumca7'})
    ul = div.find('ul', attrs={'data-testid': 'pagination-list'})
    for li in ul.find_all('li', attrs={'data-testid': 'pagination-list-item'}):
        global last_page
        last_page = int(li.a.span.text)

brand = "volkswagen"
model = "scirocco"
page = 1
URL = f"https://www.otomoto.pl/osobowe/{brand}/{model}?page={page}"
finding_last_page(URL)
counter = 1
for page in range(1, last_page):
    URL = f"https://www.otomoto.pl/osobowe/{brand}/{model}?page={page}"
    request = requests.get(URL)
    soup = BeautifulSoup(request.content, 'html5lib')
    for div in soup.find_all('div',attrs={'class' : "ooa-le0vtj e1b25f6f14"}):
        print(counter,".",div.a["href"])
        counter +=1
# div = soup.find('div', attrs = {'class':'ooa-1oll9pn e19uumca7'})
# ul = soup.find('ul', attrs={'data-testid': 'pagination-list'})
# for li in ul.find_all('li', attrs={'data-testid': 'pagination-list-item'}):
#     all_pages = int(li.a.span.text)
    
# print(all_pages)
