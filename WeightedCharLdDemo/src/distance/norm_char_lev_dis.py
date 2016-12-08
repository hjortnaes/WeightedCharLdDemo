# -*- coding: UTF-8 -*-
'''
@author: Nils Hjortnaes

Functions for calculating the distance of words
'''

from character_map import *
from distance.norm_char_lev_dis import *

class NormCharLevDis(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
def get_word_distance(self, alignment, norm_dist = 1):
    '''
    Gets the distance between two aligned strings
    
    @param alignment: A 2D array of aligned Strings
    @param norm_dist: the distance to normalize the word length by
    
    @return: The distance between aligned words
    '''
    distance = 0

    print alignment
    for i in alignment.length:
        distance += search_sub_graph(i[0], i[1])
    return distance / norm_dist

# def get_ipa_dist(self, a, b):
#     '''
#     Calculates the distance between two ipa tokens, a and b, given as characters.
#     Calculation is based on character_map.char_map and is the manhattan distance
#     in a 3D map.
#     
#     @return: The 3D manhattan distance as an int
#     
#     a: ipa token one
#     b: ipa token two
#     '''
#     return (
#         abs(char_map[a][0] - char_map[b][0]) + 
#         abs(char_map[a][1] - char_map[b][1]) + 
#         abs(char_map[a][2] - char_map[b][2])
#         )




