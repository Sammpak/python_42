# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_raise_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/09 09:59:03 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/09 11:24:25 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(nbr_input: str) -> bool:
    try:
        int(nbr_input)
    except ValueError as e:
        print(f"{e}")
        return False
    else:
        if (int(nbr_input) > 40):
            print(f"Caught input_temperature error: {nbr_input}°C is too hot "
                  "for plants (max 40°C)")
            return False
        if (int(nbr_input) < 0):
            print(f"Caught input_temperature error: {nbr_input}°C is too cold "
                  "for plants (min 0°C)")
            return False
    return True


if __name__ == "__main__":
    print("=== Garden Temperature ===")

    for _ in range(0, 5):
        nbr_input = input("Lets convert a number: ")
        print(f"Input data is '{nbr_input}'")
        if (test_temperature(nbr_input)):
            res = input_temperature(nbr_input)
            print(f"Temperature is now {nbr_input}")

    print("All tests completed - program didn't crash!")
