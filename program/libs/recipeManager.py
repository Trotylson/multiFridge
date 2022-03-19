
class RecipeAdder():
    
    def addIngredients(self):
        ingredients = input('input ingredient: ').lower()
        return ingredients
    
    def addQuantity(self):
        quantity = input('quantitty of an item: ')
        return quantity

    def addUnit(self):
        unit = input('units: ').lower()
        return unit
    
class RecipeDeleter():
    
    def deleteIngredient(self):
        ingredient = input('input ingredient to delete from recipe: ').lower()
        return ingredient
    
class RecipeEditor():
    def selectIngredient(self):
        object = input('Please select item name to edit params: ')
        return object
    
    def selectColumn(self):
        while True:
            column = input("Select parametr to change\ningredient name = i\nquantity = q\nunit = u\n: ")
            # if column == "i" or "q" or "u":
            #     return "ingredients" or "quantity" or "unit"
            if column == "i":
                return "ingredients"
            elif column == "q":
                return "quantity"
            elif column == "u":
                return "unit"
            else:
                print("Wrong parametr, please try again.")
            return column
    
    def setValue(self):
        value = input('Type value: ')
        return value