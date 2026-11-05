# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/04 12:43:22 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/05 15:45:05 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    class statistic:
        def __init__(self):
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0
            self.produce_shade_count = 0

        def increment_grow(self):
            self.grow_count += 1

        def increment_age(self):
            self.age_count += 1

        def increment_show(self):
            self.show_count += 1

        def increment_shade(self):
            self.produce_shade_count += 1

        def show_statistic(self):
            print(f"Stats: {self.grow_count} grow,")
            print(f"{self.age_count} age, {self.show_count} show")
            if self.produce_shade_count >= 1:
                print(f"{self.produce_shade_count} shade")

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        self.stats = self.statistic()

    def _grow(self):
        self.stats.increment_grow()

    def _age(self):
        self.stats.increment_age()

    def _show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        self.stats.increment_show()

    @staticmethod
    def check_age(age_in_day):
        return age_in_day > 365


class Anonymous(Plant):
    def __init__(self, name=None, age=None, height=None):
        super().__init__(
            name or "Unknown plant",
            age or 0,
            height or 0
        )


class Vegetable(Plant):
    def __init__(self, harvest_season, name, age, height):
        super().__init__(name, age, height)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self):
        self.nutritional_value += 1
        self._grow()

    def age_plant(self):
        self.age += 1
        self.nutritional_value += 1
        self._age()

    def show(self):
        self._show()


class Seed:
    def __init__(self, number_of_seeds, parent_name, color):
        self.number_of_seeds = number_of_seeds
        self.parent_name = parent_name
        self.color = color

    def show(self):
        print(f"Seed from {self.parent_name} ({self.color}):")
        print(f"{self.number_of_seeds} items packaged.")


class Flower(Plant):
    def __init__(self, name, color, age, height):
        super().__init__(name, age, height)
        self.color = color
        self.is_blooming = False
        self.seeds = None

    def bloom(self, seed_count):
        self.is_blooming = True
        self.seeds = Seed(seed_count, self.name, self.color)

    def show(self):
        self._show()
        print(f" Color: {self.color}")            
        if self.is_blooming:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

        if self.seeds:
            print(f"Seeds : {self.seeds.number_of_seeds}")
        else:
            print("Seeds : 0")


class Tree(Plant):
    def __init__(self, name, trunk_diameter, age, height):
        super().__init__(name, age, height)
        self.trunk_diameter = trunk_diameter

    def produce_shape(self):
        self.stats.increment_shade()

    def show(self):
        self._show()
        print(f"Trunk diameter: {self.trunk_diameter}")


if __name__ == "__main__":
    print("=== Garden statistic ===")
    print("check year-old")
    rose = Plant("rose", 10, 2)
    rose_2 = Plant("rose", 4000, 2)
    print(f"is {rose.age} more than a year? -> {rose.check_age(rose.age)}")
    print(f"is {rose_2.age} more than a year?->{rose_2.check_age(rose_2.age)}")

    print(" ")

    print("=== Flower ===")
    new_rose = Flower("rose", "red", 10, 15)
    new_rose.show()
    print("[Statistic for Rose]")
    new_rose.stats.show_statistic()
    print("[asking the rose to grow and bloom]")
    new_rose.bloom(3)
    new_rose._grow()
    new_rose.show()
    print("[Statistic for Rose]")
    new_rose.stats.show_statistic()

    print(" ")

    print("=== Tree ===")
    new_tree = Tree("Oak", 5, 365, 200)
    new_tree.show()
    print("[Statistic for Oak]")
    new_tree.stats.show_statistic()
    print("[asking the oak to shade]")
    new_tree.produce_shape()
    new_tree.stats.show_statistic()

    print(" ")

    print("=== Seed  ===")
    sunflower = Flower("Sunflower", "Yellow", 45, 80)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.bloom(42)
    sunflower._age()
    sunflower._grow()
    sunflower.show()
    print("[Statistic for sunflower]")
    sunflower.stats.show_statistic()

    print(" ")

    print("=== Anonymous ===")
    new_anonymous = Anonymous()
    new_anonymous._show()
    print("[Statistic for Anonymous]")
    new_anonymous.stats.show_statistic()
