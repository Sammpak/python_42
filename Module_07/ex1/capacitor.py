from creature import *

if __name__ == "__main__":
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()
    sproutling = factory.create_base()
    sproutling.describe()
    sproutling.attack()
    sproutling.heal()
    bloomelle = factory.create_evolved()
    print(" evolved")
    bloomelle.describe()
    bloomelle.attack()
    bloomelle.heal()

    print(" ")

    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()
    shiftling = factory.create_base()
    shiftling.describe()
    shiftling.attack()

    

