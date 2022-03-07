import database.persistance as db


def addItem():
    item = input('Please input item name: ').lower()
    quantity =  input('Please input item quantity: ').lower()
    unit = input('Please input quantity unit: ').upper()

    db.addItem(item, quantity, unit)