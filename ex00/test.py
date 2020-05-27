from recipe import Recipe
from book import Book
import datetime


ingredients = ["steak", "pain", "fromage"]
salade = ["salade", "sauce"]
tiramisu = ["Too much things"]
list = {"starter": [], "lunch": [], "dessert": [], }
recipe1 = Recipe("Burger", 1, 10, ingredients, "Classic Burger", "lunch")
recipe2 = Recipe("Salade", 1, "5", salade, "Classic Salad", "starter")
recipe3 = Recipe("Tiramisu", 4, 60, tiramisu, "Classic Tiramisu 🇮🇹", "dessert")
book1 = Book("livre", datetime.datetime.now(), datetime.datetime.now(), list)
book1.add_recipe(recipe1)
book1.add_recipe(recipe2)
book1.add_recipe(recipe3)
book1.get_recipe_by_name("Tiramisu")
book1.get_recipes_by_types("dessert")
