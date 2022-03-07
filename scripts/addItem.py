import database.persistance as db


def addItem():
    item = input('Please input item name: ').lower()
    quantity = input('Please input item quantity: ')
    unit = input('Please input quantity unit: ').upper()
    price = input('Please input price: ')

    db.addItem(item, quantity, unit, price)