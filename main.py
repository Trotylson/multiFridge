import libs.databaseManager as db
import libs.itemManager as manager
import libs.dbSeed as dbSeed  # <---- to seed database

fridge = db.Fridge()
item = manager.ItemAdder()
deleter = manager.ItemDeleter()

print('Hello fridge :)')

# fridge.showItems()    # <--- show db

# fridge.deleteItem(deleter.deleteItem())  # <--- delete item

# while True:
    
#     fridge.addItem(item.addName(), item.addQuantity(), item.addUnit(), item.addPrice())
    
#     answer = input('Do you want to add another item? [Y/N]: ').lower()
#     if answer == 'y':
#         continue
#     else: break

# ########################### DATABASE SEEDER #####################################
# ######################### use only if needed ... ################################
# fridge.cur.execute("drop table fridge")  # <---- start seed database
# fridge.cur.execute("CREATE TABLE IF NOT EXISTS fridge (date text, name text, quantity real, unit text, price real)")
# for x in dbSeed.seed['items']:
#     fridge.addItem(x['name'], x['quantity'], x['unit'], x['price'])
# fridge.con.commit()     # <---- end database seeding
# print('Database seeded successfully!')
# #################################################################################
# #################################################################################

# print(dbSeed.seed['items'][0])
# for x in dbSeed.seed['items']:
#     print(x['name'])
    
fridge.con.close()
exit()

