# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_water_reminder.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/05 11:51:11 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/05 11:51:12 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_water_reminder():
    time_since_water = int(input("Days since last watering: "))
    if (time_since_water > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
