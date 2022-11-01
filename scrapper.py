#Choose scirocco / lancer x
#Scrape it
#make it look nice
#store it in DB
import requests
from bs4 import BeautifulSoup
brand = "volkswagen"
model = "scirocco"
min_year = "2008"
fuel_type = "petrol"#petrol
min_capacity = "1900"#1900
def finding_last_page(brand, model, min_year, fuel_type, min_capacity):
    URL = f"https://www.otomoto.pl/osobowe/{brand}/{model}/od-{min_year}?search%5Bfilter_enum_fuel_type%5D={fuel_type}&search%5Bfilter_float_engine_capacity%3Afrom%5D={min_capacity}?page=1"
    request = requests.get(URL)
    soup = BeautifulSoup(request.content, 'html5lib')
    div = soup.find('div', {'class':'ooa-1oll9pn e19uumca7'})
    ul = div.find('ul', {'data-testid': 'pagination-list'})
    for li in ul.find_all('li', {'data-testid': 'pagination-list-item'}):
        global last_page
        last_page = int(li.a.span.text)
def all_deals(brand, model, min_year, fuel_type, min_capacity, last_page):        
    counter = 1
    for page in range(1, last_page+1):
        deals_counter = 0
        URL = f'https://www.otomoto.pl/osobowe/{brand}/{model}/od-{min_year}?search%5Bfilter_enum_fuel_type%5D={fuel_type}&search%5Bfilter_float_engine_capacity%3Afrom%5D={min_capacity}%3Fpage%3D1"&page={page}'
        request = requests.get(URL)
        soup = BeautifulSoup(request.content, 'html5lib')
        for div in soup.find_all('div',attrs={'class' : "ooa-le0vtj e1b25f6f14"}):
            deals_counter +=1
            deal_url = div.a["href"]
            print(counter,".",deal_url)
            single_deal(deal_url)

            counter +=1
def single_deal(deal_url):                      #extract price/ production year/ transmision/ mileage
    request = requests.get(deal_url)
    soup = BeautifulSoup(request.content, 'html5lib')
    span = soup.find('span', {"class":"offer-price__number"})
    price = span.contents[0].strip()
    currency = span.contents[1].text

    span = soup.find_all('span', {'class':'offer-main-params__item'})
    year = span[0].text.strip()
    mileage = span[1].text.strip()
    print(price, currency, year, mileage)


finding_last_page(brand, model, min_year, fuel_type, min_capacity)
all_deals(brand, model, min_year, fuel_type, min_capacity, last_page)
