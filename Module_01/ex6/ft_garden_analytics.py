# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/09 16:51:56 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/11 11:04:52 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def add_grow(self) -> None:
            self._grow_calls += 1

        def add_age(self) -> None:
            self._age_calls += 1

        def add_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, {self._show_calls} show")

    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = 1.0) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self._growth_rate = growth_rate
        self._stats = Plant._Stats()
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
        self._stats.add_grow()

    def age(self) -> None:
        self._age += 1
        self._stats.add_age()

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        self._stats.add_show()

    def display_stats(self) -> None:
        self._stats.display()

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str, growth_rate: float = 1.0,
                 is_blooming: bool = False) -> None:
        super().__init__(name, height, age, growth_rate)
        self._color = color
        self._is_blooming = is_blooming

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._is_blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str, seeds_on_bloom: int,
                 growth_rate: float = 1.0) -> None:
        super().__init__(name, height, age, color, growth_rate)
        self._seeds = 0
        self._seeds_on_bloom = seeds_on_bloom

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")

    def bloom(self) -> None:
        self._seeds = self._seeds_on_bloom
        super().bloom()


class Tree(Plant):
    class _Stats_tree(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade = 0

        def add_shade(self) -> None:
            self._shade += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float, growth_rate: float = 1.0) -> None:
        super().__init__(name, height, age, growth_rate)
        self._stats: Tree._Stats_tree = Tree._Stats_tree()
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        self._stats.add_shade()
        print(f"Tree {self._name} now produces a shade of {self._height}"
              f"cm long and {self._trunk_diameter}cm wide.")


def display_stats(plant: Plant) -> None:
    plant.display_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    rose_age = Flower("Rose", 15.0, 10, "red", 8.0)
    print("=== Check year-old")
    print(f"Is {rose_age.get_age()} days more than a year? ->"
          f" {rose_age.is_older_than_year(rose_age.get_age())}")
    rose_age.set_age(400)
    print(f"Is {rose_age.get_age()} days more than a year? ->"
          f" {rose_age.is_older_than_year(rose_age.get_age())}")
    print("")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print("")

    print("=== Tree")
    oak = Tree("oak", 200.0, 265, 12)
    oak.show()
    print("[statistics for oak]")
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for oak]")
    display_stats(oak)
    print("")

    print("=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, "yellow", 42)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for sunflower]")
    display_stats(sunflower)
    print("")

    print("=== Anonymous")
    anonymous = Plant.anonymous()
    anonymous.show()
    print("[statistics for Anonymous]")
    display_stats(anonymous)
