# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/05 11:57:47 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/09 14:59:43 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str, age: int, height: float) -> None:
        self._name = name
        self._age = age
        self._height = height

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


class Vegetable(Plant):
    def __init__(self, harvest_season: str,
                 /, name: str, age: int, height: float) -> None:
        super().__init__(name, age, height)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self) -> None:
        self._height = round(self._height + 0.5, 1)
        self._nutritional_value += 1

    def celebrate_birthday(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


class Flower(Plant):
    def __init__(self, name: str, color: str,
                 /, age: int, height: float) -> None:
        super().__init__(name, age, height)
        self._color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        print(f"Color: {self._color}")
        if self._is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, trunk_diameter: int,
                 /, age: int, height: int) -> None:
        super().__init__(name, age, height)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              "{self._height}cm long "
              f"and {self._trunk_diameter}cm wide.")

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        print(f"Trunk Diameter: {self._trunk_diameter}cm")


if __name__ == "__main__":
    tree = Tree("Oak", 10, 5, 100)
    flower = Flower("Rose", "Red", 2, 1.0)
    vegetable = Vegetable("Spring", "Carrot", 1, 0.5)

    print("=== Garden Plant Types ===")

    print("Flower ===============")
    flower.show()
    print(f"[Asking the {flower.get_name()} to bloom]")
    flower.bloom()
    flower.show()

    print("Tree ===============")
    tree.show()
    print(f"[asking the {tree.get_name()} to produce shade]")
    tree.produce_shade()

    print("Vegetable ===============")
    vegetable.show()
    print(f"[make {vegetable.get_name()} grow and age for 20 days]")
    for _ in range(20):
        vegetable.grow()
        vegetable.celebrate_birthday()
    vegetable.show()
