# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_first_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/09 09:59:03 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/10 15:28:10 by spaccaud        ###   ########.fr        #
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
    return True


if __name__ == "__main__":
    print("=== Garden Temperature ===")

    nbr_input = input("Lets convert a number: ")
    print(f"Input data is '{nbr_input}'")
    if (test_temperature(nbr_input)):
        res = input_temperature(nbr_input)
        print(f"Temperature is now {nbr_input}")
    print("All tests completed - program didn't crash!")
