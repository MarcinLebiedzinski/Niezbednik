class Ingredient:

    def __init__(self, name, protein, carbohydrates, fat):
        self.name = name
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat

    def __str__(self):
        return f'{self.name}'


class Meal:

    def __init__(self, name):
        self.name = name
        self.protein = 0
        self.carbohydrates = 0
        self.fat = 0
        self.ingredients_list = []
        self.calories = 0

    def __str__(self):
        return f'{self.name}'

    def add_ingredient(self, ingredient, amount):
        self.ingredients_list.append((ingredient.name, amount))
        self.protein += (amount / 100) * ingredient.protein
        self.carbohydrates += (amount / 100) * ingredient.carbohydrates
        self.fat += (amount / 100) * ingredient.fat

    def show_ingredients_and_nutrient(self):
        self.calories = round((self.protein * 4) + (self.carbohydrates * 4) + (self.fat * 9.4), 1)
        return f"""
        Ingredients: {self.ingredients_list}, 
        {self} contains: {self.protein}g protein, {self.carbohydrates}g carbohydrates, {self.fat}g fat. 
        Calories = {self.calories}kcal
        """


class DayMenu:

    def __init__(self, name):
        self.name = name
        self.protein = 0
        self.carbohydrates = 0
        self.fat = 0
        self.meal_list = []
        self.calories = 0

    def __str__(self):
        return f'{self.name}'

    def add_meal(self, meal):
        self.meal_list.append((meal.name, meal.ingredients_list))
        self.protein += meal.protein
        self.carbohydrates += meal.carbohydrates
        self.fat += meal.fat

    def show_menu(self):
        self.calories = round((self.protein * 4) + (self.carbohydrates * 4) + (self.fat * 9.4), 1)

        return f"""
        Meal: {self.meal_list},
        {self} contains: {self.protein}g protein, {self.carbohydrates}g carbohydrates, {self.fat}g fat.
        Total calories = {self.calories}kcal
        """


egg = Ingredient('egg', 13, 1.1, 11)
tomato = Ingredient('tomato', 0.9, 3.9, 0.2)
bread = Ingredient('bread', 9, 49, 3.2)
print(egg.protein)
print(egg.carbohydrates)
print(egg.fat)

scrambled_eggs = Meal('scrambled_eggs')
scrambled_eggs.add_ingredient(egg, 200)
scrambled_eggs.add_ingredient(tomato, 50)
print(scrambled_eggs.show_ingredients_and_nutrient())


sandwich = Meal('sandwich')
sandwich.add_ingredient(bread, 25)
sandwich.add_ingredient(tomato, 50)
print(sandwich.show_ingredients_and_nutrient())

very_minimalistic_menu = DayMenu('very_minimalistic_menu')
very_minimalistic_menu.add_meal(scrambled_eggs)
very_minimalistic_menu.add_meal(sandwich)
print(very_minimalistic_menu.show_menu())

