
class ItemAdder():
    
    def addName(self):
        name = input('Please input item name: ').lower()
        return name
    
    def addQuantity(self):
        quantity = input('Please input item quantity: ')
        return quantity
    
    def addUnit(self):
        unit = input('Please input quantity unit: ').lower()
        return unit
    
    def addPrice(self):
        price = input('Please input price: ')
        return price
    
    
class ItemEditor():
    
    def selectItem(self):
        object = input('Please select item name to edit params: ')
        return object
    
    def selectColumn(self):
        column = input("Type item parametr to change: ")
        return column
    
    def setValue(self):
        value = input('Type value: ')
        return value
#########################################################################
    def editName(self):
        name = input('Type item name to edit params: ')
        return name
    
    def editQuantity(self):
        quantity = input('Type item quantity to edit params: ')
        return quantity
    
    def editUnit(self):
        unit = input('Type item unit to edit params: ')
        return unit
    
    def editPrice(self):
        price = input('Type item price to edit params: ')
        return price
    
    
class ItemDeleter():
    
    def deleteItem(self):
        object = input("Enter item name to delete: ")
        return object
    
    
class ItemDisplayer():
    
    def displayItem(self):
        pass