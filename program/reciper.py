import program.libs.databaseManager as db
import program.libs.itemManager as itemManager
import program.libs.recipeManager as recipeManager

def run():
    recipe_name  = input("recipe name: ")
    recipe = db.Recipes(recipe_name)