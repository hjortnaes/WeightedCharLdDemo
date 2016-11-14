# -*- coding: UTF-8 -*-
'''
distance.character_map

Map of all characters and positions in the 3D IPA tree used to calculate 
distance between characters.

@author:     Nils Hjortnaes

@contact:    nhjortnaes@gmail.com
'''
# map from character to 3D pos (x, y, z)
char_map = {
    "p": (0, 1, 0),
    "t": (3, 1, 0),
    "k": (6, 1, 0),
    "tʃ": (4, 2, 0),
    "f": (1, 3, 0),
    "θ": (2, 3, 0),
    "s": (3, 3, 0),
    "ʃ": (4, 3, 0),
    "x": (6, 3, 0),
    "m": (0, 0, 1),
    "n": (3, 0, 1),
    "ŋ": (6, 0, 1),
    "b": (0, 1, 1),
    "d": (3, 1, 1),
    "g": (6, 1, 1),
    "dʒ": (4, 2, 1),
    "v": (1, 3, 1),
    "ð": (2, 3, 1),
    "z": (3, 3, 1),
    "ʒ": (4, 3, 1),
    "ɣ": (6, 3, 1),
    "(w)": (0, 4, 1),
    "j": (5, 4, 1),
    "w": (6, 4, 1),
    "l": (3, 5, 1),
    "r": (3, 6, 1),
    "R": (7, 6, 1),
    "i": (0, 4, 2),
    "(j)": (5, 4, 2),
    "u": (6, 4, 2),
    "e": (0, 5, 2),
    "o": (6, 5, 2),
    "æ": (0, 6, 2),
    "a": (6, 6, 2)
    }


