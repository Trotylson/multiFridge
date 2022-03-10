import libs.databaseManager as db
import libs.itemManager as itemManager
import libs.recipeManager as recipeManager

recipe_name  = input("recipe name: ")
recipe = db.Recipes(recipe_name)