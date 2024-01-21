# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# def creatinf_dict(list):
def creating_dict(list):
    cook_book = {}
    for recipe in dishes:
        recipe = recipe.split("\n")
        key = recipe[0]
        quantity_ingredients = int(recipe[1])
        ingredients = []
        i = 2
        for iterator in range(quantity_ingredients):
            ingredients_string = recipe[i]
            ss = ingredients_string.split(" | ")
            dic = {'ingredient_name': ss[0], 'quantity': ss[1], 'measure': ss[2]}
            ingredients.append(dic)
            i += 1
        cook_book[key] = ingredients
    return cook_book


with open('file.txt') as f:
    data = f.readlines()
    dishes = []
    recipes = ""
    for dish in data:
        if dish == "\n":
            dishes.append(recipes)
            recipes = ""
            continue
        recipes = recipes + dish


print(creating_dict(dishes))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
