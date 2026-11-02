# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spaccaud <spaccaud@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/30 14:57:00 by spaccaud          #+#    #+#              #
#    Updated: 2026/11/02 12:36:29 by spaccaud         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive():
	days_until_harvest = int(input("Days until harvest: "))
	start_counting(days_until_harvest, 1)
	
def start_counting(days_until_harvest, current_day):
	if(days_until_harvest == 0):
		print("Harvest time!")
	elif(days_until_harvest == current_day):
		print(f"Day {current_day}")
		print("Harvest time!")
	elif(days_until_harvest > current_day):
		print(f"Day {current_day}")
		current_day = current_day + 1
		start_counting(days_until_harvest, current_day)
	