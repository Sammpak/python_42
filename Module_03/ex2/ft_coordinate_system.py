# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/11 14:06:56 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/13 13:11:11 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import math


class Coordinate_error(Exception):
    def __init__(self, message: str = "Unknown coordinate error") -> None:
        self.message = message
        super().__init__(self.message)


def is_valid_format_float(input: str) -> tuple[float, float, float]:
    # format "x.x,y.y,z.z"
    coord: list[float] = [0.0, 0.0, 0.0]
    i: int = 0
    is_negative: bool = False
    is_small_digit: bool = False
    decimals: int = 0
    digits: int = 0

    for c in input:
        if c == ',':
            i += 1
            if i > 2:
                raise Coordinate_error("Invalid syntax")
            is_negative = False
            is_small_digit = False
            decimals = 0
            digits = 0
        elif c == '-':
            is_negative = True
        elif c == '.':
            is_small_digit = True
        elif c in "0123456789":
            if is_small_digit:
                decimals += 1
            digits = digits * 10 + int(c)
            value: float = digits / 10 ** decimals  # decale le .
            if (is_negative):
                coord[i] = -value
            else:
                coord[i] = value
        else:
            raise Coordinate_error(f"Error on parameter '{c}': could not "
                                   f"convert string to float: '{c}'")

    if i != 2:
        raise Coordinate_error("Invalid syntax")
    return (coord[0], coord[1], coord[2])


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("")
    while (True):
        try:
            print("Get a first set of coordinates")
            coord: str = input("Enter new coordinates as "
                               "floats in format 'x,y,z': ")
            coord_1: list[float] = is_valid_format_float(coord)
            print(f"Got a first tuple: {coord_1}")
            print(f"It includes: X={coord_1[0]},Y={coord_1[1]},Z={coord_1[2]}")
            distance_center: int = math.sqrt((coord_1[0]-0.0)**2 +
                                             (coord_1[1]-0.0)**2 +
                                             (coord_1[2]-0.0)**2)
            print(f"distance from the center: {round(distance_center, 4)}")
            break
        except Coordinate_error as e:
            print(f"error: {e}")

    print("")

    while (True):
        try:
            print("Get a second set of coordinates")
            coord_2: str = input("Enter new coordinates as "
                                 "floats in format 'x,y,z: ")
            coord_2: list[float] = is_valid_format_float(coord_2)
            distance_beetwen: int = 0
            distance_beetwen = math.sqrt((coord_1[0]-coord_2[0])**2 +
                                         (coord_1[1]-coord_2[1])**2 +
                                         (coord_1[2]-coord_2[2])**2)
            print("Distance between the 2 sets of coordinates: "
                  f"{round(distance_beetwen, 4)}")
            break
        except Coordinate_error as e:
            print(f"error: {e}")
