# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/11 14:06:56 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/11 15:12:46 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


class Coordinate_error(Exception):
    def __init__(self, message: str = "Unknown coordinate error") -> None:
        self.message = message
        super().__init__(self.message)


def is_valid_format(input: str) -> bool:
    # format x,y,z    


    for c in input:
        while (c != ','):
            print(f"{c}")
            c += 1

    return True


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    argv: list[str] = sys.argv

    while (True):
        try:
            print("Get a first set of coordinates")
            coord_1: str = input("Enter new coordinates as floats in format 'x,y,z':")
            is_valid_format(coord_1)
        except Coordinate_error as e:
            print
            
    