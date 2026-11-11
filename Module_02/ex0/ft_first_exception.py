# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_first_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/09 09:59:03 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/11 11:42:33 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:

    try:
        nbr_input: str = "25"
        print(f"Input data is '{nbr_input}'")
        temp: int = input_temperature(nbr_input)
        print(f"Temperature is now {nbr_input}")

        print("")

        nbr_input = "abc"
        print(f"Input data is '{nbr_input}'")
        temp = input_temperature(nbr_input)
        print(f"Temperature is now {temp}")

    except ValueError as e:
        print(f"Caught input_temperature err: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
    print("All tests completed - program didn't crash!")
