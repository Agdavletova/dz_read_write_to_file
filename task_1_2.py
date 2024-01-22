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


def get_shop_list_by_dishes(menu, number_persons):
    ingredients_dict = {}
    for dish_in_list in menu:
        for dish, ingredients in cook.items():
            if dish == dish_in_list:
                for ingredient in ingredients:
                    name = ingredient['ingredient_name']
                    if name in ingredients_dict:
                        q = number_persons * int(ingredient['quantity'])
                        previous_q = int(ingredients_dict[name]['quantity'])
                        ingredients_dict[name]['quantity'] = str(q + previous_q)
                    else:
                        q = number_persons * int(ingredient['quantity'])
                        ingredients_dict[name] = {'measure': ingredient['measure'], 'quantity': q}
    res = dict(sorted(ingredients_dict.items()))
    return res


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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
cook = creating_dict(dishes)
print(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 3))

