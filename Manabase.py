#!/usr/bin/env/python
# coding=utf-8
from __future__ import unicode_literals

from Deck import Deck


def percentage(part, whole):
    return 100 * float(part) / float(whole)


def sim_game_start(turns_allowed):
    nr_cards = 60
    nr_lands = 18
    nr_good_lands = 16

    # Shuffle deck
    d = Deck(nr_cards, nr_lands, nr_good_lands)

    # Draw 7
    h = d.draw_hand()

    # Decide mulligan
    if h.lands < 2 or h.lands > 5:
        # Mulligan to 6
        h = d.mulligan()
    if h.lands < 2 or h.lands > 4:
        # Mulligan to 5
        h = d.mulligan()
    if h.lands < 1 or h.lands > 4:
        # Mulligan to 4
        h = d.mulligan()
    # Draw cards for the number of turns left
    for i in range(1, turns_allowed + 1):
        card = d.draw_card()
        h.add_card(card)

    return h


def get_good_land_prob():
    nr_iterations = 100000
    nr_good_lands_needed = 2
    turns_allowed = 1
    success = 0

    for i in range(0, nr_iterations):
        h = sim_game_start(turns_allowed)
        if h.good_lands >= nr_good_lands_needed:
            success += 1

    return 'Prob. = {p}%, ' \
           'Success = {s}, ' \
           'Iter. = {i}.'.format(
                p=percentage(success, nr_iterations),
                s=success,
                i=nr_iterations
            )


if __name__ == '__main__':
    print(get_good_land_prob())
