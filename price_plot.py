#Plotting avg price for each year of production, for each of models
#paste plot on home page
import sqlite3 as sql
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator as ML
import matplotlib.ticker as ticker
import numpy as np
conn = sql.connect("C:/Users/mwppl/Desktop/Code/Full-Stack-Project/otofeature/deals.db")
c = conn.cursor()

c.execute("SELECT ROUND(avg(price)), model, year from Cars group by model, year order by model, year")

rows = c.fetchall()
fig, ax = plt.subplots()
avg_prices = []
year = []
# for row in rows:
#     if row[1] == "Scirocco":
#         short = str(row[0]).rstrip("000")
#         avg_prices.append(short)
#         year.append(row[2])
# print (avg_prices)
for row in rows:
    if row[1] == "Scirocco":
        avg_prices.append(row[0])
        year.append(row[2])
ax.plot(year, avg_prices, label = "Scirocco", linewidth = 2, marker = ".")
avg_prices = []
year = []
for row in rows:
    if row[1] == "Lancer":
        avg_prices.append(row[0])
        year.append(row[2])
ax.plot(year, avg_prices, label = "Lancer", linewidth = 2, marker = ".")
avg_prices = []
year = []
for row in rows:
    if row[1] == "c30":
        avg_prices.append(row[0])
        year.append(row[2])
ax.plot(year, avg_prices, label = "c30", linewidth = 2, marker = ".")
ax.set_title("Average prices")
ax.legend()
ax.set_xlabel("Year")
ax.set_ylabel("Avg. Mileage")
ax.yaxis.set_major_locator(ML(10000))
majors = ['10k','20k','30k','40k','50k','60k','70k','80k','90k','100k']
ax.yaxis.set_major_formatter(ticker.FixedFormatter(majors))
ax.xaxis.set_major_locator(ML(1))
ax.grid(True, linestyle="--" )
plt.show()