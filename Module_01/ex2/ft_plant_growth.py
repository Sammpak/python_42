# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/05 11:56:24 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/09 16:45:37 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str, height: int, age: int,
                 /, growth_rate: float) -> None:
        self._name = name
        self._age = age
        self._height = height
        self._growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def grow(self) -> None:
        self._height = round(self._height + self._growth_rate, 1)

    def age(self) -> None:
        self._age += 1


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    rose = Plant("Rose", 25, 30, 0.8)
    sunflower = Plant("Sunflower", 80, 45, 1.2)
    cactus = Plant("Cactus", 15, 120, 0.5)

    for i in range(7):
        print(f"==== Day {i + 1} ====")
        rose.grow()
        rose.show()
        rose.age()
        sunflower.grow()
        sunflower.show()
        sunflower.age()
        cactus.grow()
        cactus.show()
        cactus.age()
