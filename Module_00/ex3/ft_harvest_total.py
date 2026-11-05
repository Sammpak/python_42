# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_harvest_total.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/05 11:50:06 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/05 11:50:18 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_harvest_total():
    day_1 = int(input("Day 1 harvest: "))
    day_2 = int(input("Day 2 harvest: "))
    day_3 = int(input("Day 3 harvest: "))
    print(f"Total harvest : {day_1 + day_2 + day_3}")
