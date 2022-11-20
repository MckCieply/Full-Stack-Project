#Plotting avg mileage for each year of production, for each of models
#and paste it on homepage
import sqlite3 as sql
conn = sql.connect("C:/Users/mwppl/Desktop/Code/Full-Stack-Project/otofeature/deals.db")
c = conn.cursor()

c.execute("SELECT ROUND(avg(mileage)), model, year from Cars group by model, year order by model, year")
rows = c.fetchall()

for row in rows:
    print(row)