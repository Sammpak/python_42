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
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = 1.0) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self._growth_rate = growth_rate
        self.set_height(height)
        self.set_age(age)
 
    def get_name(self) -> str:
        return self._name
 
    def get_height(self) -> float:
        return self._height
 
    def get_age(self) -> int:
        return self._age
 
    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(height)
 
    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
 
    def grow(self) -> None:
        self._height = round(self._height + self._growth_rate, 1)
 
    def age(self) -> None:
        self._age += 1
 
    def show(self) -> None:
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
