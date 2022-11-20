#Plotting avg price for each year of production, for each of models
#paste plot on home page
import sqlite3 as sql
import matplotlib.pyplot as plt
import numpy as np
conn = sql.connect("C:/Users/mwppl/Desktop/Code/Full-Stack-Project/otofeature/deals.db")
c = conn.cursor()

c.execute("SELECT ROUND(avg(price)), model, year from Cars group by model, year order by model, year")

rows = c.fetchall()
avg_prices = []
year = []
for row in rows:
    if row[1] == "Scirocco":
        avg_prices.append(row[0])
        year.append(row[2])
plt.plot(year, avg_prices, label = "Scirocco")
avg_prices = []
year = []
for row in rows:
    if row[1] == "Lancer":
        avg_prices.append(row[0])
        year.append(row[2])
plt.plot(year, avg_prices, label = "Lancer")
avg_prices = []
year = []
for row in rows:
    if row[1] == "c30":
        avg_prices.append(row[0])
        year.append(row[2])
plt.plot(year, avg_prices, label = "c30")

plt.legend()
plt.show()