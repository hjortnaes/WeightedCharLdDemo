# -*- coding: UTF-8 -*-
'''
distance.character_map

Map of all characters and positions in the 3D IPA tree used to calculate 
distance between characters.

@author:     Nils Hjortnaes

@contact:    nhjortnaes@gmail.com
'''

from Queue import *

missing_chars = []

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

#i, ɪ, y, ʏ, u, ʊ, e, ɛ, ø, œ, o, ɔ, ɤ, ʌ, ɚ, a, æ, ɐ, ɑ, ɒ, m, b, p, β, f, v, w, n, d, t, θ, ð, s, z, ʃ, ʒ, l, ɾ, ɹ, ŋ, g, k, x, ɣ, j, ʁ, h, ɦ, ʔ
__sub_graph__ = {
    u"i":[u"y", u"e", u"j"],
    u"ɪ":[u"ʏ", u"ɛ", u"j"],
    u"y":[u"i", u"u", u"ʊ", u"ø"],
    u"ʏ":[u"ɪ", u"ʊ", u"œ"],
    u"u":[u"y", u"o", u"w"],
    u"ʊ":[u"y", u"ɔ", u"w"],
    u"e":[u"i", u"ø", u"ɤ", u"a", u"æ"],
    u"ɛ":[u"ɪ", u"œ", u"ʌ", u"ə"],
    u"ø":[u"y", u"e", u"o"],
    u"œ":[u"ʏ", u"ɛ", u"ɔ"],
    u"o":[u"u", u"ø", u"ɤ", u"ʌ", u"ɒ", u"l"],
    u"ɔ":[u"ʊ", u"œ", u"ʌ"],
    u"ɤ":[u"e", u"o", u"ɑ"],
    u"ʌ":[u"ɛ", u"o", u"ɔ", u"ə", u"ɐ", u"ɑ", u"ɒ", u"ɹ", u"ʁ"],
    u"ə":[u"ɛ", u"ʌ", u"ɹ", u"ʁ"],
    #this looks the same as the later a in this font. It is not
    u"a":[u"e", u"ɐ", u"ɑ"],
    u"æ":[u"e", u"ɐ", u"ɑ"],
    u"ɐ":[u"ʌ", u"a", u"æ", u"ɑ", u"ɒ"],
    u"ɑ":[u"ɤ", u"ʌ", u"a", u"æ", u"ɐ", u"ɒ", u"ɹ", u"ʁ"],
    u"ɒ":[u"o", u"ʌ", u"ɑ", u"ɐ", u"ɹ", u"ʁ"],
    u"m":[u"b", u"n", u"ŋ"],
    u"b":[u"m", u"p", u"β", u"v", ],
    u"p":[u"b", u"f", u"ʔ"],
    u"β":[u"b", u"w", u"ɦ"],
    u"f":[u"p", u"v", u"h"],
    u"v":[u"b", u"f", u"w", u"ɦ"],
    u"w":[u"u", u"ʊ", u"β", u"v", u"j", u"ʁ", u"ɦ"],
    u"n":[u"m", u"d", u"l", u"r", u"ɹ", u"ŋ"],
    u"d":[u"n", u"t", u"ð", u"z", u"ʒ", u"l", u"r", u"ɹ"],
    u"t":[u"d", u"θ", u"s", u"ʃ", u"ʔ"],
    u"θ":[u"t", u"ð", u"z", u"ʒ", u"h"],
    u"ð":[u"d", u"θ", u"s", u"ʃ", u"l", u"r", u"ɹ", u"j", u"ʁ", u"ɦ"],
    u"s":[u"t", u"ð", u"z", u"ʒ", u"h"],
    u"z":[u"d", u"θ", u"s", u"ʃ", u"l", u"r", u"ɹ", u"j", u"ɦ"],
    u"ʃ":[u"t", u"ð", u"z", u"ʒ", u"h"],
    u"ʒ":[u"d", u"θ", u"s", u"ʃ", u"l", u"r", u"ɹ", u"j", u"ɦ"],
    u"l":[u"o", u"n", u"d", u"ð", u"z", u"ʒ", u"j", u"ʁ"],
    u"r":[u"n", u"d", u"ð", u"z", u"ʒ", u"j", u"ʁ"],
    u"ɹ":[u"ʌ", u"ə", u"ɑ", u"ɒ", u"n", u"d", u"ð", u"z", u"ʒ", u"j", u"ʁ"],
    u"ŋ":[u"m", u"n", u"ɟ", u"g", u"ʔ"],
    u"ɟ":[u"ŋ", u"q", u"c", u"k", u"ʝ", u"ɣ"],
    u"g":[u"ŋ", u"q", u"c", u"k", u"ʝ", u"ɣ"],
    u"q":[u"ɟ", u"g", u"χ", u"x", u"ʔ"],
    u"c":[u"ɟ", u"g", u"χ", u"x", u"ʔ"],
    u"k":[u"ɟ", u"g", u"χ", u"x", u"ʔ"],
    u"χ":[u"q", u"c", u"k", u"ʝ", u"ɣ", u"h"],
    u"x":[u"q", u"c", u"k", u"ʝ", u"ɣ", u"h"],
    u"ʝ":[u"ɟ", u"g", u"χ", u"x", u"ʁ", u"ɦ"],
    u"ɣ":[u"ɟ", u"g", u"χ", u"x", u"ʁ", u"ɦ"],
    u"j":[u"i", u"ɪ", u"w", u"ð", u"z", u"ʒ", u"l", u"r", u"ɹ", u"ʁ", u"ɦ"],
    u"ʁ":[u"ʌ", u"ə", u"ɑ", u"ɒ", u"w", u"ð", u"l", u"r", u"ɹ", u"ʝ", u"ɣ", u"j", u"ɦ"],
    u"h":[u"f", u"θ", u"s", u"ʃ", u"χ", u"x", u"ɦ", u"ʔ"],
    u"ɦ":[u"β", u"v", u"w", u"ð", u"z", u"ʒ", u"ʝ", u"ɣ", u"j", u"ʁ", u"h"],
    u"ʔ":[u"p", u"t", u"ŋ", u"q", u"c", u"k", u"h"]
    }

