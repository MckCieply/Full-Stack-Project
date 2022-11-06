#plotting grafs year / avg price  AND  avg mileage / price
import sqlite3 as sql
import matplotlib.pyplot as plt

conn = sql.connect("deals.db")
c = conn.cursor()

c.execute("SELECT price, year, mileage FROM cars")
result = c.fetchall()
price, year, mileage = [], [], []
for row in result:
    price.append(int(row[0].replace(".", "")))
    year.append(row[1])
    mileage.append(int(row[2].replace(" ", "").strip("km")))

#Gotta get AVG smhow dunno how yet

conn.close()


# print(max_year, min_year)
# plt.plot(price, year)
# plt.show()

