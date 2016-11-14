# -*- coding: UTF-8 -*-
'''
@author: Nils Hjortnaes

Table of distances between ipa tokens allowing our distance measurement
'''

from character_map import char_map

def get_ipa_dist(self, a, b):
    '''
    Calculates the distance between two ipa tokens, a and b, given as characters.
    Calculation is based on character_map.char_map and is the manhattan distance
    in a 3D map.
    
    @return: The 3D manhattan distance as an int
    
    a: ipa token one
    b: ipa token two
    '''
    return (
        abs(char_map[a][0] - char_map[b][0]) + 
        abs(char_map[a][1] - char_map[b][1]) + 
        abs(char_map[a][2] - char_map[b][2])
        )