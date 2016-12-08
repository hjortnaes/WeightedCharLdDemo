# -*- coding: UTF-8 -*-
'''
main.runner

Main function and decision tree

@author: Nils Hjortnaes

@contact: nhjortnaes@gmail.com
'''

import csv
import glob
import sys

from Bio import Seq, pairwise2

from distance import *
from distance.norm_char_lev_dis import *
from main.runner import *
from Bio.FSSP.fssp_rec import align


if __name__ == "__main__":
    
    print """
    Welcome to the Best Lexicostatistics Project ever.
    Please make sure csv files are in resources/csv_files.
    """
    
    #Main Program loop
    while True:
        
        print """
        Choose an option:
        (1) Compare Languages
        (2) Print a Tree (Not yet supported)
        (3) Exit the Program
        """
        user_in = input()
        
        if user_in == 1:
            lang_compare()
        elif user_in == 2:
            build_tree()
            #do the second thing
        elif user_in == 3:
            sys.exit(0)
        else:
            print "That is not a valid option. Please choose a valid option\n"
    
def lang_compare():
    while True:
        print """
        What algorithm should be used:
        (1) Character Weighted Levenshtein Distance
        (2) Max Normalized Character Weighted Levenshtein Distance
        (3) Min Normalized Character Weighted Levenshtein Distance
        """
        user_in = input()
        
        if user_in > 0 and user_in < 4:
            #import files
            word_sets = __read_files__()
            dist_matrix = [[0 for y in range(len(word_sets))] for x in range(len(word_sets))]
            
            #list of languages in order they will be processed - python items() correspond
            languages = word_sets.keys()
            
            for i in range(len(word_sets)):
                for j in range(len(word_sets) - i):
                    j += i
                    lang_total = __compare_word_lists__(languages[i] + "_" + languages[j], word_sets[languages[i]], word_sets[languages[j]])
                    #fill in both halves of matrix
                    dist_matrix[i][j] = lang_total
                    dist_matrix[j][i] = lang_total
                    
            #write the distance matrix to a file
            with open(r"reports/language_distances/dist_matrix.txt", 'w') as f:
                for row in dist_matrix:
                    f.write("[" + ', '.join(str(i) for i in row) + "]\n")
            return
        else: 
            print "That is not a valid option. Please choose a valid option\n"
        
    
def build_tree():
    '''
    Builds a tree and prints it to a specified location. This should use Lingpy becase
    tree building is hard and lingpy can print trees in various ways for us.
    '''
    print """
    Where should the Tree be Printed:
    (1) Console
    (2) HTML File
    (3) Text File
    """
    user_in = raw_input()
    #Build and print the tree
    
def __read_files__():
    '''
    Finds and reads all files in {project-dir}/resources/csv_files and returns a List of all
    sets of words. Assumes that the word list is sorted by language and then word.
    
    @return a dictionary of dictionaries where the outer key is the language and the inner key is 
    the plaintext word. The inner value is the IPA of the word for the outer language
    '''
    word_sets = {}
    
    #defaults based on example header
    index_of_lang = 1
    index_of_word = 5
    index_of_ipa = 9
    
    #TODO make this way more general for future use
    files = glob.glob("resources/csv_files/*.csv")
    for curr_file in files:
        
        with open(curr_file) as csvFile:
            reader = csv.reader(csvFile, delimiter = ',')
            get_header = True
            curr_lang = ""
            curr_words = {}
            
            for row in reader:
                
                #first row of the file defines locations of data
                if get_header:
                    get_header = False
                    index_of_lang = row.index("LanguageName")
                    index_of_word = row.index("WordModernName1")
                    index_of_ipa = row.index("Phonetic")
                    
                else:
                    #starting a new language
                    if row[index_of_lang] != curr_lang:
                        
                        #only add non-empty lists
                        if len(curr_words) > 0:
                            #map dictionary of IPA words to the language
                            word_sets[curr_lang] = curr_words
                        
                        #start recording for next language
                        curr_lang = row[index_of_lang]
                        
                    #map IPA to plain text word
                    curr_words[row[index_of_word]] = row[index_of_ipa]
                    
    return word_sets

#TODO make this general, is very breakable right now
def __compare_word_lists__(pair, dict_one, dict_two):
    '''
    Assumes both dictionaries are the same length. Calculates the total distance between the two
    lists and prints the individual word distances to a file in 
    {project_root}/reports/word_comparisons
    
    @return the total distance between the languages
    '''
    total = 0
    words = dict_one.keys()
    #file for writing results
    print pair
    with open(r"reports/word_comparisons/" + pair + ".txt", 'w') as f:
        #get all words in the lists
        for key in words:
            
            #convert to Sequences for alignment
#             seq_one = Seq(dict_one[key])
#             seq_two = Seq(dict_two[key])
            alignment = pairwise2.align.globalxx(dict_one[key], dict_two[key])
            print alignment
            f.write(alignment[0][0] + "\n" + alignment[0][1])
            
            #compare read in files
#             dist = norm_char_lev_dis.get_word_distance(alignment, user_in)
#             f.write("{}: {}").format(key, dist)
#             total += dist
    return total
    
    
    
    
    
    