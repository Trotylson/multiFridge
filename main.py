import database.persistance as db
import scripts.addItem as addItem

print('Hello fridge :)')

while True:
    addItem.addItem()
    
    answer = input('Do you want to add another item? [Y/N]: ').lower()
    if answer == 'y':
        continue
    else: break

db.con.close()
exit()

# TODO: 
    # create database infrastructure - adequate to the intentions   <=  dzikitatus  done.
    # create database library                                       <=  Trotylson
    # create 'addItem' function                                     <=  Trotylson   done.
    # create 'editItem' function                                    <=  dzikitatus
    # create 'deleteItem' function                                  <=  dzikitatus