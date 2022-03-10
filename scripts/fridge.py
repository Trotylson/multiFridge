import libs.databaseManager as db
import libs.itemManager as manager
import libs.dbSeed as dbSeed  # <---- to seed database
import scripts.imageFridge as imageFridge


fridge = db.Fridge()
item = manager.ItemAdder()
editor = manager.ItemEditor()
deleter = manager.ItemDeleter()


print('\nHello fridge :)')


imageFridge.printImage()


# image.printImage()

# fridge.editItem(editor.selectItem(), editor.selectColumn(), editor.setValue()) # <---- edititem wybierz nazwe do zmiany -> kolumne -> wartosc

# fridge.editItem(editor.selectItem(), editor.editName(), editor.editQuantity(), editor.editUnit(), editor.editPrice())  # <---- edititem caly wiersz

# fridge.showItems()    # <--- show db

# fridge.deleteItem(deleter.deleteItem())  # <--- delete item

# while True:
    
#     fridge.addItem(item.addName(), item.addQuantity(), item.addUnit(), item.addPrice())
    
#     answer = input('Do you want to add another item? [Y/N]: ').lower()
#     if answer == 'y':
#         continue
#     else: break

# ########################### DATABASE fridge table SEEDER #####################################
# ######################### use only if needed ... ################################
# fridge.cur.execute("drop table fridge")  # <---- start seed database
# fridge.cur.execute("CREATE TABLE IF NOT EXISTS fridge (date text, name text, quantity real, unit text, price real)")
# for x in dbSeed.seed['items']:
#     fridge.addItem(x['name'], x['quantity'], x['unit'], x['price'])
# fridge.con.commit()     # <---- end database seeding
# print('Database seeded successfully!')
# #################################################################################


# print(dbSeed.seed['items'][0])
# for x in dbSeed.seed['items']:
#     print(x['name'])
    
fridge.con.close()
exit()

