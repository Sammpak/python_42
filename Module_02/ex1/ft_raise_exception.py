# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_raise_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/09 09:59:03 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/11 12:51:46 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def input_temperature(temp_str: str) -> int:
    result: int = int(temp_str)
    if (result > 40):
        raise ValueError(f"{result}°C is too hot for plants (max 40°C)")
    if (result < 0):
        raise ValueError(f"{result}°C is too cold for plants (min 0°C)")
    return result


def test_temperature() -> None:
    list_input: list[str] = ["25", "abc", "100", "-50"]

    for nbr in list_input:
        try:
            print(f"Input data is '{nbr}")
            result: int = input_temperature(nbr)    
            print(f"Temperature is now {result}°C")
        except ValueError as e:
            print(f"Caught input_temperature err: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
    print("All tests completed - program didn't crash!")
