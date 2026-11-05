# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/05 11:56:55 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/05 11:57:01 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name, height, age, growth_rate):
        self.name = name
        self.age = age
        self.height = height
        self.growth_rate = growth_rate


def show(plant):
    print(f"Created: {plant.name}: {plant.height}cm, {plant.age} days old")


def grow(plant):
    plant.height = round(plant.height + plant.growth_rate, 1)


def age(plant):
    plant.age += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30, 0.8)
    sunflower = Plant("Sunflower", 80, 45, 1.2)
    cactus = Plant("Cactus", 15, 120, 0.5)
    oak = Plant("Oak", 200, 365, 0.1)
    fern = Plant("Fern", 15, 120, 0.3)

    print("=== Plant Factory Output ===")
    show(rose)
    show(sunflower)
    show(cactus)
    show(oak)
    show(fern)
