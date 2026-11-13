# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_achievement_tracker.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spaccaud <spaccaud@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/11/13 13:14:54 by spaccaud          #+#    #+#              #
#    Updated: 2026/11/13 15:42:12 by spaccaud         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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

    commun_achivement: set[str] = set.union(p_alice, p_bob, p_alice, p_dylan)
    print(f"Common achievements: '{commun_achivement}'")