def search_sub_graph(a, b):
    '''
    Searches the substitution matrix graph representation to get the edit distance
    between two characters a and b
    
    @return the distance between the characters
    '''
    #Base Case
    if a == b:
        return 0
    
    #deletion
    if a == '-' or b == '-':
        return 4
    
    queue = Queue()
    searched = {a:0}
    curr_char = a
    curr_tuple = (a, 0)
    
    #check for diacritic matched with another diacritic or a gap char
    if (not __sub_graph__.has_key(a) or a == '-') and (not __sub_graph__.has_key(b) or b == '-'):
        return 0
    #Check if the character is not in the graph
    if not __sub_graph__.has_key(a):
        if not a in missing_chars:
            missing_chars.append(a)
            print "Character " + a + " not found in graph"
#         raise ValueError("Character " + a + " not found in graph")
        return 50
    if not __sub_graph__.has_key(b): 
        if not b in missing_chars:
            missing_chars.append(b)
            print "Character " + b + " not found in graph"
#         raise ValueError("Character " + a + " not found in graph")
        return 50
    
    #breadth first search
    while True:
        #Check the first characters and add them to the queue
        for char in __sub_graph__[curr_char]:
            #only add unsearched characters to prevent cycles
            if not searched.has_key(char):
                if char == b:
                    return curr_tuple[1] + 1
                searched[char] = curr_tuple[1] + 1
                queue.put((char, curr_tuple[1] + 1))
        
        if queue.empty():
            #This should never happen
            print "No path found: Check graph for completeness"
            return -1
        
        #get the next character tuple
        curr_tuple = queue.get()
        curr_char = curr_tuple[0]
            
    return searched[b]




