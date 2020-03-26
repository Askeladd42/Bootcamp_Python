# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plam <plam@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/24 17:13:38 by plam              #+#    #+#              #
#    Updated: 2020/03/24 20:30:07 by plam             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
import sys

def ft_progress(lst):
	

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)
