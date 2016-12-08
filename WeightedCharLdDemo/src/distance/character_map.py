# -*- coding: UTF-8 -*-
'''
distance.character_map

Map of all characters and positions in the 3D IPA tree used to calculate 
distance between characters.

@author:     Nils Hjortnaes

@contact:    nhjortnaes@gmail.com
'''

from Queue import *

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

# i, y, u, e, ø, o, ʌ, æ, ɑ, ɒ, m, b, p, β, f, v, w, n, d, t, θ, ð, s, z, ʃ, ʒ, l, ɾ, ɹ, ŋ, g, k, x, ɣ, j, ʁ, h, ɦ, ʔ
__sub_graph__ = {
    "i":["y", "e", "j"],
    "y":["i", "u", "ø", ],
    "u":["y", "o", "ʌ", "w"],
    "e":["i", "ø", "æ"],
    "ø":["y", "e", "o"],
    "o":["u", "ø", "ʌ", "ɒ", "l"],
    "ʌ":["u", "o", "ɑ", "ɒ", "ɹ", "ʁ"],
    "æ":["e", "ɑ"],
    "ɑ":["ʌ", "æ", "ɒ", "ɹ", "ʁ"],
    "ɒ":["o", "ʌ", "ɑ", "ɹ", "ʁ"],
    "m":["b", "n", "ŋ"],
    "b":["m", "p", "β", "v", ],
    "p":["b", "f", "ʔ"],
    "β":["b", "w", "ɦ"],
    "f":["p", "v", "h"],
    "v":["b", "f", "w", "ɦ"],
    "w":["u", "β", "v", "j", "ʁ", "ɦ"],
    "n":["m", "d", "l", "ɾ", "ɹ", "ŋ"],
    "d":["n", "t", "ð", "z", "ʒ", "l", "ɾ", "ɹ"],
    "t":["d", "θ", "s", "ʃ", "ʔ"],
    "θ":["t", "ð", "z", "ʒ", "h"],
    "ð":["d", "θ", "s", "ʃ", "l", "ɾ", "ɹ", "j", "ʁ", "ɦ"],
    "s":["t", "ð", "z", "ʒ", "h"],
    "z":["d", "θ", "s", "ʃ", "l", "ɾ", "ɹ", "j", "ɦ"],
    "ʃ":["t", "ð", "z", "ʒ", "h"],
    "ʒ":["d", "θ", "s", "ʃ", "l", "ɾ", "ɹ", "j", "ɦ"],
    "l":["o", "n", "d", "ð", "z", "ʒ", "j", "ʁ"],
    "ɾ":["n", "d", "ð", "z", "ʒ", "j", "ʁ"],
    "ɹ":["ʌ", "ɑ", "ɒ", "n", "d", "ð", "z", "ʒ", "j", "ʁ"],
    "ŋ":["m", "n", "g", "ʔ"],
    "g":["ŋ", "k", "ɣ"],
    "k":["g", "x", "ʔ"],
    "x":["k", "ɣ", "h"],
    "ɣ":["g", "x", "ʁ", "ɦ"],
    "j":["i", "w", "ð", "z", "ʒ", "l", "ɾ", "ɹ", "ʁ", "ɦ"],
    "ʁ":["ʌ", "ɑ", "ɒ", "w", "ð", "l", "ɾ", "ɹ", "ɣ", "j", "ɦ"],
    "h":["f", "θ", "s", "ʃ", "x", "ɦ", "ʔ"],
    "ɦ":["β", "v", "w", "ð", "z", "ʒ", "ɣ", "j", "ʁ", "h"],
    "ʔ":["p", "t", "ŋ", "k", "h"]
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
    
    queue = Queue.Queue()
    searched = {a:0}
    curr_char = a
    curr_tuple = (a, 0)
    
    with open("reports/missing_chars.txt", 'a') as missing_file:
        
        while True:
            #Check if the character is not in the graph
            if not __sub_graph__.has_key(curr_char):
                missing_file.write(curr_char + "\n")
                print "Character " + curr_char + " not found in graph"
                return -1
            
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
                break
            
            #get the next character tuple
            curr_tuple = queue.get()
            curr_char = curr_tuple[0]
            
            
        return searched[b]




