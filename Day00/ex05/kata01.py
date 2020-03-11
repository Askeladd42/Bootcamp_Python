# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plam <plam@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 17:59:44 by plam              #+#    #+#              #
#    Updated: 2020/03/11 21:58:37 by plam             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

cnt = 0
val = languages.values()
print(val)
for i in languages:
	print(i + " was created by " + languages[i])
	cnt += 1