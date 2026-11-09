# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_different_errors.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/09 10:34:42 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/09 11:49:18 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def garden_operations(operation_number: int) -> None:
    if (operation_number == 0):
        int("abc")
    elif (operation_number == 1):
        123 % 0
    elif (operation_number == 2):
        open("opening_this_beautifull_noexistant_file.txt", "r")
    elif (operation_number == 3):
        "123" + 123
    elif (operation_number == 4):
        print("All error types tested successfully!")


def test_error_types(operation_number: int) -> None:
    try:
        garden_operations(operation_number)
    except ValueError as e:
        print(f"{e}")
    except ZeroDivisionError as e:
        print(f"{e}")
    except FileNotFoundError as e:
        print(f"{e}")
    except TypeError as e:
        print(f"{e}")


if __name__ == "__main__":

    print("=== Garden Error Types Demo ===")
    for i in range(0, 5):
        print(f"Testing operation: {i}...")
        test_error_types(i)
