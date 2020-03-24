# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plam <plam@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/23 15:58:48 by plam              #+#    #+#              #
#    Updated: 2020/03/24 17:11:44 by plam             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import random
from sys import argv as av
from random import randint as r_int

inp = 0
cnt = 0
answer = r_int(1, 99)
print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")
while inp != answer:
	inp = input("What's your guess between 1 and 99?\n")
	if not inp.isdigit() and inp != "exit":
		print("That's not a number.")
	elif inp == "exit":
		print("Goodbye!")
		sys.exit(1)
	else:
		inp = int(inp)
		if inp < answer:
			print("Too low!")
		if inp > answer:
			print("Too high!")
		cnt += 1
else:
	if inp == 42 and answer == 42:
		print("The answer to the ultimate question of life, the universe and everything is 42.")
	cnt += 1
	if cnt == 1:
		print("Congratulations! You got it on your first try!")
	else:
		print("Congratulations, you've got it!")
		print("You won in " + str(cnt) + " attempts!")