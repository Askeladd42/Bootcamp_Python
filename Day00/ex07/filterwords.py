# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plam <plam@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 18:02:59 by plam              #+#    #+#              #
#    Updated: 2020/03/21 16:54:27 by plam             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from sys import argv as av
import string
import re

"""Using list comprehensions, you will have to make a program that removes all the words in a string that are shorter than or equal to n letters, and returns the filtered list with no punctuation.
The program will accept only two parameters: a string, and an integer n.
"""

def lst_filling(av):
	str = re.sub('['+string.punctuation+']', '', av[1]) # enleve les ponctuations de la string et met les mots dans une liste
	lst = str.split()
	for i in lst:
		if len(i) < int(av[2]):
			lst.remove(i)
	return lst

if len(av) != 3 or av[1].isdigit == True or av[2].isdigit() == False:
	print("ERROR")
	sys.exit(1)
elif av[1] == "":
	print("Empty string")
	sys.exit(1)
else:
	print(lst_filling(av))