# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plam <plam@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 18:07:19 by plam              #+#    #+#              #
#    Updated: 2020/03/12 20:17:16 by plam             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Book(object):
	def __init__(self, name, r_t):
		self.name = name		# class variable unique to each instance
		self.last_update = 0 #[datetime](https://docs.python.org/3/library/datetime.html)
		self.creation_date = 0 #[datetime](https://docs.python.org/3/library/datetime.html)
		self.recipe_type = r_t #a dictionnary with 3 keys: "starter", "lunch", "dessert". (dict)

	def get_recipe_by_name(self, name):
		"""Print a recipe with the name `name` and return the instance"""
		pass

	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		pass

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		pass