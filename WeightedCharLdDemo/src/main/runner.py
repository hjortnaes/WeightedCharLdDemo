'''
Created on Oct 26, 2016

@author: Nils Hjortnaes
'''

from main.runner import *
from distance import *
from norm_char_lev_dis import *

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
        (2) Print a Tree
        (3) Exit the Program
        """
        user_in = raw_input()
        
        if user_in == 1:
            lang_compare()
        elif user_in == 2:
            build_tree()
            #do the second thing
        elif user_in == 3:
            exit
        else:
            print "That is not a valid option. Please choose a valid option\n"
    
def lang_compare():
    print """
    What algorithm should be used:
    (1) Character Weighted Levenshtein Distance
    (2) Max Normalized Character Weighted Levenshtein Distance
    (3) Min Normalized Character Weighted Levenshtein Distance
    """
    user_in = raw_input()
    #TODO import files here
    #compare read in files
    
def build_tree():
    print """
    Where should the Tree be Printed:
    (1) Console
    (2) HTML File
    (3) Text File
    """
    user_in = raw_input()
    #Build and print the tree
    
    