# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spaccaud <spaccaud@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/30 14:47:03 by spaccaud          #+#    #+#              #
#    Updated: 2026/10/30 14:49:34 by spaccaud         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
	time_since_water = int(input("Days since last watering: "))
	if(time_since_water > 2):
		print("Water the plants!")
	else:
		print("Plants are fine")