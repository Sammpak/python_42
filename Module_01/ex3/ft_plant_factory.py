# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/05 11:56:55 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/10 15:17:11 by spaccaud        ###   ########.fr        #
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
        print(f"Created: {self._name}: {self._height}cm, {self._age} days old")

    def grow(self) -> None:
        self._height = round(self._height + self._growth_rate, 1)

    def age(self) -> None:
        self._age += 1


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()
 
    rose.set_height(25)
    print(f"Height updated: {rose.get_height()}cm")
    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days")
    print()
 
    rose.set_height(-5)
    rose.set_age(-10)
    print()
 
    print("Current state: ", end="")
    rose.show()
    print()
