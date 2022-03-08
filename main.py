import libs.databaseManager as db
import libs.itemManager as manager

fridge = db.Fridge()
item = manager.ItemAdder()

print('Hello fridge :)')

while True:
    
    fridge.addItem(item.addName(), item.addQuantity(), item.addUnit(), item.addPrice())
    
    answer = input('Do you want to add another item? [Y/N]: ').lower()
    if answer == 'y':
        continue
    else: break

fridge.con.close()
exit()

# TODO: 
    # create database infrastructure - adequate to the intentions   <=  dzikitatus  done.
    # create database library                                       <=  Trotylson
    # create 'addItem' function                                     <=  Trotylson   done.
    # create 'editItem' function                                    <=  dzikitatus
    # create 'deleteItem' function                                  <=  dzikitatus