#plotting grafs year / avg price  AND  avg mileage / price
import sqlite3 as sql

conn = sql.connect("deals.db")
c = conn.cursor()



conn.close()