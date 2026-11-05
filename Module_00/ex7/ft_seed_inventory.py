# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_seed_inventory.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/05 11:52:57 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/05 11:53:44 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit == "packets"):
        result = f"{quantity} packets available"
    elif (unit == "grams"):
        result = f"{quantity} grams total"
    elif (unit == "area"):
        result = f"cover {quantity} square meters"
    else:
        result = f"{quantity} Unknown unit type"
    print(f"{seed_type.title()} seeds: {result}")
