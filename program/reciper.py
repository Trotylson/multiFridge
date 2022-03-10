import program.libs.databaseManager as db
import program.libs.itemManager as itemManager
import program.libs.recipeManager as recipeManager

def run():
    recipe_name  = input("recipe name: ")
    recipe = db.Recipes(recipe_name)
    recipe.con.close()
    
    name = input("choose receipt to add ingredients: ")
    recipeadd = db.Recipes()
    add = recipeManager.RecipeAdder()
    recipeadd.addRecipe(name, add.addIngredients(), add.addQuantity(), add.addUnit())
    recipeadd.con.close()
    