# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plam <plam@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 17:59:40 by plam              #+#    #+#              #
#    Updated: 2020/03/11 01:27:14 by plam             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

t = (19, 42, 21)
s_len = len(t)
s1 = "The " + str(s_len) + " numbers are : "
for i in range (s_len):
	s1 += str(t[i])
	if i < s_len-1:
		s1 += ", "
print(s1)