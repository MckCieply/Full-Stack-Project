#Plotting avg mileage for each year of production, for each of models
#and paste it on homepage
import sqlite3 as sql
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator as ML
import matplotlib.ticker as ticker
conn = sql.connect("./otofeature/deals.db")
c = conn.cursor()

c.execute("SELECT ROUND(avg(mileage)), model, year from Cars group by model, year order by model, year")
rows = c.fetchall()

fig, ax = plt.subplots()
def single_plot(brand):
    single_plot.avg_mileage = [row[0] for row in rows if row[1] == brand]
    single_plot.year = [row[2] for row in rows if row[1] == brand]
    
single_plot("Scirocco")
ax.plot(single_plot.year, single_plot.avg_mileage, label = "Scirocco", linewidth = 2, marker = ".", color="magenta")
single_plot("Lancer")
ax.plot(single_plot.year, single_plot.avg_mileage, label = "Lancer", linewidth = 2, marker =".", color="white")
single_plot("c30")
ax.plot(single_plot.year, single_plot.avg_mileage, label = "c30", linewidth = 2, marker =".", color="blue")

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