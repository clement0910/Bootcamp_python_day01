# self.name = name if isinstance(name, str) else exit()
class Recipe:

    def __init__(self, name, cooking_lvl,
                 cooking_time, ingredients, description, recipe_type):
        if isinstance(name, str):
            self.name = name
        else:
            print("Need string for name.")
            exit()
        if isinstance(cooking_lvl, int) and cooking_lvl < 6\
           and cooking_lvl > 0:
            self.cooking_lvl = cooking_lvl
        else:
            print("Need a number between 1 and 5 for cooking_lvl")
            exit()
        if str(cooking_time).isdigit() is True:
            self.cooking_time = cooking_time
        else:
            print("Need a number in minutes.")
            exit()
        if isinstance(ingredients, list):
            self.ingredients = ingredients
        else:
            print("Need list for ingredients.")
            exit()
        self.description = description
        if isinstance(recipe_type, str):
            if recipe_type is "starter" or recipe_type is "lunch"\
               or recipe_type is "dessert":
                self.recipe_type = recipe_type
            else:
                print("Unknow recipe type, pls write: lunch, dessert, starter")
                exit()
        else:
            print("Need string for name.")
            exit()

    def __str__(self):
        string = "Name of the recipe: {}\n".format(self.name)
        string += "- Cooking Lvl: {}\n".format('⭐' * self.cooking_lvl)
        string += "- Cooking Time: {} minutes\n".format(self.cooking_time)
        string += "- Ingredients: {}\n".format(self.ingredients)
        string += "- Description: {}\n".format(self.description)
        string += "- Type of recipe: {}".format(self.recipe_type)
        return string
