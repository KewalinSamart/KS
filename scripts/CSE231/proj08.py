###############################################################################
#    Programming Project #8
#
#    Algorithm
#        display header
#        prompt for a string (y/n) to start or end the program
#        call function to open file
#            prompt for strings (a file name)
#            loop while the input is incorrect
#                reprompt for strings (a file name)
#        prompt for strings (the rack 2-7 chars)
#        loop while the input is incorrect
#            reprompt for strings (the rack)
#        prompt for strings (tiles on board)
#        loop while the input is incorrect
#            reprompt for strings (tiles on board)
#        display outputs 
#        exit the program if the input for (y/n) is 'n' 
############################################################################### 

import itertools     #import itertools for making combination of characters
from operator import itemgetter  #import itemgetter for sorting.

#dictionary representing score for each character (constant)
SCORE_DICT = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,'J':8,'K':5,'L':1,'M':3,
              'N':1,'O':1,'P':3,'Q':10,'R':1,'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}

def open_file():
    '''
    Open a file (.txt). 
    No parameters
    Returns: the opened file for reading only (fp).
    '''
    #while loop to reprompt for input if it's incorrect
    while True:
        file_name = input("Input word file: ") #prompt for a file name
        
        try:                           #open the file if successful
            fp = open(file_name, "r") 
            break
        except FileNotFoundError:      #display error message if not successful
            print("File not found. Try again.") 
            
    return fp
            

def read_file(fp):
    '''
    Read through each line in the file 'fp' and collect wanted data which are words in each line 
    and put them in a dictionary with all keys has the same value, 1.
    fp: returning value of the open_file() fuction.
    Returns: a dictionary of english words with all values 1.
    
    '''
    scrabble_words_dict = {}
    word_list = []
    for line in fp:
        line = line.split()
        count_ch = 0
        for word in line:
            for ch in word:
                if ch.isalpha():
                    count_ch += 1
                else:
                    count_ch = 0
               
            if count_ch >= 3:
                if "-" not in word: 
                    if "'" not in word:
                        word_list.append(word)
                
    for word in word_list:        
        scrabble_words_dict[word] = 1
    
    return scrabble_words_dict
            
            

def calculate_score(rack,word):
    """
    This function calsulate score for each word and add bonus point to the words that
    use all characters in the rack with length of the rack equals to 7.
    rack: string input containing 2-7 characters in total (strings)
    word: the word that is built by the characters in the rack (strings)
    Returns: score for a particular word
    """
    score = 0
    length_rack = len(rack)    
    
    for ch in word: 
        score += SCORE_DICT[ch.upper()]
            
    for ch in word:
        if ch in rack:
            rack = rack.replace(ch,'',1)
    if length_rack == 7 and rack == "":
        score += 50
    
   
    return score

def generate_combinations(rack,placed_tile):
    """
    This function generates set of word combinations between rack and placed_tile in tuples of characters.
    rack: string input containing 2-7 characters in total (strings)
    placed_tile: the tiles that are placed on the board (strings)
    Returns: set_combination, a set containing tuples of mix characters.
    """
    if placed_tile != "":
        set_combination = set()
        for i in range(3,len(rack)+2):
            for x in itertools.combinations(rack+placed_tile,i):
                if placed_tile in x:
                    set_combination.add(x)
    
    elif placed_tile == "":
        set_combination = set()
        for i in range(3,len(rack)+1):
            for x in itertools.combinations(rack,i):
                set_combination.add(x)  
        
    return set_combination

    
def generate_words(combo,scrabble_words_dict):    
    """
    This function generates words from the combination we get form the previous function.
    combo: each tuple in set_combination (the returning value of generate_combinations(rack,placed_tile) 
    function) (tuples)
    scrabble_words_dict: the returning value of read_file(fp) function (dictionary)
    Returns: a set of valid words that can be found in the input word file (set)
    """
    word_list = []
    valid_word_set = set()
    for w in itertools.permutations(combo):
        word = ''.join(w)
        word_list.append(word)
    
    for word in word_list:
        if word in scrabble_words_dict:
            valid_word_set.add(word)
    return valid_word_set
            

def generate_words_with_scores(rack,placed_tile,scrabble_words_dict):
    """
    This function generates words with its corresponding score in a dictionary.
    rack: string input containing 2-7 characters in total (strings)
    placed_tile: the tiles that are placed on the board (strings)
    scrabble_words_dict: the returning value of read_file(fp) function (dictionary)
    Returns: a dictionary containing words with its corresponding score (dictionary)
    """
    word_dict = {}
    set_combination = generate_combinations(rack,placed_tile)
    for combo in set_combination:
        valid_word_set = generate_words(combo,scrabble_words_dict)
        
        for word in valid_word_set:
            word_dict[word] = calculate_score(rack,word)
        
    return word_dict

