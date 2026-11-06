# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_command_quest.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/06 13:18:26 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/06 13:28:24 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys

if __name__ == "__main__":
    print("=== Comand Quest ===")
    list_arg: list = sys.argv
    nbr_arg: int = len(sys.argv)
    print(f"Program name {list_arg[0]}")
    if (nbr_arg == 1):
        print("No argument provided!")
    else:
        print(f"Argument received {nbr_arg}")
        for i in range(1, nbr_arg):
            print(f"Argument {i}: {list_arg[i]}")
