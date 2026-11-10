# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_finally_block.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/10 15:34:46 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/10 16:13:27 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


class Wathering_error(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> bool:
    if (plant_name[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        print(f"Wathering {plant_name} [OK]")
        return True
    return False


def test_watering_system(list_plant: list):
    print("Opening watering system")
    try:
        for plant in list_plant_valid:
            if (water_plant(plant) is False):
                raise Wathering_error(f"Caught PlantError: Invalid plant"
                                      f" name to water: '{plant}'")
    except Wathering_error as e:
        print(f"{e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print("Testing valid plants...")
    list_plant_valid = ["Tomtato", "Lettuce", "Carrots"]
    test_watering_system(list_plant_valid)
    print("")
    print("Testing invalid plants...")
    list_plant_valid = ["Tomtato", "lettuce", "Carrots"]
    test_watering_system(list_plant_valid)
    print("Cleanup always happens, even with errors!")
