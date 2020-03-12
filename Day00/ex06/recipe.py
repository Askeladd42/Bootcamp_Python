# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plam <plam@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 10:51:48 by plam              #+#    #+#              #
#    Updated: 2020/03/12 12:11:47 by plam             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
	print(cookbook[recipe])

#p_recipe('cake')
'''3.

'''

'''4.

'''

'''5.

'''

'''6.

'''