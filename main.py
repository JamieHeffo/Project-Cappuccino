import os
import json

#Initialise empty list to store recipes
recipes = []
shopping = []

current_dir = os.getcwd()
#path to recipes folder
recipe_dir = os.path.join(current_dir, "Recipes")


#Iterate through JSON files
try:
    for filename in os.listdir(recipe_dir):
        if filename.endswith(".json"):
            #Build path to file
            file_path = os.path.join(recipe_dir, filename)

            #Open file and read contents
            with open(file_path, "r") as file:

                #Load JSON file into dictionary
                recipe_data = json.load(file)

                #append list of recipes with files read
                recipes.append(recipe_data)
    
except:
     print("Could not open file")
     print(current_dir)
     print(recipe_dir)

#Menu
def menu():
    print("-----------------------")
    print("Please Choose an Option")
    print("-----------------------")
    print("1 : List all Recipes")
    print("2 : Print Recipe")
    print("3 : Create Shopping List")
    print("-----------------------")
    option = input("Selection : ")
    print("-----------------------")

    if (option == "1"):
        printRecipe()
        menu()

    if (option == "2"):
        fetchRecipe()

    if (option == "3"):
        addToList()
    
    else:
        print("Invalid Selection : Please Try Again")
        menu()

#Print all Recipes
def printRecipe():
    for index, recipe in enumerate(recipes):
        recipeNo = index + 1
        print("{}. {}".format(recipeNo, recipe["name"]))

#Retreive Specific Recipe
def fetchRecipe():

    recipe_name = input("Recipe Name : ")

    for recipe in recipes:
        if recipe["name"] == recipe_name:

            #Print recipe data
            print("Name : ", recipe["name"])
            print("Ingredients : \n")

            for ingredient in recipe["ingredients"]:
                print(" - {} ({}g".format(ingredient["name"], ingredient["amount"]))

        else:
            print("Recipe Not Found")

#Add Recipe to shopping list
def addToList():

    while(True):

        for index, recipe in enumerate(recipes):
            recipeNo = index + 1
            print("{}. {}".format(recipeNo, recipe["name"]))
        print("-----------------------")

        #Simluate Flashing Cursor
        for i in range(10):
            cursor = "|" if i % 2 == 0 else " "
            selection = input("Recipe Number : ")# + cursor + "\r")

            #If the selection is a valid recipe index
            if selection.strip() in [str(recipeNo) for index in range(len(recipes))]:
                #return true
                break

        #Valid selection made
        break

    selected_recipe = int(selection) - 1

    #Add ingredients of the selected recipe to shopping list
    for ingredient in recipes[selected_recipe]["ingredients"]:
        shopping.append("{} {}g".format(ingredient["name"], ingredient["amount"]))

    print("Selection : ", recipes[selected_recipe]["name"])
    print("Ingredients\n", shopping)
        

            
                            



menu()
            