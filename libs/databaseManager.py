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

    def editItem(self, object, column, value):
        for x in self.cur.execute(f"SELECT name FROM fridge"):
            if object in x:
                self.cur.execute(f"""UPDATE fridge set 
                {column} = ?
                where name = ?""", (value, object))
                self.con.commit()
                return print(f'{column} for {object} updated to {value}!')
        print(f'{object} is not in your base!')

    def editItemRecord(self, object, name, quantity, unit, price):
        self.cur.execute("""UPDATE fridge set 
        name = ?,
        quantity = ?,
        unit = ?,
        price = ?
        where name = ?""", (name, quantity, unit, price, object))
        self.con.commit()

    def deleteItem(self, itemName):
        self.cur.execute("delete from fridge where name = ?", (itemName,))
        self.con.commit()

    def showItems(self):
        for x in self.cur.execute("SELECT * FROM fridge"):
            print(x)
        
################## recipes #################

class Recipes():
    
    con = sqlite3.connect("./database/recipes.db")
    cur = con.cursor()
    
    def __init__(self, recipe):
        self.cur.execute(f"create table if not exists {recipe} (ingredients text, quantity real, unit text)")
        self.con.commit()
        
    def addRecipe(self, recipeName, ingredients):
        self.cur.execute("insert into dinner values (?, ?, ?)", (addDate, recipeName, ingredients))
        self.con.commit()

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

