# -*- coding: UTF-8 -*-
'''
@author: Nils Hjortnaes

Functions for calculating the distance of words
'''

from ipa_distance import *

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
    #make sure the 2D array is the format I think it is
    print alignment
    for i in alignment.length:
        distance += get_ipa_dist(i[0], i[1])
    return distance / norm_dist





