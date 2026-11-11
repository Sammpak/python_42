# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: spaccaud <spaccaud@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/06 13:48:02 by spaccaud        #+#    #+#               #
#  Updated: 2026/11/11 13:24:35 by spaccaud        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


class Score_error(Exception):
    def __init__(self, message: str = "Unknown score error") -> None:
        self.message = message
        super().__init__(self.message)


def get_valid_scores(args: list[str]) -> list[int]:
    scores: list[int] = [0] * len(args)
    i: int = 0
    for arg in args:
        try:
            scores[i] = int(arg)
            i += 1
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return scores[:i]


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scores: list[int] = get_valid_scores(sys.argv[1:])
    if len(scores) == 0:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        total: int = sum(scores)
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {total}")
        print(f"Average score: {total / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")