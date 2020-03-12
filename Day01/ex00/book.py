# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plam <plam@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 18:07:19 by plam              #+#    #+#              #
#    Updated: 2020/03/12 19:04:17 by plam             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Book(object):
	def __init__(self, name):
		self.name = name		# class variable unique to each instance
		self.last_update = [datetime](https://docs.python.org/3/library/datetime.html)
		self.creation_date = [datetime](https://docs.python.org/3/library/datetime.html)
		self.recipe_type =  a dictionnary why 3 keys: "starter", "lunch", "dessert". (dict)

	def get_recipe_by_name(self, name):
    """Print a recipe with the name `name` and return the instance"""
    pass

	def get_recipes_by_types(self, recipe_type):
    """Get all recipe names for a given recipe_type """
    	pass

	def add_recipe(self, recipe):
    """Add a recipe to the book and update last_update"""
    	pass