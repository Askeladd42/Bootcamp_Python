# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plam <plam@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 12:40:23 by plam              #+#    #+#              #
#    Updated: 2020/03/09 17:23:25 by plam             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def rev_args(text):
	str = ""
	for i in range(len(text)-1, -1, -1):
		if text[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			str += text[i].lower()
		elif text[i] in "abcdefghijklmnopqrstuvwxyz":
			str += text[i].upper()
		else:
			str += text[i]
	return str

s_len = len(sys.argv)
if s_len > 1:
	final_str = ""
	while s_len > 1:
		chain = rev_args(str(sys.argv[s_len - 1]))
		final_str += chain
		s_len -= 1
		if s_len > 1:
			final_str += " "
	print(final_str)