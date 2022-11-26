
import requests
from bs4 import BeautifulSoup
import sqlite3 as sql
import time
start_time = time.time()

class Car():
    def __init__(self, brand, model, min_year, fuel_type, min_capacity, chasis):
        self.conn = sql.connect("C:/Users/mwppl/Desktop/Code/Full-Stack-Project/otofeature/deals.db")
        self.brand = brand
        self.model = model 
        self.min_year = min_year 
        self.fuel_type = fuel_type
        self.min_capacity = min_capacity
        self.chasis = chasis
        self.finding_last_page()
        self.all_deals()

    def finding_last_page(self):
        #Finding whether There is more than one page of deals
        URL = f"https://www.otomoto.pl/osobowe/{self.brand}/{self.model}/seg-{self.chasis}/od-{self.min_year}?search%5Bfilter_enum_fuel_type%5D={self.fuel_type}&search%5Bfilter_float_engine_capacity%3Afrom%5D={self.min_capacity}?page=1"
        request = requests.get(URL)
        soup = BeautifulSoup(request.content, 'html5lib')
        global last_page
        try:
            div = soup.find('div', {'class':'ooa-1oll9pn e19uumca7'})
            ul = div.find('ul', {'data-testid': 'pagination-list'})
            for li in ul.find_all('li', {'data-testid': 'pagination-list-item'}):
                last_page = int(li.a.span.text)
        except:
            last_page = 1
    def all_deals(self):  
        #Scrapping exact deals from page with all deals      
        counter = 0
        for page in range(1, last_page+1):
            URL = f'https://www.otomoto.pl/osobowe/{self.brand}/{self.model}/seg-{self.chasis}/od-{self.min_year}?search%5Bfilter_enum_fuel_type%5D={self.fuel_type}&search%5Bfilter_float_engine_capacity%3Afrom%5D={self.min_capacity}%3Fpage%3D1"&page={page}'
            request = requests.get(URL)
            soup = BeautifulSoup(request.content, 'html5lib')
            for div in soup.find_all('div',attrs={'class' : "ooa-1mxnix4 e1b25f6f15"}):
                self.deal_url = div.a["href"]
                #print(counter+1,".",self.deal_url)
                self.single_deal(self.deal_url)    
                counter +=1
        print(f"Total of {counter} deals ...")
        self.finish_commit()

    def single_deal(self,deal_url):
        #Scrapping directly from exact deal URL                      
        request = requests.get(deal_url)
        soup = BeautifulSoup(request.content, 'html5lib')
        span = soup.find('span', {"class":"offer-price__number"})
        self.price = span.contents[0].replace(" ", "")
        self.currency = span.contents[1].text

        span = soup.find_all('span', {'class':'offer-main-params__item'})
        self.year = span[0].text.strip()
        self.mileage = span[1].text.strip().replace(" ", "").strip("km")

        span = soup.find('span',{'class':'offer-meta__value'})
        self.add_date = span.contents[0]

        span = soup.find('span',{'id':'ad_id'})
        self.id = span.text
        self.db_query()

    def db_query(self):
        #Checking whether table is created, if not create one
        #Inserting into the table each single deal
        c = self.conn.cursor()
        try:    
            c.execute(f"""CREATE TABLE cars(id INT PRIMARY KEY, brand TEXT, model TEXT, price INT, currency TEXT, year INT, mileage INT, add_date TEXT, url TEXT)""")
        except:
            pass
        
        try:
            c.execute("""INSERT INTO  cars VALUES (?,?,?,?,?,?,?,?,?)""",(self.id, self.brand, self.model, self.price, self.currency, self.year, self.mileage, self.add_date, self.deal_url))
        except:
            pass
        
    def finish_commit(self):
        #Commiting bunch of ready inserts, once per car model
        self.conn.commit()

        print(f"Finishing... ")              
        self.conn.close()

scirocco = Car("Volkswagen", "Scirocco", "2008", "petrol", "1900", "")

lancer = Car("Mitsubishi", "Lancer", "2007", "petrol", "1700", "sedan")

c30 =  Car("Volvo", "c30","2008", "petrol", "", "")

if __name__ == "__main__":
    print(f"--- {round(time.time() - start_time, 2)} seconds ---")
