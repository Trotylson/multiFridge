import program.libs.databaseManager as db
import program.libs.itemManager as itemManager
import program.libs.recipeManager as recipeManager

# ############## dodaje receptce lub dodaje do istniejacej #############
# def run():
#     name = input("name receipt to add ingredients: ")
#     recipeadd = db.Recipes(name)
#     add = recipeManager.RecipeAdder()
        
#     while True:
#         recipeadd.addRecipe(add.addIngredients(), add.addQuantity(), add.addUnit())
            
#         ask = input('Add more? [y/n]: ')
#         if ask == 'n':
#             break
            
#     recipeadd.con.close()
           
#################################################################

################## pokazuje stół z przepisem (przepis)#########
# def show_recipe():
    # while True:
    #     name = input("type recipe to show list of ingredients: ")
    #     show = db.Recipes(name)
    #     show.showRecipe()
            
    #     ask = input("chcesz sprawdzic inny przepis [y/n]?: ")
    #     if ask == 'n':
    #         break
    # show.con.close()
########################################################

############### delete table(recipe)###########
# def delete_recipe():
#     while True:
#         name = input("enter recipe name to delete: ")
#         delRecipe = db.Recipes(name)
#         delRecipe.deleteRecipe()
#         print("recipe deleted succesfuly")

#         ask = input("chcesz usunąć kolejny przepis [y/n]?: ")
#         if ask == 'n':
#             break
#     delRecipe.con.close() 
# delete_recipe()
#######################################################

name = input("input receipt name to delete ingredients: ").lower()
deleterow = db.Recipes(name)
deleter = recipeManager.RecipeDeleter()
# kutang = deleter.deleteIngredient()
deleterow.deleteRow(deleter.deleteIngredient())

# db.Recipes(name).deleteRow(deleter.deleteIngredient)