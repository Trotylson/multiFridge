import sqlite3
from datetime import date

addDate = date.today()

con = sqlite3.connect('./database/fridge.db')
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS fridge (date text, name text, quantity real, unit text price real)")

def addItem(itemName, quantity, unit):
    cur.execute("insert into fridge values (?, ?, ?, ?)", (addDate, itemName, quantity, unit))
    con.commit()

def editItem():
    pass

def deleteItem():
    pass

def showItems():
    pass

