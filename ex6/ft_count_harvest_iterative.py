# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spaccaud <spaccaud@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/30 14:51:25 by spaccaud          #+#    #+#              #
#    Updated: 2026/10/30 14:57:19 by spaccaud         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
	until_harvest = int(input("Days until harvest: "))
	i = 1
	while(i <= until_harvest):
		print(f"Day {i}")
		i = i + 1
	print("Harvest time!")