# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plam <plam@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 18:07:22 by plam              #+#    #+#              #
#    Updated: 2020/03/12 20:06:33 by plam             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Recipe(object):
	def __init__(self, name, c_l, c_t, r_t):
		self.name = name					# class variable unique to each instance
		self.cooking_level = c_l
		self.cooking_time = c_t
		self.ingredients = []
		self.description = None
		self.recipe_type = r_t

	def __str__(self):
		print(self.description)
		txt = ""
		return txt
