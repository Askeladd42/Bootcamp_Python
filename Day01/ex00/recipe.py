# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plam <plam@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 18:07:22 by plam              #+#    #+#              #
#    Updated: 2020/03/12 18:41:55 by plam             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Recipe(object):
	def __init__(self, name):
		self.name = name		# class variable unique to each instance
		self.cooking_level = 1
		self.cooking_time = 0
		self.ingredients = []
		self.description = None
		self.recipe_type = "starter"
	def __str__(self):
		print(self.description)
		txt = ""
		return txt
