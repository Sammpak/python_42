# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_age.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/05 11:50:25 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/05 11:50:44 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_plant_age():
    plant_age = int(input("Enter plant age  in days: "))
    if (plant_age > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
