# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plam <plam@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 18:07:25 by plam              #+#    #+#              #
#    Updated: 2020/03/12 20:19:12 by plam             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#from book import Book
from recipe import Recipe

salad_r = Recipe("salad", 1, 15, "starter")
print(salad_r.name, salad_r.cooking_level, salad_r.cooking_time, salad_r.recipe_type, sep=", ")