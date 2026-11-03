# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sampak <sampak@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/11/02 17:42:09 by spaccaud          #+#    #+#              #
#    Updated: 2026/11/03 10:28:12 by sampak           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name, height, age, growth_rate):
        self.name = name
        self.age = age
        self.height = height
        self.growth_rate = growth_rate

def show(plant):
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")

def grow(plant):
    plant.height = round(plant.height + plant.growth_rate, 1)
    
def age(plant):
    plant.age += 1

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    rose = Plant("Rose", 25, 30, 0.8)
    sunflower = Plant("Sunflower", 80, 45, 1.2)
    cactus = Plant("Cactus", 15, 120, 0.5)

    for i in range(7):
        print(f"==== Day {i + 1} ====")
        grow(rose)
        age(rose)
        show(rose)
        grow(sunflower)
        age(sunflower)
        show(sunflower)
        grow(cactus)
        age(cactus)
        show(cactus)