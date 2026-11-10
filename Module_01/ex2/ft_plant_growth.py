# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/05 11:56:24 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/10 15:17:45 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str, height: float, age: int,
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

    def get_height(self) -> float:
        return self._height


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")

    rose = Plant("Rose", 25.0, 30, 0.8)
    start_height = rose.get_height()
    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()

    growth = round(rose.get_height() - start_height, 1)
    print(f"Growth this week: {growth}cm")
