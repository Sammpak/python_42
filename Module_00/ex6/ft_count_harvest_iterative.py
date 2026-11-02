# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spaccaud <spaccaud@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/30 14:51:25 by spaccaud          #+#    #+#              #
#    Updated: 2026/11/02 13:46:17 by spaccaud         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
	until_harvest = range(0, int(input("Days until harvest: ")))
	for num in until_harvest:
		print(f"Day {num + 1}")
	print("Harvest time!")