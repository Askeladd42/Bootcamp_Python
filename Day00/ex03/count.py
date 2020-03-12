# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plam <plam@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 19:59:10 by plam              #+#    #+#              #
#    Updated: 2020/03/12 11:17:36 by plam             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# cas arg vide et multi args à patcher

import sys
from inspect import signature

def text_analyzer(text=None):
	"""This a very useful function to detail the number of each type of 
		character (even spaces) used on it.
		No that is not a line for slacking!
	"""
	if len(sys.argv) > 2
	if text:
		lcase = 0
		ucase = 0
		p_marks = 0
		sp = 0

		t_len = len(text)
		if t_len > 0:
			for i in range(t_len):
				if text[i] in "abcdefghijklmnopqrstuvwxyz":
					lcase += 1
				elif text[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
					ucase += 1
				elif text[i] in ".:;?!,":
					p_marks += 1
				elif text[i] == " ":
					sp += 1
				i += 1
			print("The text contains " + str(i) + " characters:")
		if ucase > 0:
			print("- " + str(ucase) + " upper letters")
		if lcase > 0:
			print("- " + str(lcase) + " lower letters")
		if p_marks > 0:
			print("- " + str(p_marks) + " punctuation marks")
		if sp > 0:
			print("- " + str(sp) + " spaces")
	elif text == None:
		print("What is the text to analyse?")
		text = input("")
		text_analyzer(text)
	else:
		print("ERROR")
		sys.exit(1)