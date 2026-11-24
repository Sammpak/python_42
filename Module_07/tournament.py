from ex2 import (
    CreatureFactory, FlameFactory,
    HealingCreatureFactory, TransformCreatureFactory,
    BattleStrategy, NormalStrategy, AggressiveStrategy, DefensiveStrategy,
    InvalidStrategyError, AquaFactory
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                factory_a, strat_a = opponents[i]
                factory_b, strat_b = opponents[j]
                a = factory_a.create_base()
                b = factory_b.create_base()
                print("\n* Battle *")
                print(a.describe())
                print(" vs.")
                print(b.describe())
                print(" now fight!")
                action_a: list[str] = strat_a.act(a)
                for a in action_a:
                    print(f"{a}")
                action_b: list[str] = strat_b.act(b)
                for b in action_b:
                    print(f"{b}")
    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")
        pass


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    # [ (Flameling+Normal), (Healing+Defensive) ]
    print("Tournament 0 (basic)")
    battle([(flame, normal), (healing, defensive)])

    print(" ")
    print("Tournament 1 (error)")
    # [ (Flameling+Aggressive), (Healing+Defensive) ]
    battle([(flame, aggressive), (healing, defensive)])

    print(" ")
    print("Tournament 2 (multiple)")
    # [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]
    battle([(aqua, normal), (healing, defensive), (transform, aggressive)])
