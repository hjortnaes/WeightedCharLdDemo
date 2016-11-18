# -*- coding: UTF-8 -*-
'''
main.runner

Main function and decision tree

@author: Nils Hjortnaes

@contact: nhjortnaes@gmail.com
'''

import csv
import glob

from distance import *
from distance.norm_char_lev_dis import *
from main.runner import *


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
            exit
        else:
            print "That is not a valid option. Please choose a valid option\n"
    
def lang_compare(self):
    print """
    What algorithm should be used:
    (1) Character Weighted Levenshtein Distance
    (2) Max Normalized Character Weighted Levenshtein Distance
    (3) Min Normalized Character Weighted Levenshtein Distance
    """
    user_in = input()
    
    #import files
    
    
    #compare read in files
    norm_char_lev_dis.get_word_distance(alignment, user_in)
        
    
def build_tree(self):
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
    
def read_files(self):
    '''
    Finds and reads all files in {project-dir}/resources/csv_files and returns a List of all
    sets of words. 
    '''
    words = []
    
    files = glob.glob("resources/csv_files/*.csv")
    for curr_file in files:
        with open(curr_file) as csvFile:
            reader = csv.reader(csvFile, delimiter = ',')
            get_header = True
            for row in reader:
                if get_header:
                    get_header = False
                    header = row
                print row
            print header
        
    return 
    
    
    
    
    
    
    
    