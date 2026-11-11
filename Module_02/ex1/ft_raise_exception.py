# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_raise_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/09 09:59:03 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/11 11:42:55 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def input_temperature(temp_str: str) -> int:
    result: int = int(temp_str)
    if (result > 40):
        print(f"Caught input_temperature error: {nbr_input}°C is too hot "
              "for plants (max 40°C)")
        return False
    if (result < 0):
        print(f"Caught input_temperature error: {nbr_input}°C is too cold "
              "for plants (min 0°C)")
        return False
    return result


def test_temperature(nbr_input: str) -> bool:
    try:
        input_temperature(nbr_input)
    except ValueError as e:
        print(f"Caught input_temperature err: {e}")
        return False
    return True


if __name__ == "__main__":
    print("=== Garden Temperature ===")

    nbr_input: str = "25"
    print(f"Input data is '{nbr_input}'")
    test_temperature(nbr_input)

    nbr_input = "abc"
    print(f"Input data is '{nbr_input}'")
    test_temperature(nbr_input)

    nbr_input = "100"
    print(f"Input data is '{nbr_input}'")
    test_temperature(nbr_input)

    nbr_input = "-50"
    print(f"Input data is '{nbr_input}'")
    test_temperature(nbr_input)

    print("All tests completed - program didn't crash!")
