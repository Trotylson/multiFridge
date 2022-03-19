import program.libs.databaseManager as db
import program.libs.itemManager as itemManager
import program.libs.recipeManager as recipeManager

# ############## dodaje receptce lub dodaje do istniejacej #############
# def run():
#     name = input("name receipt to add ingredients: ").lower()
#     recipeadd = db.Recipes(name)
#     add = recipeManager.RecipeAdder()
        
#     while True:
#         recipeadd.addRecipe(add.addIngredients(), add.addQuantity(), add.addUnit())
            
#         ask = input('Add more? [y/n]: ')
#         if ask == 'y':
#             pass
#         elif ask == 'n':
#             break
#         else:
#             continue
            
#     recipeadd.con.close()
# run()  
#################################################################
################## pokazuje stół z przepisem (przepis)#########
def show_recipe():
    while True:
        name = input("type recipe to show list of ingredients: ").lower()
        show = db.Recipes(name)
        show.showRecipe()
            
        ask = input("chcesz sprawdzic inny przepis [y/n]?: ")
        if ask == 'n':
            break
    
show_recipe()
########################################################
############### delete table(recipe)###########
# def delete_recipe():
#     while True:
#         name = input("enter recipe name to delete: ").lower()
#         delRecipe = db.Recipes(name)
#         delRecipe.deleteRecipe()
#         print("recipe deleted succesfuly")

#         ask = input("chcesz usunąć kolejny przepis [y/n]?: ")
#         if ask == 'n':
#             break
#     delRecipe.con.close() 
# delete_recipe()
#######################################################
##################delete skladnik z receipta ################
# name = input("input receipt name to delete ingredients: ").lower()
# deleterow = db.Recipes(name)
# deleter = recipeManager.RecipeDeleter()
# deleterow.deleteRow(deleter.deleteIngredient())
# db.Recipes(name).deleteRow(deleter.deleteIngredient)
########################################################################
################# show tables(recipes)################################
# show = db.Recipes()
# show.showTables()
### /\ proba kiedy w klasie - nie dziala? ### \/ kiedy def przed klasą - działa #####
# db.showTables()
########################################################################
#################### edycja przepisu ###################################
# name = input("wprowadz przepis: ")
# recka = db.Recipes(name)
# reckaEdit = recipeManager.RecipeEditor()
# recka.editRecipe(reckaEdit.selectIngredient(), reckaEdit.selectColumn(), reckaEdit.setValue())
########################################################################