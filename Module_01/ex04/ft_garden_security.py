# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sampak <sampak@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/11/02 17:42:09 by spaccaud          #+#    #+#              #
#    Updated: 2026/11/03 11:16:40 by sampak           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.height = 0

    
    def set_height(self, height):
        if(height < 0):
            print(f" {self.name} Error, height can't be negative")
            print("Height update rejected")
        else:
            self.height = height

    def set_age(self, age):
        if(age < 0):
            print(f" {self.name} Error, age can't be negative")
            print("Age update rejected")
        else:
            self.age = age
    
    def get_height(self):
        return self.height
    
    def get_age(self):
        return self.age
    

def show(plant):
    print(f"Created: {plant.name}: {plant.height}cm, {plant.age} days old")

if __name__ == "__main__":
    print("=== Garden Security Output ===")
    rose = Plant("Rose")
    rose.set_height(25)
    rose.set_age(30)
    show(rose)

    rose.set_height(30)
    rose.set_age(35)
    show(rose)

    rose.set_height(-5)
    rose.set_age(-10)
    show(rose)