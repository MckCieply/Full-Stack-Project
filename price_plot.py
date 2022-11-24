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
ax.plot(year, avg_prices, label = "Scirocco", linewidth = 2, marker = ".", color="magenta")
avg_prices = []
year = []
for row in rows:
    if row[1] == "Lancer":
        avg_prices.append(row[0])
        year.append(row[2])
ax.plot(year, avg_prices, label = "Lancer", linewidth = 2, marker = ".", color="white")
avg_prices = []
year = []
for row in rows:
    if row[1] == "c30":
        avg_prices.append(row[0])
        year.append(row[2])
ax.plot(year, avg_prices, label = "c30", linewidth = 2, marker = ".", color="black")

titleparams = {                                                             #Title parameters
'fontsize': 20,
 'fontweight':'bold',
 'color': 'white',
 'verticalalignment': 'baseline',
 'horizontalalignment': 'center'}
ax.set_title("Average prices", fontdict=titleparams, color="white")         #Set graph title

ax.legend()                                                                 #Show legend
ax.set_xlabel("Year", color="white")                                        #Show x label
ax.set_ylabel("Avg. Mileage", color="white")                                #show y label
ax.yaxis.set_major_locator(ML(10000))                                       #set range between marks on y
majors = ['10k','20k','30k','40k','50k','60k','70k','80k','90k','100k']     #custom values for y
ax.yaxis.set_major_formatter(ticker.FixedFormatter(majors))                 #use custom values for y
ax.xaxis.set_major_locator(ML(1))                                           #set range between marks on x
ax.set_facecolor("#002029")                                                 #graph background color
fig.set_facecolor('#00303d')                                                #background behind axes
ax.grid(True, linestyle="--", color="#00607a" )                             #set grid 

ax.spines['left'].set_color('white')                                        #white x 'n' y axes
ax.spines['bottom'].set_color('white')
ax.tick_params(which="both", colors="white")                                #customization of ticks
ax.tick_params(which="major", length = 8)

plt.savefig("otofeature\cardeals\static\PricePlot.png")                     #save plot
#plt.show()