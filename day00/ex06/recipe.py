#!/usr/bin/env python
# -*- coding: utf-8 -*-

cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
    },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
    }
}


def printAll():
    for recipe in cookbook:
        printRecipe(recipe)


def printRecipe(recipe):
    if recipe in cookbook:
        print('\033[0;32mRecipe for {}:\033[0;0m'.format(recipe))
        print(' Ingredients list: {}'.format(cookbook[recipe]['ingredients']))
        print(' To be eaten for {}.'.format(cookbook[recipe]['meal']))
        print(
            ' Takes {} minutes of cooking.\n'.format(
                cookbook[recipe]['prep_time'])
        )
    else:
        print(
            '\033[1;31mRecipe {} is not in cookbook.\033[0;0m'.format(recipe))


def deleteRecipe(recipe):
    if recipe in cookbook:
        del cookbook[recipe]
        print('\033[0;32mRecipe {} deleted\033[0;0m'.format(recipe))
    else:
        print(
            '\033[1;31mRecipe {} is not in cookbook.\033[0;0m'.format(recipe))


def addRecipe(name, ingredients, meal, prep_time):
    time = None
    if prep_time.isdigit():
        time = int(prep_time)
    if name not in cookbook:
        if isinstance(time, int):
            cookbook[name] = {
                'ingredients': ingredients,
                'meal': meal,
                'prep_time': time
            }
            print(
                '\033[0;32mThe recipe {} was added to cookbook\033[0;0m'.
                format(name))
        else:
            print('\033[1;31mInvalid time value\033[0;0m')
    else:
        print('\033[1;31mThis recipe is already in cookbook\033[0;0m')


if __name__ == "__main__":
    while True:
        print('Please select an option by typing the corresponding number:')
        print('\033[1;34m1:\033[0;0m Add a recipe')
        print('\033[1;34m2:\033[0;0m Delete a recipe')
        print('\033[1;34m3:\033[0;0m Print a recipe')
        print('\033[1;34m4:\033[0;0m Print the cookbook')
        print('\033[1;34m5:\033[0;0m Quit')

        userInput = input()
        if userInput.isdigit():
            userInput = int(userInput)

        if userInput == 1:
            rName = input('Enter the recipe\'s name:\n')
            rIngre = input(
                'Enter the recipe\'s ingredients separates by space:\n'
                ).split()
            rMeal = input('Enter the type of meal:\n')
            rTime = input('Enter the preparation time in minutes:\n')
            addRecipe(rName, rIngre, rMeal, rTime)
        elif userInput == 2:
            rName = input('Enter the recipe\'s name to delete:\n')
            deleteRecipe(rName)
        elif userInput == 3:
            rName = input('Enter the recipe\'s name to print:\n')
            printRecipe(rName)
        elif userInput == 4:
            printAll()
        elif userInput == 5:
            print('\033[0;32mCookbook closed.\033[0;0m')
            break
        else:
            print('\033[1;31mThis option does not exist.\033[0;0m')
