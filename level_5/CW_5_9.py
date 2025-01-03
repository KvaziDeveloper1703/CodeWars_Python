"""
Pete loves baking cakes, but he's not great at math. Help him figure out how many cakes he can bake given a recipe and the available ingredients.
Write a function cakes(recipe, available) that:
+ Takes two arguments:
    + recipe: an object with the required ingredients and their amounts.
    + available: an object with the available ingredients and their amounts.
+ Returns the maximum number of cakes Pete can bake (as an integer).
+ If an ingredient in the recipe is missing in the available object, consider its amount as 0.

Example:
Input: cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
Output: 2 (Pete can bake 2 cakes).

Пит обожает печь торты, но он плохо считает. Помогите ему узнать, сколько тортов он сможет испечь, имея рецепт и доступные ингредиенты.
Напишите функцию cakes(recipe, available), которая:

+ Принимает два аргумента:
    + recipe: объект с необходимыми ингредиентами и их количеством.
    + available: объект с доступными ингредиентами и их количеством.
+ Возвращает максимальное количество тортов, которое сможет испечь Пит (в виде целого числа).
+ Если какого-то ингредиента из рецепта нет в объекте available, считайте его количество равным 0.

Пример:
Ввод: cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
Вывод: 2 (Пит сможет испечь 2 торта).

https://www.codewars.com/kata/525c65e51bf619685c000059
"""

def cakes(recipe, available):
    max_cakes = float('inf')

    for ingredient, required_amount in recipe.items():
        if ingredient not in available:
            return 0
        else:
            max_cakes = min(max_cakes, available[ingredient] // required_amount)

    return max_cakes

print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))
print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"sugar": 1200, "eggs": 5, "milk": 200}))