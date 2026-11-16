import random


def get_all_achievements() -> set[str]:
    return {
        'Crafting Genius', 'Strategist', 'World Savior',
        'Speed Runner', 'Survivor', 'Master Explorer',
        'Treasure Hunter', 'Unstoppable', 'First Steps',
        'Collector Supreme', 'Untouchable', 'Sharp Mind',
        'Boss Slayer',
    }


def gen_player_achievements() -> set[str]:
    achievements: set[str] = get_all_achievements()
    count = random.randint(2, len(achievements))
    return set(random.sample(list(achievements), count))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print("")

    p_alice: set[str] = gen_player_achievements()
    print(f'Player Alice {p_alice}')

    p_bob: set[str] = gen_player_achievements()
    print(f'Player Bob {p_bob}')

    p_charlie: set[str] = gen_player_achievements()
    print(f'Player Charlie {p_charlie}')

    p_dylan: set[str] = gen_player_achievements()
    print(f'Player Dylan {p_dylan}')

    all_achivement: set[str] = get_all_achievements()
    print(f"All distinct achievements: {all_achivement}")

    commun_achivement: set[str] = set.intersection(
        p_alice, p_bob, p_charlie, p_dylan
    )
    print(f"Common achievements: '{commun_achivement}'")

    alice_unique: set[str] = set.difference(p_alice, p_bob, p_charlie, p_dylan)
    print(f"Alice has: '{alice_unique}'")

    bob_unique: set[str] = set.difference(p_bob, p_alice, p_charlie, p_dylan)
    print(f"Bob has: '{bob_unique}'")

    charlie_unic: set[str] = set.difference(p_charlie, p_alice, p_bob, p_dylan)
    print(f"Charlie has: '{charlie_unic}'")

    dylan_unique: set[str] = set.difference(p_dylan, p_alice, p_bob, p_charlie)
    print(f"Dylan has: '{dylan_unique}'")

    alice_missing: set[str] = set.difference(all_achivement, p_alice)
    print(f"Alice missing: '{alice_missing}'")

    bob_missing: set[str] = set.difference(all_achivement, p_bob)
    print(f"Bob missing: '{bob_missing}'")

    charlie_missing: set[str] = set.difference(all_achivement, p_charlie)
    print(f"Charlie missing: '{charlie_missing}'")

    dylan_missing: set[str] = set.difference(all_achivement, p_dylan)
    print(f"Dylan missing: '{dylan_missing}'")
