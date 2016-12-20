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
import codecs

from Bio import Seq, pairwise2, Phylo
from Bio.Phylo.TreeConstruction import _DistanceMatrix, DistanceTreeConstructor

from distance import *
from distance.norm_char_lev_dis import *
from distance.character_map import missing_chars
from main.runner import *
from Bio.FSSP.fssp_rec import align
from algorithm.clustering import neighbor


if __name__ == "__main__":
    
    lang_dist = None
    
    print """
    Welcome to the Best Lexicostatistics Project ever.
    Please make sure csv files are in resources/csv_files.
    """
    
    #Main Program loop
    while True:
        
        print """
        Choose an option:
        (1) Compare Languages
        (2) Print a Tree
        (3) Exit the Program
        """
        user_in = input()
        
        if user_in == 1:
            lang_dist = lang_compare()
        elif user_in == 2:
            if not lang_dist is None:
                build_tree(lang_dist[0], lang_dist[1])
            else:
                print "Run a comparison to generate the distance matrix first\n"
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
            word_sets = __read_files()
            lang_dist = [[0 for y in range(len(word_sets))] for x in range(len(word_sets))]
            
            #list of languages in order they will be processed - python items() correspond
            languages = word_sets.keys()
            
            #process each pair of languages
            for i in range(len(word_sets)):
                #process all languages after i (no repeat pairs)
                for j in range(len(word_sets) - i):
                    j += i
                    lang_total = __compare_word_lists(user_in, languages[i] + "_" + languages[j], word_sets[languages[i]], word_sets[languages[j]])
                    #fill in both halves of matrix
                    lang_dist[i][j] = lang_total
                    lang_dist[j][i] = lang_total
                    
            #write the distance matrix to a file
            with codecs.open(r"reports/language_distances/dist_matrix.txt", 'w', encoding='utf-8') as f:
                i = 0
                f.write(str(languages) + "\n")
                for row in lang_dist:
                    f.write(languages[i] + "[" + ", ".join(str(i) for i in row) + "]\n")
                    i += 1
                    
            #write missing_chars to its file
            with codecs.open("reports/missing_chars.txt", 'a', encoding = "utf-8") as missing_file:
                for thing in missing_chars:
                    missing_file.write(thing + "\n")
            return (languages, lang_dist)
        else: 
            print "That is not a valid option. Please choose a valid option\n"
        
    
def build_tree(languages, lang_dist):
    '''
    Builds a tree and prints it to a specified location. 
    '''
    print """
    Where should the Tree be Printed:
    (1) Console
    (2) Text File
    (3) Both
    """
    user_in = input()
    
    #Build and print the tree
    if user_in > 0 and user_in < 4:
        #decode the strings in languages
        for i in range(len(languages)):
            languages[i] = codecs.encode(languages[i], 'utf-8')
            
        #get the lower triangle matrix format
        for i in range(len(lang_dist)):
            lang_dist[i] = lang_dist[i][:i + 1]
            
        dist_matrix = _DistanceMatrix(languages, lang_dist)
        
        tree_constructor = DistanceTreeConstructor()
        upgma_tree = tree_constructor.upgma(dist_matrix)
        neighbor_tree = tree_constructor.nj(dist_matrix)
        
        if not upgma_tree is None and not neighbor_tree is None:
            #Draw to the console
            if user_in == 1:
                print "upgma tree:\n" 
                Phylo.draw_ascii(upgma_tree)
                Phylo.draw(upgma_tree)
                print "\nneighbor joining tree:\n"
                Phylo.draw_ascii(neighbor_tree)
                
            #draw to the files only
            elif user_in == 2:
                with open(r"reports/language_distances/upgma_tree.txt", 'w') as f:
#                     f.write(str(upgma_tree))
                    Phylo.draw_ascii(upgma_tree, f)
                with open(r"reports/language_distances/neighbor_tree.txt", 'w') as f:
#                     f.write(str(neighbor_tree))
                    Phylo.draw_ascii(neighbor_tree, f)
                    
            #draw to the files and the console
            elif user_in == 3:
                print "upgma tree:\n"
                Phylo.draw_ascii(upgma_tree)
                print "\nneighbor joining tree:\n"
                Phylo.draw_ascii(neighbor_tree)
                
                with open(r"reports/language_distances/upgma_tree.txt", 'w') as f:
#                     f.write(str(upgma_tree))
                    Phylo.draw_ascii(upgma_tree, f)
                with open(r"reports/language_distances/neighbor_tree.txt", 'w') as f:
#                     f.write(str(neighbor_tree))
                    Phylo.draw_ascii(neighbor_tree, f)
        
        else:
            print "Run a comparison to generate the distance matrix first\n"
            
    else:
        print "That is not a valid option. Please choose a valid option\n"
    
def __read_files():
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
        
        with codecs.open(curr_file) as csvFile:
            reader = csv.reader(csvFile, delimiter = ',')
            get_header = True
            curr_lang = ""
            curr_words = {}
            
            #process each row of the csv file. Header defines content
            for row in reader:
                
                #decode into unicode
                for i in range(len(row)):
                    row[i] = codecs.decode(row[i], "utf-8")
                
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
                            #reset curr_words
                            curr_words = {}
                        
                        #start recording for next language
                        curr_lang = row[index_of_lang]
                        
                    #map IPA to plain text word
                    curr_words[row[index_of_word]] = row[index_of_ipa]
                    
            #map last dictionary in file of IPA words to the language
            word_sets[curr_lang] = curr_words
            #reset curr_words
            curr_words = {}
    return word_sets

#TODO make this general, is very breakable right now
def __compare_word_lists(user_in, pair, dict_one, dict_two):
    '''
    Assumes both dictionaries are the same length. Calculates the total distance between the two
    lists and prints the individual word distances to a file in 
    {project_root}/reports/word_comparisons
    
    @return the total distance between the languages
    '''
    total = 0
    normalize_by = 1
    words = dict_one.keys()
    #file for writing results
    print pair
    with codecs.open(r"reports/word_comparisons/" + pair + ".txt", 'w', encoding='utf-8') as f:
        #get all words in the lists
        for key in words:
            
            print key
            f.write(str(key) + "\n")
            
            distances = []
            shortest = sys.maxint
            
            if user_in == 2:
                normalize_by = max(len(dict_one[key]), len(dict_two[key]))
            elif user_in == 3:
                normalize_by = min(len(dict_one[key]), len(dict_two[key]))
            
            #get the alignments of the words
            alignments = pairwise2.align.globalxx(list(dict_one[key]), list(dict_two[key]), gap_char = ['-'])
#             print alignments
            
            for align in alignments:
                #only take the shortest alignments
#                 if len(align[0]) < shortest:
#                     distances = []
#                     shortest = len(align[0])
#                 elif len(align[0]) > shortest:
#                     continue
                    
#                 f.write('\t'.join(align[0]) + "\n" + '\t'.join(align[1]) + "\n")
            
                #for testing
                zipped_alignment = zip(list(align[0]), list(align[1]))
                
                #compare read in files
                dist = norm_char_lev_dis.get_word_distance(zipped_alignment, normalize_by)
                distances.append(dist)
                
                f.write(u"alignment:\n{}\n{} distance:{}\n\n".format('\t'.join(align[0]), '\t'.join(align[1]), dist))
            total += min(distances)
    return total
    
    
    
    
    
    