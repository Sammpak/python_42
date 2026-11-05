# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_count_harvest_iterative.py                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/05 11:51:34 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/05 11:51:56 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_count_harvest_iterative():
    until_harvest = range(0, int(input("Days until harvest: ")))
    for num in until_harvest:
        print(f"Day {num + 1}")
    print("Harvest time!")
