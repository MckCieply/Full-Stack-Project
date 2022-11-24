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

fig, ax = plt.subplots()
avg_mileage = []
year = []
for row in rows:
    if(row[1] == "Scirocco"):
        avg_mileage.append(row[0])
        year.append(row[2])

ax.plot(year, avg_mileage, label = "Scirocco", linewidth = 2, marker =".", color="magenta" )

avg_mileage = []
year = []
for row in rows:
    if(row[1] == "Lancer"):
        avg_mileage.append(row[0])
        year.append(row[2])
ax.plot(year, avg_mileage, label = "Lancer", linewidth = 2, marker =".", color="white")

avg_mileage = []
year = []
for row in rows:
    if(row[1] == "c30"):
        avg_mileage.append(row[0])
        year.append(row[2])
ax.plot(year, avg_mileage, label = "c30", linewidth = 2, marker =".", color="black")

titleparams = {
'fontsize': 20,
 'fontweight':'bold',
 'color': 'white',
 'verticalalignment': 'baseline',
 'horizontalalignment': 'center'}
ax.set_title("Average mileage", color="white", fontdict=titleparams)
                                              
ax.legend()
ax.set_xlabel("Year", color="white")
ax.set_ylabel("Avg. Mileage", color="white")
ax.yaxis.set_major_locator(ML(50000))
majors = ['50k','100k','150k','200k','250k','300k','350k','400k']
ax.yaxis.set_major_formatter(ticker.FixedFormatter(majors))
ax.xaxis.set_major_locator(ML(1))
ax.yaxis.set_minor_locator(ML(25000))
ax.grid(True, linestyle="--", color="#00607a" )
ax.set_facecolor("#002029")
fig.set_facecolor('#00303d')

ax.spines['left'].set_color('white')
ax.spines['bottom'].set_color('white')
ax.tick_params(which="both", colors="white")
ax.tick_params(which="minor", length = 5)
ax.tick_params(which="major", length = 8)
plt.savefig("otofeature\cardeals\static\MileagePlot.png")
#plt.show()