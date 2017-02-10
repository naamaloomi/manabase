#!/usr/bin/env/python
# coding=utf-8
from __future__ import unicode_literals

from random import randint

from Card import Card
from Hand import Hand


class Deck(object):
    def __init__(self, nr_of_cards, nr_of_lands, nr_of_good_lands):
        self.cards_in_deck = nr_of_cards
        self.lands_in_deck = nr_of_lands
        self.good_lands_in_deck = nr_of_good_lands
        self.cards_in_library = nr_of_cards
        self.lands_in_library = nr_of_lands
        self.good_lands_in_library = nr_of_good_lands
        self.mulligans = 0

    def draw_card(self):
        r = randint(1, self.cards_in_deck)

        if r <= self.good_lands_in_deck:
            self.cards_in_library -= 1
            self.lands_in_library -= 1
            self.good_lands_in_library -= 1
            return Card('Good land')
        elif r <= self.lands_in_deck:
            self.cards_in_library -= 1
            self.lands_in_library -= 1
            return Card('Bad land')
        else:
            self.cards_in_library -= 1
            return Card('Spell')

    def draw_hand(self, x=7):
        h = Hand()
        for i in range(1, x):
            h.add_card(self.draw_card())
        return h

    def mulligan(self):
        self.reset_deck()
        self.mulligans += 1
        return self.draw_hand(7 - self.mulligans)

    def reset_deck(self):
        self.cards_in_library = self.cards_in_deck
        self.lands_in_library = self.lands_in_deck
        self.good_lands_in_library = self.good_lands_in_deck
