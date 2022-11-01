#Choose scirocco / lancer x
#Scrape it
#make it look nice
#store it in DB

import requests
from bs4 import BeautifulSoup
brand = "volkswagen"
model = "scirocco"
URL = f"https://www.otomoto.pl/osobowe/{brand}/{model}"
request = requests.get(URL)
soup = BeautifulSoup(request.content, 'html5lib')
offer_links = []
for div in soup.find_all('div',attrs={'class' : "ooa-le0vtj e1b25f6f14"}):
    print(div.a["href"])
