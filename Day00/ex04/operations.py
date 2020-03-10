# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plam <plam@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 17:22:23 by plam              #+#    #+#              #
#    Updated: 2020/03/10 17:49:42 by plam             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from sys import argv as av

s_len = len(av)
if s_len == 3:
	try:
		a = int(av[1])
		b = int(av[2])
	except ValueError:
		print("InputError: only numbers")
		print("Usage: python operations.py <number1> <number2>")
		print("Example:")
		print("python operations.py 10 3")
		sys.exit(1)
	else:
		print("Sum:		" + str(a+b))
		print("Difference:	" + str(a-b))
		if b != 0:
			print("Product:	" + str(a*b))
			print("Quotient:	" + str(a/b))
			print("Remainder:	" + str(a%b))
		else:
			print("Product:	" + str(a*b))
			print("Quotient:	ERROR (div by 0)")
			print("Remainder:	ERROR (modulo by 0)")
else:
	if s_len > 3:
		print("InputError: too many numbers")
	print("Usage: python operations.py <number1> <number2>")
	print("Example:")
	print("python operations.py 10 3")
	sys.exit(1)