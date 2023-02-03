import json

def convert_to_json(recipe_file):
    recipes = []
    current_recipe = {}
    with open(recipe_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line == "":
                continue
            if line.upper().startswith("NAME"):
                if current_recipe:
                    recipes.append(current_recipe)
                current_recipe = {}
                current_recipe['name'] = line.split('-')[0].strip()
            elif line.upper().startswith("INGREDIENTS"):
                ingredients = []
                while True:
                    line = next(lines).strip()
                    if line == "":
                        break
                    ingredients.append({"name": line.split(" ")[-1], "amount": line.split(" ")[0]})
                current_recipe['ingredients'] = ingredients
            elif line.upper().startswith("INSTRUCTIONS"):
                instructions = []
                while True:
                    line = next(lines).strip()
                    if line == "":
                        break
                    instructions.append(line)
                current_recipe['instructions'] = instructions
    if current_recipe:
        recipes.append(current_recipe)
    return recipes

def save_json_files(recipes):
    for recipe in recipes:
        recipe_file = recipe['name'].lower().replace(" ", "_") + ".json"
        with open(recipe_file, 'w') as file:
            json.dump(recipe, file)

if __name__ == "__main__":
    recipe_file = input("Enter the recipe file name: ")
    recipes = convert_to_json(recipe_file)
    save_json_files(recipes)
    print("Recipes converted to JSON and saved as separate files")