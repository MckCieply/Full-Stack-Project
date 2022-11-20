#Plotting avg price for each year of production, for each of models
#paste plot on home page
import sqlite3 as sql

conn = sql.connect("C:/Users/mwppl/Desktop/Code/Full-Stack-Project/otofeature/deals.db")
c = conn.cursor()

c.execute("SELECT ROUND(avg(price)), model, year from Cars group by model, year order by model, year")

rows = c.fetchall()

for row in rows:
    print(row)