# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plam <plam@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 10:51:48 by plam              #+#    #+#              #
#    Updated: 2020/03/12 17:59:39 by plam             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

cookbook = {
	'sandwich' : {
		'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'],
		'meal' : 'lunch',
		'prep_time' : '10'
		},
	'cake' : {
		'ingredients' : ['flour', 'sugar', 'eggs'],
		'meal' : 'dessert',
		'prep_time' : '60'
		},
	'salad' : {
		'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
		'meal' : 'lunch',
		'prep_time' : '15'
	}
}

'''1.
print(cookbook.keys())
print(cookbook.values())
print(cookbook.items())
'''

#2.

def p_recipe(recipe):
	print("Recipe for " + recipe + ":")
	print("Ingredients list: " + str(cookbook[recipe]['ingredients']))
	print("To be eaten for " + cookbook[recipe]['meal'] + ".")
	print("Takes " + cookbook[recipe]['prep_time'] + " minutes of cooking.")

##p_recipe('cake')


#3.
def d_recipe(recipe):
	del cookbook[recipe]

##d_recipe('sandwich')
##print(cookbook.keys())

#4.

def add_recipe(r_name, r_ingr, r_meal, r_time):
	cookbook[r_name] = {
		'ingredients' : r_ingr,
		'meal' : r_meal,
		'prep_time' : r_time
		}
##add_recipe('vegetarian lasagnas', ['tomatoes', 'cashew nuts cream', 'spinach', 'lasagnas'], 'lunch/diner', '55')
##print(cookbook['vegetarian lasagnas'].items())

#5.

recipe_names = ""
cnt = 0
for i in cookbook:
	recipe_names += i
	cnt += 1
	if cnt < len(cookbook):
		recipe_names += ", "
##print(recipe_names)

#6.

p = input("Please select an option by typing the corresponding number:\n" 
		+ "1: Add a recipe\n" 
		+ "2: Delete a recipe\n" 
		+ "3: Print a recipe\n" 
		+ "4: Print the cookbook\n" 
		+ "5: Quit\n")
while p not in "12345":
	p = input("This option does not exist, please type the corresponding number.\nTo exit, enter 5.\n")
else:
	while p != "5":
		if p == "1":
			r = input("Please enter the recipe's name and  its details (ingredients, meal, preparation time):\n")
			if len(list(r)) == 4:
				add_recipe(r[0], r[1], r[2], r[3])
		elif p == "2":
			r = input("Please enter the recipe's name to delete:\n")
			if r in cookbook:
				d_recipe(r)
			else:
				while r != "5" or r not in cookbook:
					r = input("This option does not exist, please type the corresponding recipe.\n" +
								"To exit, enter 5.\n")
					if r == "5":
						print("Cookbook closed.")
						sys.exit(1)
		elif p == "3":
			r = input("Please enter the recipe's name to get its details:\n")
			while r != "5" and r not in cookbook:
				r = input("This option does not exist, please type the corresponding recipe.\n" +
							"To exit, enter 5.\n")
			if r == "5":
					print("Cookbook closed.")
					sys.exit(1)
			elif r in cookbook:
				p_recipe(r)
		elif p == "4":
			for i in cookbook:
				p_recipe(i)
				print("\n")
		p = input("")
	else:	
		print("Cookbook closed.")
		sys.exit(1)
	