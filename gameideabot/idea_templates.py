# Copyright (c) 2016 Jonathan Lloyd - copyright@thisisjonathan.com
#
# The MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""Templates for game ideas generated by the gameideabot twitterbot"""

from gameideabot import util
from gameideabot.word_lists import (
    ADJECTIVES,
    GENRES,
    CHARACTERS,
    CHARACTER_ADJECTIVES,
    THINGS,
    PRESENT_VERBS,
    ACTIONS,
    ART_STYLES,
    SETTINGS,
    RESOURCES,
)


NORMAL_IDEA_TEMPLATES = [
    lambda seen_words: 'In this game you must save the world from {} {} ' \
    'by trying to {}.'.format(
        util.a_an(util.pick_word(CHARACTER_ADJECTIVES, seen_words)),
        util.pick_word(CHARACTERS, seen_words),
        util.pick_word(ACTIONS, seen_words),
    ),
    lambda seen_words: '{} game where {} {} {} {}.'.format(
        util.a_an(util.pick_word(GENRES, seen_words)),
        util.a_an(util.pick_word(CHARACTER_ADJECTIVES, seen_words)),
        util.pick_word(CHARACTERS, seen_words),
        util.pick_word(PRESENT_VERBS, seen_words),
        util.a_an(util.pick_word(THINGS, seen_words)),
    ),
    lambda seen_words: '{} {} {} game set in {}.'.format(
        util.a_an(util.pick_word(ADJECTIVES, seen_words)),
        util.pick_word(GENRES, seen_words),
        util.pick_word(GENRES, seen_words),
        util.a_an(util.pick_word(SETTINGS, seen_words)),
    ),
    lambda seen_words: 'A game about {} set in {} ' \
    'where you can only {}.'.format(
        util.a_an(util.pick_word(CHARACTERS, seen_words)),
        util.a_an(util.pick_word(SETTINGS, seen_words)),
        util.pick_word(ACTIONS, seen_words),
    ),
    lambda seen_words: '{} {} game about {} in {} art style.'.format(
        util.a_an(util.pick_word(ADJECTIVES, seen_words)),
        util.pick_word(GENRES, seen_words),
        util.a_an(util.pick_word(SETTINGS, seen_words)),
        util.a_an(util.pick_word(ART_STYLES, seen_words)),
    ),
    lambda seen_words: '{} {} game where you have to {} before {} ' \
    '{} {}.'.format(
        util.a_an(util.pick_word(ADJECTIVES, seen_words)),
        util.pick_word(GENRES, seen_words),
        util.pick_word(ACTIONS, seen_words),
        util.a_an(util.pick_word(CHARACTERS, seen_words)),
        util.pick_word(PRESENT_VERBS, seen_words),
        util.a_an(util.pick_word(THINGS, seen_words)),
    ),
    lambda seen_words: '{} {} game about {}.'.format(
        util.a_an(util.pick_word(ADJECTIVES, seen_words)),
        util.pick_word(ART_STYLES, seen_words),
        util.a_an(util.pick_word(SETTINGS, seen_words)),
    ),
    lambda seen_words: '{} game set in {} {} where you try to {}.'.format(
        util.a_an(util.pick_word(ADJECTIVES, seen_words)),
        util.a_an(util.pick_word(ART_STYLES, seen_words)),
        util.pick_word(SETTINGS, seen_words),
        util.pick_word(ACTIONS, seen_words),
    ),
    lambda seen_words: 'In this {}-styled {} game, {} {} {} {} {}.'.format(
        util.pick_word(ART_STYLES, seen_words),
        util.pick_word(GENRES, seen_words),
        util.a_an(util.pick_word(CHARACTER_ADJECTIVES, seen_words)),
        util.pick_word(CHARACTERS, seen_words),
        util.pick_word(PRESENT_VERBS, seen_words),
        util.a_an(util.pick_word(CHARACTER_ADJECTIVES, seen_words)),
        util.pick_word(CHARACTERS, seen_words),
    ),
    lambda seen_words: '{} {} must collect {} to survive in {} {} game.'.format(
        util.a_an(util.pick_word(CHARACTER_ADJECTIVES, seen_words)),
        util.pick_word(CHARACTERS, seen_words),
        util.pick_word(RESOURCES, seen_words),
        util.a_an(util.pick_word(ART_STYLES, seen_words)),
        util.pick_word(GENRES, seen_words),
    ),
    lambda seen_words: 'In this game, the player must guide {} through {}' \ 
    ' to gather {} for their {}'.format(
        util.a_an(util.pick_word(CHARACTERS, seen_words)),
        util.a_an(util.pick_word(SETTINGS, seen_words)),
        util.pick_word(RESOURCES, seen_words),
        util.pick_word(THINGS, seen_words),
    ),
]

# These idea templates are more "chatty" but get repetitive quickly.
# They should be used less often.
CHATTY_IDEA_TEMPLATES = [
    lambda seen_words: 'What if {} game was set in {}?'.format(
        util.a_an(util.pick_word(GENRES, seen_words)),
        util.a_an(util.pick_word(SETTINGS, seen_words)),
    ),
    lambda seen_words: 'A unique twist on the {} genre. ' \
    'You have to {} while you {} to win the game.'.format(
        util.pick_word(GENRES, seen_words),
        util.pick_word(ACTIONS, seen_words),
        util.pick_word(ACTIONS, seen_words),
    ),
    lambda seen_words: 'This {} game would be interesting - ' \
    'you can only {} once.'.format(
        util.pick_word(GENRES, seen_words),
        util.pick_word(ACTIONS, seen_words),
    ),
    lambda seen_words: 'A {} little indie game set in {} {}. ' \
    'Only if you don\'t {} can you {}.'.format(
        util.pick_word(ADJECTIVES, seen_words),
        util.a_an(util.pick_word(ART_STYLES, seen_words)),
        util.pick_word(SETTINGS, seen_words),
        util.pick_word(ACTIONS, seen_words),
        util.pick_word(ACTIONS, seen_words),
    ),
    lambda seen_words: 'Game mechanic idea - before you can {} ' \
    'you must {}.'.format(
        util.pick_word(ACTIONS, seen_words),
        util.pick_word(ACTIONS, seen_words),
    ),
    lambda seen_words: 'In a world where an evil {} is going to {}, can you ' \
    '{} before it is too late?'.format(
        util.pick_word(CHARACTERS, seen_words),
        util.pick_word(ACTIONS, seen_words),
        util.pick_word(ACTIONS, seen_words),
    ),
    lambda seen_words: 'All {} games are the same these days - ' \
    '{}, {}. What if you {} instead?'.format(
        util.pick_word(GENRES, seen_words),
        util.pick_word(ACTIONS, seen_words),
        util.pick_word(ACTIONS, seen_words),
        util.pick_word(ACTIONS, seen_words),
    ),
    lambda seen_words: 'Why not make {} game where ' \
    '{} must {} in {}?'.format(
        util.a_an(util.pick_word(ADJECTIVES, seen_words)),
        util.a_an(util.pick_word(CHARACTERS, seen_words)),
        util.pick_word(ACTIONS, seen_words),
        util.a_an(util.pick_word(SETTINGS, seen_words)),
    ),
]
