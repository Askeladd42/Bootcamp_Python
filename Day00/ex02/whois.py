# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plam <plam@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 17:24:23 by plam              #+#    #+#              #
#    Updated: 2020/03/09 19:53:58 by plam             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from sys import argv as av

s_len = len(av)
if s_len == 2:
	try:
		n = int(av[1])
	except ValueError:
		print("ERROR")
		sys.exit(1)
	else:
		if n == 0:
			print("I'm Zero.")
		elif n % 2 == 0:
			print("I'm Even.")
		else :
			print("I'm Odd.")
else:
	print("ERROR")