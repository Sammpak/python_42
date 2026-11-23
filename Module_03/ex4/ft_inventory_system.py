import sys


class Dict_error(Exception):
    def __init__(self, message: str = "Unknown dict error") -> None:
        self.message = message
        super().__init__(self.message)


def argv_to_dict(argv: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for item in argv:
        item_name = ""
        item_nbr = ""
        is_value = False

        for c in item:
            if c == ":":
                is_value = True
            elif is_value:
                item_nbr += c
            else:
                item_name += c
        try:
            if (item_name not in inventory):
                if item_name == "" or item_nbr == "":
                    raise Dict_error(f" invalid parameter '{item_name}'")
                else:
                    inventory[item_name] = int(item_nbr)
            else:
                raise Dict_error(f"Redundant item '{item_name}' - discarding")
        except Dict_error as e:
            print(f"Error: {e}")
            continue
        except ValueError as e:
            print(f"Error: {e}")
            continue
    return inventory


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    argv: list[str] = sys.argv

    dict_item: dict[str, int] = argv_to_dict(argv[1::])
    if (len(dict_item) != 0):

        print("=== Inventory System Analysis ===")
        print(f"Got inventory : {dict_item}")
        list_item: list[str] = [item for item in dict_item]
        print(f"Item list : {list_item}")

        quantity_total: int = sum(dict_item.values())
        print(f"Total quantity of the {len(list_item)} "
              f"items: {quantity_total}")

        for item, nbr in dict_item.items():
            percent: float = (nbr / quantity_total) * 100
            print(f"Item {item} represents {round(percent, 1)}%")

        current_smaller: int = 0
        current_smaler_item: str = ""
        current_higher: int = 0
        current_higher_item: str = ""
        for item, nbr in dict_item.items():
            if (current_smaler_item == ""):
                current_smaller = nbr
                current_smaler_item = item
                current_higher = nbr
                current_higher_item = item
            if (nbr < current_smaller):
                current_smaller = nbr
                current_smaler_item = item
            if (nbr > current_higher):
                current_higher = nbr
                current_higher_item = item
        print(f"Item most abundant: {current_higher_item} "
              f"with quantity {current_higher}")
        print(f"Item least abundant: {current_smaler_item} "
              f"with quantity {current_smaller}")

        dict_item["magcic_item"] = 1
        print(f"Updated inventory : {dict_item}")
    else:
        print("No item in the inventory")
