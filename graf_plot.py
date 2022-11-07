#plotting grafs year / avg price  AND  avg mileage / price
import sqlite3 as sql
import matplotlib.pyplot as plt

conn = sql.connect("deals.db")
c = conn.cursor()

c.execute("SELECT year, avg(price) FROM cars GROUP BY year")
result = c.fetchall()
year = []
avg_price = []
avg_mileage = []
for row in result:
    year.append(row[0])
    avg_price.append(round(row[1], 3))

c.execute("SELECT year, avg(mileage) FROM cars GROUP BY year")
result = c.fetchall()
for row in result:
    avg_mileage.append(round(row[1], 3))
conn.close()
plt.grid(True, linestyle="--")
plt.plot(year, avg_price, color='red')
plt.ylabel("Average Price")
plt.xlabel("Year")
plt.show()

plt.plot(year, avg_mileage) 


