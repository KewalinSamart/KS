###############################################################################
#    Programming Project #6
#
#    Algorithm
#        display header
#        call function to open file
#            prompt for strings (a file name)
#            loop while the input is incorrect
#                reprompt for strings (a file name)
#        display choices
#        prompt for an integer (a choice number)
#        loop while the input is incorrect
#            reprompt for an integer (a choice number)
#        call a fuction chosen corresponding to the choice no.
#            prompt for input(s) depending on the function called
#            loop while the input(s) is/are incorrect
#                reprompt for input(s)
#            display output(s) 
#        exit the program if the input for choice in lowercase is 'q' 
###############################################################################       

import csv #import csv module for reading csv file
from operator import itemgetter #import itemgetter for sorting

def open_file():
    '''
    Open a file (.csv). 
    No parameters
    Returns: the opened file for reading only (fp).
    '''
    #while loop to reprompt for input if it's incorrect
    while True:
        file_name = input("Input a filename: ") #prompt for a file name
        
        try:                           #open the file if successful
            fp = open(file_name, encoding="ISO-8859-1") 
            break
        except FileNotFoundError:      #display error message if not successful
            print("Error: file not found.") 
            
    return fp
            
            
def read_file(fp):
    '''
    Read through each line in the file 'fp' and collect wanted data such as
    rank, website URL, average daily page views, and country in tuples and then
    add each tuple into a list.
    fp: returning value of the open_file() fuction.
    Returns: a list of tuples sorted by rank and country respectively
    
    '''
    fp.seek(0)   #start reading file at the beginning of the file
    reader = csv.reader(fp) #read through flie as a csv file 
    next(reader, None) #skip reading the first line
    list1 = []  #start with an empty list
        
    for line in reader:   
        
        #get wanted data from each line in tuples and add it to the empty list
        try: 
        
            rank = int(line[0].strip())
        
            website = line[1].strip()
        
            traffic = int(line[14].strip().replace(" ",""))
        
            page_views = int(line[5].strip().replace(" ",""))
        
            country = line[30].strip()
        
            a = rank, website, traffic, page_views, country
        
            wanted_tuple = tuple(a)
        
            list1.append(wanted_tuple) 
    
    
        except ValueError:    #skip line that contains N/A NA
            continue
            
        
    return sorted(list1, key=itemgetter(0,4)) 


def remove_duplicate_sites(list1):
    '''
    Remove duplicate sites if there is any website domain appears more than once
    in the list.
    list1: the returning value of the read_file(fp) function 
    Returns: a list of tuples with no duplicated website domains sorted by 
             rank and website respectively
    
    '''
    list2 = [] #start the returning list with an empty list
    list_web = [] #start the list of website domains with an empty list
    
    #for loop to build a list of website domains 
    for tuplee in list1:
        dot_position = 0  #initial value of index of second dot position in URL 
        
        #for loop to slicing website domains                                    
        for n, ch in enumerate(tuplee[1][4:]):
            if ch == ".":
                
                dot_position = n + 4
                 
                web = tuplee[1][4:dot_position]
                break
        
        #condition for creating a list of tuples with no duplicated sites
        if web not in list_web:
            list_web.append(web)   
            list2.append(tuplee)
            
                
    return sorted(list2, key=itemgetter(0,1)) 
            
    
            
def top_sites_per_country(list1, country_name):
    '''
    Create a list of 20 top sites for a particular country 
    list1: the returning value of the read_file(fp) function 
    country_name: selected country to display the 20 top sites (strings) 
    Returns: a list containing 20 tuples with first 20 top views of the country
    
    '''
    list3 = [] #start list of 20 top sites per country with an empty list
    count = 0  #initial number of sites
    for tuplee in list1:
        if tuplee[4] == country_name:
            list3.append(tuplee) 
            count += 1
            if count == 20:
                break
    list4 = sorted(list3, key=itemgetter(0)) #sort the 20 top sites list by rank
    return list4 

      

def top_sites_per_views(list1):
    '''
    Create a list of 20 top sites based on views 
    list1: the returning value of the read_file(fp) function 
    Returns: a list containing 20 tuples with first 20 top views 
             sorted by views and reverse to get descending orders 
    
    '''
    #sorted by views and reverse to get descending orders 
    list5 = sorted(list1, key=itemgetter(3), reverse = True) 
    #remove duplicated sites
    list6 = remove_duplicate_sites(list5) 
    #sorted by views and reverse to get descending orders 
    list8 = sorted(list6, key=itemgetter(3), reverse = True )

    list7 = []
    #get first 20 top sites based on views
    for i in range(20): 
        list7.append(list8[i])
        
    return sorted(list7, key=itemgetter(3), reverse = True )


def main():
    header = '''----- Web Data -----'''
    choices = ''' 
Choose
         (1) Top sites by country
         (2) Search by web site name
         (3) Top sites by views
         (q) Quit '''

    print(header)
    fp = open_file()    #open file
    list1 = read_file(fp) #refer list1 to read_file(fp) function 
    print(choices)
    choice = input("Choice: ")  #input a choice
    
    
    #while loop to reprompt for a choice number
    while choice.lower() != 'q':    #end the program when input is '6'
        
        #conditions for choice #1: Top sites by country
        if choice == '1':
            print("--------- Top 20 by Country -----------")
            country_name = input("Country: ")
            country_list = top_sites_per_country(list1, country_name)
            print("{:30s}  {:>15s} {:>30s}".format("Website" , "Traffic Rank", "Average Daily Page Views"))
            for tuplee in country_list: 
                website = tuplee[1]
                traffic_rank = tuplee[2]
                page_views = tuplee[3]
            
                
                print("{:30s}  {:>15d} {:>30,d}".format(website, traffic_rank, page_views))
                
            print(choices)
            choice = input("Choice: ")
            
        #conditions for choice #2: Search by web site name
        elif choice == '2':
            list_web = []
            list_search = []
            keyword = input("Search: ").lower()
            print("{:^50s}".format("Websites Matching Query"))
            
            for tuplee in list1:
                list_web.append(tuplee[1])
            
            
            for web in list_web:
                
                if keyword in web:
                    list_search.append(web)
                    
            if list_search != []:     
                for web_search in list_search:
                    print("{:<10s}".format(web_search)) 
            else:
                print("None found")
                    
                 
            print(choices)
            choice = input("Choice: ")  
    
        #conditions for choice #3: Top sites by views
        elif choice == '3':
            print("--------- Top 20 by Page View -----------")
            print("{:30s}  {:>15s}".format("Website","Ave Daily Page Views"))
            top_view = top_sites_per_views(list1)
            for tuplee in top_view:
                website = tuplee[1]
                views = tuplee[3]
                
                print("{:30s}  {:>20,d}".format(website,views))
            
            
            print(choices)
            choice = input("Choice: ") 
        
        
        #display error message for invalid input choice number
        #reprompt for a choice number
        else:
            print("Incorrect input. Try again.")
            print(choices)
            choice = input("Choice: ")
            
    #quit the program if the lowercase of the choice is 'q'       
    if choice.lower() == 'q': 
        None
            
    
# this was added to make functions to be tested individually on mirmir 
if __name__ == "__main__": 
    main() 
