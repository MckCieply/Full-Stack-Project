#Plotting avg mileage for each year of production, for each of models
#and paste it on homepage
import sqlite3 as sql
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator as ML
import matplotlib.ticker as ticker
conn = sql.connect("C:/Users/mwppl/Desktop/Code/Full-Stack-Project/otofeature/deals.db")
c = conn.cursor()

c.execute("SELECT ROUND(avg(mileage)), model, year from Cars group by model, year order by model, year")
rows = c.fetchall()

fix, ax = plt.subplots()
avg_mileage = []
year = []
for row in rows:
    if(row[1] == "Scirocco"):
        avg_mileage.append(row[0])
        year.append(row[2])

ax.plot(year, avg_mileage, label = "Scirocco", linewidth = 2, marker =".", color="m" )

avg_mileage = []
year = []
for row in rows:
    if(row[1] == "Lancer"):
        avg_mileage.append(row[0])
        year.append(row[2])
ax.plot(year, avg_mileage, label = "Lancer", linewidth = 2, marker =".", color="red")

avg_mileage = []
year = []
for row in rows:
    if(row[1] == "c30"):
        avg_mileage.append(row[0])
        year.append(row[2])
ax.plot(year, avg_mileage, label = "c30", linewidth = 2, marker =".", color="lightblue")

ax.set_title("Average prices")                                              
ax.legend()
ax.set_xlabel("Year")
ax.set_ylabel("Avg. Mileage")
ax.yaxis.set_major_locator(ML(50000))
majors = ['50k','100k','150k','200k','250k','300k','350k','400k']
ax.yaxis.set_major_formatter(ticker.FixedFormatter(majors))
ax.xaxis.set_major_locator(ML(1))
ax.grid(True, linestyle="--")
# plt.savefig("otofeature\cardeals\static\MileagePlot.png")
plt.show()