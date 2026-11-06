# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/05 11:57:06 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/06 12:25:26 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str) -> None:
        self.name = name
        self.age = 0
        self.height = 0

    def set_height(self, height: int):
        if (height < 0):
            print(f" {self.name} Error, height can't be negative")
            print("Height update rejected")
        else:
            self.height = height
            print(f"Heiht updated: {self.get_height()} cm")

    def set_age(self, age: int):
        if (age < 0):
            print(f" {self.name} Error, age can't be negative")
            print("Age update rejected")
        else:
            self.age = age
            print(f"Age updated: {self.get_age()} days")

    def get_height(self) -> int:
        return self.height

    def get_age(self) -> int:
        return self.age


def show(plant):
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    print("=== Garden Security Output ===")
    rose = Plant("Rose")
    print("current state:")
    show(rose)

    rose.set_height(25)
    rose.set_age(30)
    show(rose)

    rose.set_height(-5)
    rose.set_age(-10)
    print("current state:")
    show(rose)
