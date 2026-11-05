# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/05 11:57:47 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/05 11:58:14 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name, age, height):
        self.name = name
        self._age = age
        self.height = height


class Vegetable(Plant):
    def __init__(self, harvest_season, name, age, height):
        self.harvest_season = harvest_season
        self.nutritional_value = 0
        super().__init__(name, age, height)

    def grow(self):
        self.nutritional_value = self.nutritional_value + 1

    def age(self):
        self._age = self._age + 1
        self.nutritional_value = self.nutritional_value + 1

    def show(self):
        print(f"{self.name}: {self.height}cm, {self._age} days old")
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


class Flower(Plant):
    def __init__(self, name, color, age, height):
        self.color = color
        self.is_blooming = False
        super().__init__(name, age, height)

    def bloom(self):
        self.is_blooming = True

    def show(self):
        print(f"{self.name}: {self.height}cm, {self._age} days old")
        print(f"Color: {self.color}")
        if (self.is_blooming):
            print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, trunk_diameter, age, height):
        self.trunk_diameter = trunk_diameter
        super().__init__(name, age, height)

    def produce_shape(self):
        print(f"Tree {self.name} now produces a shade of {self.height}cm long and {self.trunk_diameter}cm wide.")

    def show(self):
        print(f"{self.name}: {self.height}cm, {self._age} days old")
        print(f"Trunk Diameter: {self.trunk_diameter}cm")


if __name__ == "__main__":
    tree = Tree("Oak", 10, 5, 100)
    flower = Flower("Rose", "Red", 2, 1)
    vegetable = Vegetable("Spring", "Carrot", 1, 0.5)

    print("=== Garden Plant Types ===")

    print("Flower ===============")
    flower.show()
    print(f"[Asking the {flower.name} to bloom]")
    flower.bloom()
    flower.show()

    print("Tree ===============")
    tree.show()
    print(f"[asking the {tree.name} to produce shade]")
    tree.produce_shape()

    print("Vegetable ===============")
    vegetable.show()
    print(f"[make {vegetable.name} grow and age for 20 days]")
    for i in range(20):
        vegetable.grow()
        vegetable.age()
    vegetable.show()
