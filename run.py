# import program.reciper as recipe
# import program.fridge as fridge
import time
import program.scripts.imageFridge as welcome
import program.reciper as rcp

welcome.printImage()
time.sleep(1)
def main():
    while True:
        choice = input("""Type 'fridge' to open the Fridge
                    \nType 'cookbook' to open the Cookbook
                    \nType 'exit' to close the program
                    \n:""").lower()

        if choice == "fridge":
            pass
        elif choice == "cookbook":
            rcp.main_reciper()
        elif choice == "exit":
            quit()
        else:
            continue
main()



# fridge.run()
# recipe.run()