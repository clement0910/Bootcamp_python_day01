import datetime
from recipe import Recipe


class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        if isinstance(name, str):
            self.name = name
        else:
            print("Need string for name.")
            exit()
        if isinstance(last_update, datetime.datetime):
            self.last_update = last_update
        else:
            print("Need datetime for last_update.")
            exit()
        if isinstance(creation_date, datetime.datetime):
            self.creation_date = creation_date
        else:
            print("Need datetime for creation_date.")
            exit()
        if isinstance(recipes_list, dict):
            self.recipes_list = recipes_list
        else:
            print("Need dictionnaries for recipes_list.")
            exit()

    def get_recipe_by_name(self, name):
        for x in self.recipes_list:
            for y in self.recipes_list[x]:
                if y.name is name:
                    print(y)

    def get_recipes_by_types(self, recipe_type):
        for x in self.recipes_list[recipe_type]:
            print(str(x))

    def add_recipe(self, recipe):
        if isinstance(recipe, Recipe):
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.datetime.now()
        else:
            print("Enter a recipe")
