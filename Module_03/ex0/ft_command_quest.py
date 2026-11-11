# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_command_quest.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/06 13:18:26 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/11 13:08:40 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys

if __name__ == "__main__":
    args: list[str] = sys.argv
    total: int = len(args)
    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")
    if total == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {total - 1}")
        i: int = 1
        for arg in args:
            print(f"Argument {i}: {arg}")
            i += 1
    print(f"Total arguments: {total}")
