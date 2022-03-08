import sqlite3
from datetime import date

addDate = date.today()

class Fridge:
    
    con = sqlite3.connect('./database/fridge.db')
    cur = con.cursor()
    
    def __init__(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS fridge (date text, name text, quantity real, unit text, price real)")
        self.con.commit()

    def addItem(self, itemName, quantity, unit, price):
        self.cur.execute("insert into fridge values (?, ?, ?, ?, ?)", (addDate, itemName, quantity, unit, price))
        self.con.commit()

    def editItem(self):
        pass

    def deleteItem(self):
        pass

    def showItems(self):
        pass

# addDate = date.today()

# con = sqlite3.connect('./database/fridge.db')
# cur = con.cursor()

# cur.execute("CREATE TABLE IF NOT EXISTS fridge (date text, name text, quantity real, unit text, price real)")

# def addItem(itemName, quantity, unit, price):
#     cur.execute("insert into fridge values (?, ?, ?, ?, ?)", (addDate, itemName, quantity, unit, price))
#     con.commit()

# def editItem():
#     pass

# def deleteItem():
#     pass

# def showItems():
#     pass

