import program.libs.databaseManager as db
import program.libs.itemManager as itemManager
import program.libs.recipeManager as recipeManager
import program.scripts.imageFridge as image 

def main_reciper():
    image.cookbookImage()
    while True:
        ask = input(
            """This is the Cookbook! Here we can:\n
1. Create new recipe\n
2. Edit selected recipe\n
3. Delete recipe\n
4. See recipes\n
5. Check ingredients of a recipe\n
6. Lucky draw! Choose my meal!\n
            
Type an integer to select, or 'back' to back, or 'exit' to quit.\n
: """)
        
        if ask == 1:
            pass
        elif ask == 2:
            pass
        elif ask == 3:
            pass
        elif ask == 4:
            pass
        elif ask == 5:
            pass
        elif ask == 6:
            pass
        elif ask == "back":
            return
        elif ask == "exit":
            quit()
        else:
            continue

# ############## dodaje receptce lub dodaje do istniejacej #############
# def run():
#     name = input("name receipt to add ingredients: ").lower()
#     recipeadd = db.Recipes(name)
#     add = recipeManager.RecipeAdder()
        
#     while True:
#         recipeadd.addRecipe(
#             recipe = str(name),
#             ingredient = add.addIngredients(),
#             quantity = add.addQuantity(),
#             unit = add.addUnit())
            
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
# def show_recipe():
#     while True:
#         name = input("type recipe to show list of ingredients: ").lower()
#         show = db.Recipes(name)
#         show.showRecipe()
            
#         ask = input("chcesz sprawdzic inny przepis [y/n]?: ")
#         if ask == 'n':
#             break
    
# show_recipe()
#######################################################
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
########################################################################
################# show tables(recipes)################################
# show = db.Recipes(recipe = None)
# show.showTables()
########################################################################
#################### edycja przepisu ###################################
# name = input("wprowadz przepis: ")
# recka = db.Recipes(name)
# reckaEdit = recipeManager.RecipeEditor()
# recka.editRecipe(reckaEdit.selectIngredient(), reckaEdit.selectColumn(), reckaEdit.setValue())
########################################################################