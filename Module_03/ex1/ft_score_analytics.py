# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/06 13:48:02 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/06 15:43:35 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys

if __name__ == "__main__":
    print("=== PLayer score Analytics")
    argv: list = sys.argv
    argc: int = len(sys.argv)
    is_correct: bool
    valide_list = [None] * argc
    i_list = 0
    if (argc == 1):
        print("No score provided. Usage:")
        
    else:
        for i in range(1, argc):
            is_correct = True
            for j in range(0, len(argv[i])):
                if argv[i][j] not in "0123456789":
                    print(f"Invalide parameter {argv[i]}")
                    is_correct = False
                    break
            if (is_correct):
                valide_list[i_list] = argv[i]
                i_list = i_list + 1

        size_real_list = 0
        for k in range(0, len(valide_list)):
            if (valide_list[k] is not None):
                size_real_list += 1
        real_list_fr = [None] * size_real_list

        for n in range(0, size_real_list):
            real_list_fr[n] = atoi(valide_list[n])

        if (size_real_list == 0):
            print("No score provided")
        else:
            total_score = 0
            for p in range(0, size_real_list):
                total_score += real_list_fr[p]
            average_score = total_score / size_real_list
            print(f"Average score: {average_score}")
            print(f"Total score {total_score}")
            print(f"Scores processed: {real_list_fr}")
            print(f"Total player: {size_real_list}")
            print(f"Low score: {min(real_list_fr)}")
            print(f"High score: {max(real_list_fr)}")
            score_range = max(real_list_fr) - min(real_list_fr)
            print(f"Score range: {score_range}")
