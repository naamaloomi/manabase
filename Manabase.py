#!/usr/bin/env/python
# coding=utf-8
from __future__ import unicode_literals

from Deck import Deck


def percentage(part, whole):
    return 100 * float(part) / float(whole)


def start_sim(deck, turns_allowed):
    # Draw 7
    h = deck.draw_hand()

    # Decide mulligan
    if h.lands < 2 or h.lands > 5:
        # Mulligan to 6
        h = deck.mulligan()
    if h.lands < 1 or h.lands > 5:
        # Mulligan to 5
        h = deck.mulligan()
    # if h.lands < 1 or h.lands > 4:
        # Mulligan to 4
        # h = deck.mulligan()
    # Draw cards for the number of turns left
    for i in range(1, turns_allowed + 1):
        card = deck.draw_card()
        h.add_card(card)

    return h


def get_good_land_prob(nr_cards=60,
                       nr_lands=18,
                       nr_good_lands=13,
                       nr_iterations=100000,
                       nr_good_lands_needed=1,
                       turns_allowed=0):
    success = 0

    for i in range(0, nr_iterations):
        # Make deck
        d = Deck(nr_cards, nr_lands, nr_good_lands)

        # Start simulation
        h = start_sim(d, turns_allowed)

        # Evaluate result
        if h.good_lands >= nr_good_lands_needed:
            success += 1

    return 'Probability to get {gl} good land in {t} turns = {p}%, ' \
           ''.format(
                gl=nr_good_lands_needed,
                t=turns_allowed,
                p=percentage(success, nr_iterations),
            )


if __name__ == '__main__':
    print(get_good_land_prob())
