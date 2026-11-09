# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/09 11:53:34 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/09 15:02:37 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def main() -> None:
    print("Testing PlantError...")
    try:
        raise PlantError("Caught PlantError: The tomato plant is wilting!")
    except PlantError as e:
        print(f"{e}")

    print("Testing WaterError...")
    try:
        raise WaterError("Caught WaterError: Not enough water in the tank!")
    except WaterError as e:
        print(f"{e}")

    print("Testing GardenError...")
    try:
        raise GardenError()
    except GardenError as e:
        print(f"{e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    main()
