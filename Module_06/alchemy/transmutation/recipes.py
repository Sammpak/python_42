from ..elements import create_air                # relatif
from alchemy.potions import strength_potion      # absolu
from elements import create_fire                 # absolu (racine)

def lead_to_gold() -> str:
    return "Recipe transmuting Lead to Gold" + create_air() + " and " +create_fire() + " and " + strength_potion()
