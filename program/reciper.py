import program.libs.databaseManager as db
import program.libs.itemManager as itemManager
import program.libs.recipeManager as recipeManager

def run():
    name = input("choose receipt to add ingredients: ")
    recipeadd = db.Recipes(name)
    add = recipeManager.RecipeAdder()
    
    while True:
        recipeadd.addRecipe(add.addIngredients(), add.addQuantity(), add.addUnit())
        
        ask = input('Add more? [y/n]: ')
        if ask == 'n':
            break
        
    recipeadd.con.close()
    