# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/05 11:57:06 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/09 16:23:59 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str) -> None:
        self._name = name
        self._age = 0
        self._height = 0

    def set_height(self, height: int):
        if (height < 0):
            print(f" {self._name} Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Heiht updated: {self.get_height()} cm")

    def set_age(self, age: int):
        if (age < 0):
            print(f" {self._name} Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self.get_age()} days")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self):
        print(f"{self._name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security Output ===")
    rose = Plant("Rose")
    print("current state:")
    rose.show()

    rose.set_height(25)
    rose.set_age(30)
    rose.show()

    rose.set_height(-5)
    rose.set_age(-10)
    print("current state:")
    rose.show()
