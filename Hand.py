#!/usr/bin/env/python
# coding=utf-8
from __future__ import unicode_literals

class Hand(object):
    def __init__(self):
        self.cards = 0
        self.spells = 0
        self.bad_lands = 0
        self.good_lands = 0

    def __str__(self):
        return 'Cards = {c}, ' \
               'Spells = {s}, ' \
               'Good lands = {gl}, ' \
               'Bad lands = {bl}'.format(
                    c=self.cards,
                    s=self.spells,
                    gl=self.good_lands,
                    bl=self.bad_lands
                )

    def _add_spell(self):
        self.spells += 1

    def _add_bad_land(self):
        self.bad_lands += 1

    def _add_good_land(self):
        self.good_lands += 1

    def add_card(self, card):
        if card.type == 'Good land':
            self._add_good_land()
        elif card.type == 'Bad land':
            self._add_bad_land()
        elif card.type == 'Spell':
            self._add_spell()
        self.cards += 1

    @property
    def lands(self):
        return self.good_lands + self.bad_lands
