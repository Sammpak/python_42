# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/05 11:56:24 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/06 10:49:35 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str, height: int, age: int,
                 /, growth_rate: float) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.growth_rate = growth_rate


def show(plant) -> None:
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


def grow(plant) -> None:
    plant.height = round(plant.height + plant.growth_rate, 1)


def age(plant) -> None:
    plant.age += 1


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    rose = Plant("Rose", 25, 30, 0.8)
    sunflower = Plant("Sunflower", 80, 45, 1.2)
    cactus = Plant("Cactus", 15, 120, 0.5)

    for i in range(7):
        print(f"==== Day {i + 1} ====")
        grow(rose)
        age(rose)
        show(rose)
        grow(sunflower)
        age(sunflower)
        show(sunflower)
        grow(cactus)
        age(cactus)
        show(cactus)
