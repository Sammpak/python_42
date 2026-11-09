# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/09 16:51:56 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/09 16:52:18 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Statistic:
    def __init__(self, nbr_grow: int, nbr_show: int, nbr_age: int) -> None:
        self._nbr_grow = nbr_grow
        self._nbr_show = nbr_show
        self._nbr_age = nbr_age

    def add_show(self) -> None:
        self._nbr_show += 1

    def add_grow(self) -> None:
        self._nbr_grow += 1

    def add_age(self) -> None:
        self._nbr_age += 1


class Plant(Statistic):
    def __init__(self, name: str, age: int, height: int, nbr_grow: int = 0, nbr_show: int = 0, nbr_age: int = 0) -> None:
        super().__init__(nbr_grow, nbr_show, nbr_age)
        self._name: str = name
        self._age: int = age
        self._height: int = height

    def age_plant(self) -> None:
        self._age += 1
        self.add_age()

    def grow_plant(self) -> None:
        self._height += 1
        self.add_grow()

    def show_plant(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        self.add_show()

    @staticmethod
    def check_age(age_in_day: int) -> bool:
        return age_in_day > 365


class Flower(Plant):
    def __init__(self, name: str, color: str, age: int, height: int, nbr_grow: int = 0, nbr_show: int = 0, nbr_age: int = 0) -> None:
        super().__init__(name, age, height, nbr_grow, nbr_show, nbr_age)
        self.color: str = color
        self.is_blooming: bool = False

    def bloom(self, seed_count: int) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show_plant()
        print(f" Color: {self.color}")
        if self.is_blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


if __name__ == "__main__":
    print("=== Garden statistic ===")
    print("=== Flower ===")
    new_rose = Flower("rose", "red", 10, 15)

    new_rose.show()
    print(f"Show count recorded in stats: {new_rose._nbr_show}")
    new_rose.show()    
    print(f"Show count recorded in stats: {new_rose._nbr_show}")
