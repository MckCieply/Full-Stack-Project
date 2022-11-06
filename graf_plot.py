#plotting grafs year / avg price  AND  avg mileage / price
import sqlite3 as sql

conn = sql.connect("deals.db")
c = conn.cursor()

c.execute("SELECT price, year, mileage FROM cars")
result = c.fetchall()
price, year, mileage = [], [], []
for _ in result:
    price.append(int(_[0].replace(".", "")))
    year.append(_[1])
    mileage.append(int(_[2].replace(" ", "").strip("km")))
print (mileage)

conn.close()