def sort_words(word_dict):
    """
    This function sorts the dictionary that is the returning value of 
    generate_words_with_scores(rack,placed_tile,scrabble_words_dict) function.
    word_dict: the returning value of generate_words_with_scores(rack,placed_tile,scrabble_words_dict) function.
    Returns: two lists sorted by alphabetical order and scores in descending order and 
    by alphabetical order and length in descending order respectively.
    """
    list_of_tuple = []
    
    for key, value in word_dict.items():
        word = key
        score = value
        length = len(word)
        wanted_info = word, score, length
        tuple_info = tuple(wanted_info)
        list_of_tuple.append(tuple_info)
        list_of_tuple = sorted(list_of_tuple, key = itemgetter(0))
    
    return sorted(list_of_tuple, key = itemgetter(1,2), reverse = True), sorted(list_of_tuple, key = itemgetter(2,1), reverse = True)
        

def display_words(word_list,specifier):
    """
    This function displays the first 5 words sorted by score and length.
    word_list: one of the two lists which are the returning values of sort_words(word_dict) function.
    specifier: input strings indicating what we want it to be sorted by (score or length) (strings)
    Displays: first 5 sorted words by score and length in descending order
    
    """

    if specifier == 'score':
        
        print("Word choices sorted by Score")
        print("{:>6s}  -  {:s}".format("Score","Word"))
        
        if len(word_list) <= 5:
            count = 0
            for info in word_list:
                print("{:>6d}  -  {:s}".format(info[1],info[0]))
                count += 1
                if count > len(word_list):
                    break
                
        elif len(word_list) > 5:
            count = 0
            for info in word_list:
                
                print("{:>6d}  -  {:s}".format(info[1],info[0]))
                count += 1
                if count >= 5:
                    break
                
    elif specifier == 'length':
        print("\nWord choices sorted by Length")
        print("{:>6s}  -  {:s}".format("Length","Word"))
        
        if len(word_list) <= 5:
            count = 0
            for info in word_list:
                print("{:>6d}  -  {:s}".format(info[2],info[0]))
                count += 1
                if count > len(word_list):
                    break
                
        elif len(word_list) > 5:
            count = 0
            for info in word_list:
                
                print("{:>6d}  -  {:s}".format(info[2],info[0]))
                count += 1
                if count >= 5:
                    break
                    
def main():
    ''' 
        This function is the main function that is executed automatically
        while the program is running.
        no parameters
        Returns: the result depends on the loop and conditions within 
        the function.  
    '''
    
    print("Scrabble Tool")
    answer = input("Would you like to enter an example (y/n): ")
    while True:
        if answer == 'y':   #continue the program if the user enters 'y'
            fp = open_file()
            scrabble_words_dict = read_file(fp)
            
            #while loop to prompt for the rack
            while True:
                rack = input("Input the rack (2-7chars): ")
                if rack.isalpha() == False:   #check whether it all are characters
                    print("Error: only characters and 2-7 of them. Try again.") #display an error statement if not
                    continue
                
                else: #check number of characters: the rack must be 2-7 characters only
                    if len(rack) >= 2 and len(rack) <= 7: 
                        break
                    else:  #display an error statement if not
                        print("Error: only characters and 2-7 of them. Try again.")
                        continue
                
            #while loop displaying words with sorted by score in descending order    
            while True:  
                tiles = input("Input tiles on board (enter for none): ")
                if tiles != "": #conditions for tiles not an empty string
                    if tiles.isalpha() == False: #check if tiles contain only characters 
                        print("Error: tiles must be characters or empty")   
                        continue
                    else:
                        break
                elif tiles == "": #if tiles an empty string then exit the loop and continue the program
                    break

                
            word_dict1 = {} 
            #get all generated words into a dictionary as keys with score for each as its value. Then display the results.
            if tiles != "":
                for placed_tile in tiles:
                    word_dict = generate_words_with_scores(rack,placed_tile,scrabble_words_dict)
                    word_dict1.update(word_dict)
                    
            elif tiles == "":
                word_dict = generate_words_with_scores(rack,"",scrabble_words_dict)
                word_dict1.update(word_dict)
            

            sortedlist_score, sortedlist_length = sort_words(word_dict1)
        
            display_words(sortedlist_score,'score')
            display_words(sortedlist_length,'length')
            answer = input("Do you want to enter another example (y/n): ") #ask the user whether or not to continue
            continue
        
        #exit the program if 'n' is the input
        elif answer == 'n':
            print("Thank you for playing the game")
            break
    
# this was added to make functions to be tested individually on mirmir 
if __name__ == "__main__":
    main()        
    


