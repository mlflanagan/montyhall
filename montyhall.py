#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
montyhall.py
mlf March 2020
Reference: https://github.com/DeegC/monty_hall_paradox
"""

from random import randrange


def play():
    """
    Run a single simulation of the Monty Hall problem.
    Returns:
        'switch' if the contestant should switch doors to win.
        'stay'   if the contestant should NOT switch doors.
    """

    # Randomly choose a winning door.
    winning_door = randrange(3)

    # Contestant randomly chooses a door.
    contestant_choice = randrange(3)

    # Determine if the contestant should switch or stay.
    return "stay" if contestant_choice == winning_door else "switch"


if __name__ == '__main__':
    results = {"stay": 0, "switch": 0}
    for i in range(1000):
        stay_or_switch = play()
        results[stay_or_switch] += 1
    print("stay: {}, switch: {}".format(results["stay"], results["switch"]))
