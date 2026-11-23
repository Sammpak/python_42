import random


def get_all_name() -> set[str]:
    return {
        'samuel', 'aatrox', 'Zeri',
        'Annie', 'garen', 'VI',
        'Leblanc', 'yuumi', 'Skarner'
    }


def get_random_name() -> str:
    players = list(get_all_name())
    return random.choice(players)


def get_list_name(nbr: int) -> list[str]:
    return [get_random_name() for i in range(nbr)]


def capitalize_list(name_list: list[str]) -> list[str]:
    return [name.capitalize() for name in name_list]


def capitalize_list_only(name_list: list[str]) -> list[str]:
    return [name for name in name_list if name[0].isupper()]


def gen_dict(name_list: list[str]) -> dict[str, int]:
    return {name: random.randint(0, 1000) for name in name_list}


def get_high_score(dict_name: dict[str, int], average: float
                   ) -> dict[str, int]:
    return {name: value for name, value in dict_name.items()
            if value > average}


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    name_list: list[str] = get_list_name(10)
    print(f"Initial list of players: {name_list}")

    name_list_capitalized: list[str] = capitalize_list(name_list)
    print(f"New list with all names capitalize {name_list_capitalized}")

    name_list_capitalized_only: list[str] = capitalize_list_only(name_list)
    print(f"New list with all names capitalize {name_list_capitalized_only}")

    dict_name: dict[str, int] = gen_dict(name_list_capitalized_only)
    print(f"Score dict {dict_name}")

    total: int = sum([value for value in dict_name.values()])
    average: float = total / len(dict_name)
    print(f"Average score: {round(average, 1)}")

    dict_high_score: dict[str, int] = get_high_score(dict_name, average)
    print(f"high scores: {dict_high_score}")
