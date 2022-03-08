
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
    
    
class ItemEditor(): # <== # well, I'm not sure it's good conception...
    
    def editName(self):
        pass
    
    def editQuantity(self):
        pass
    
    def editUnit(self):
        pass
    
    def editPrice(self):
        pass
    
    
class ItemDeleter():
    
    def deleteItem(self):
        pass
    
    
class ItemDisplayer():
    
    def displayItem(self):
        pass