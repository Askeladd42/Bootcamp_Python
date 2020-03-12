# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata03.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plam <plam@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 23:55:21 by plam              #+#    #+#              #
#    Updated: 2020/03/12 10:07:26 by plam             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#enlever le \n a la fin

phrase = "The right format"
padding = ""
limit = 0
if len(phrase) < 42:
	limit = 42 - len(phrase)
for i in range (limit):
	padding += "-"
display = padding + phrase
print(display, end="")