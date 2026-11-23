import random
from typing import Generator


def get_all_player() -> set[str]:
    return {
        'Samuel', 'Aatrox', 'Zeri',
        'Annie', 'Garen', 'VI',
        'Leblanc', 'Yuumi', 'Skarner'
    }


def get_all_action() -> set[str]:
    return {
        'Move', 'Gank', 'Dive',
        'Farm', 'Die', 'Kill'
    }


def get_random_action() -> str:
    actions = list(get_all_action())
    return random.choice(actions)


def get_random_player() -> str:
    players = list(get_all_player())
    return random.choice(players)


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        yield (get_random_player(), get_random_action())


def consume_event(
    list_event: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while len(list_event) > 0:
        index: int = random.randrange(len(list_event))
        event: tuple[str, str] = list_event[index]
        del list_event[index]
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    stream = gen_event()

    for i in range(1000):
        player, action = next(stream)
        print(f"Event {i}: Player {player} did action {action}")

    events: list[tuple[str, str]] = []
    for _ in range(10):
        events += [next(stream)]
    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")
