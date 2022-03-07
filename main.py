import database.persistance as db
import scripts.addItem as addItem

print('Hello fridge :)')

while True:
    addItem.addItem()
    
    answer = input('Do you want to add another item? [Y/N]: ').lower()
    if answer == 'n':
        break

db.con.close()
exit()