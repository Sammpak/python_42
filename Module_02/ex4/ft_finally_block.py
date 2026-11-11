# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_finally_block.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/10 15:34:46 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/11 11:51:56 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


class Watering_error(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> bool:
    if (plant_name[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        print(f"Watering {plant_name} [OK]")
        return True
    else:
        raise Watering_error("Caught PlantError: Invalid plant name to "
                             f"water: {plant_name}")


def test_watering_system(list_plant: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in list_plant:
            water_plant(plant)
    except Watering_error as e:
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
