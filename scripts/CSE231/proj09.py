#############################################################################################
#    Programming Project #9
#
#    Algorithm
#        display banner
#        display choices
#        prompt for a string (a choice)
#        loop while the input is incorrect
#            reprompt for a string (a valid choice)
#        call function to open file
#            prompt for strings (a file name)
#            loop while the input is incorrect
#                reprompt for strings (a valid file name)
#        display outputs or prompt for futher input(s) depending on the input for choice.
#        prompt for a string (a choice)
#        loop while the input is incorrect
#            reprompt for a string (a valid choice)
#        exit the program if the input for choice is '5' 
############################################################################################ 

import csv   #import csv module to read .csv file
from operator import itemgetter   #import itemgetter module to do sorting
import matplotlib.pyplot as plt  #import matplotlib.pyplot for plotting
import numpy as np    #import numpy for multidimensional array object


def open_file(message):
    '''
    Open a file (.txt). 
    message: a valid name file
    Returns: a file pointer (fp).
    '''
    #while loop to reprompt for input if it's incorrect
    while message != "":
        try: 
            fp = open(message, encoding = "utf8")  #open the file if successful
            break
        except FileNotFoundError:      #display error message if not successful
            print("File not found. Try again.") 
            message = input("Enter the file name: ")
            continue
        
    if message == "": #open breachdata.csv if the input is an empty string
        fp = open("breachdata.csv", encoding = "utf8")  
            
    return fp

def build_dict(reader):
    '''
    This function take the reader of the file pointer from open_file(message) function
    to build a dictionary containg 2 dictionaries inside.
    reader: csv.reader(fp)
    Returns: a big dictionary with 2 info dictionaries inside.
    '''
    next(reader,None)   #skip the header line
    
    dict_entity = {}
    
    
    for line in reader:
        dict_info1 = {}
        dict_info2 = {}
        
        #get the needed info from each line
        entity = line[0].strip()
        records_lost = line[2].replace(",","")
        if records_lost == "": #set records_lost equal 0 if the info is an empty string
            records_lost = 0
        else:
            records_lost = int(line[2].replace(",","")) #if not, then convert it to an integer
            
        year = line[3].strip()
        if year.isdigit():
            year = int(year) #check if the year is valid
        else:
            continue   #if not, skip the line 
        
        story = line[4].strip()
        if story == "" :   #skip line if the info is an empty string
            continue
        
        sector = line[5].strip() 
        if sector == "":   #skip line if the info is an empty string
            continue
        
        method = line[6].strip()
        if method == "":   #skip line if the info is an empty string
            continue
        
        news_sources = line[11].strip()
        if news_sources == "":   #skip line if the info is an empty string
            continue
        else:
            news_sources = news_sources.split(",")
        
        #get all needed info into tuples
        info1 = records_lost, year, story, news_sources
        info1_tuple = tuple(info1)
        info2 = sector, method
        info2_tuple = tuple(info2) 
        dict_info1[entity] = info1_tuple
        dict_info2[year] = info2_tuple
        mix = dict_info1, dict_info2
        mix_tuple = tuple(mix)
        
        #build the dictionary
        if entity not in dict_entity:
            dict_entity[entity] = []
            
        if entity in dict_entity:
            
            dict_entity[entity].append(mix_tuple)     
            
    return dict_entity
       
      
    
def top_rec_lost_by_entity(dictionary):
    '''
     This fuction takes the dictionary which is the returning value of build_dict(reader) 
     to build a list of tuples of top 10 records lost by entity
     dictionary: the returning value of build_dict(reader)
     Returns: a list of tuples of top 10 records lost by entity
    '''
    dict_info = {}
    list_tup = []
    
    for value1 in dictionary.values():
        for tup in value1:
            dictt = tup[0]
            for key2 in dictt:
                for value2 in dictt.values():
                    if key2 not in dict_info:
                        dict_info[key2] = []
                    if key2 in dict_info:
                        dict_info[key2].append(value2[0])
            
    count = 0 
    for key, value in dict_info.items():
        sum_values = sum(value)
        
          
        info_tup = key, sum_values
        
        list_tup.append(info_tup) 
        
    list_tup = sorted(list_tup, key = itemgetter(1,0), reverse = True)    
    list_tup_new = []  
    for tup in list_tup:
        list_tup_new.append(tup)
        count += 1
        if count == 10:
            break
            
    
    return list_tup_new


def records_lost_by_year(dictionary):
    '''
    This fuction takes the dictionary which is the returning value of build_dict(reader) 
    to build a list of tuples of top records lost by year
    dictionary: the returning value of build_dict(reader)
    Returns: a list of tuples of top records lost by year
    '''
    dict_year = {}
    list_year = []
    for value in dictionary.values():
        for tup in value:
           dictt = tup[0]
           for value1 in dictt.values():
               if value1[1] not in dict_year:
                   dict_year[value1[1]] = []
               if value1[1] in dict_year:
                   dict_year[value1[1]].append(value1[0])
    #create a list of tuples of top records lost by year
    for key, value in dict_year.items():
        sum_values = sum(value)
        
          
        info_tup = key, sum_values
        
        list_year.append(info_tup) 
    
    return sorted(list_year, key = itemgetter(1), reverse = True)  
    

def top_methods_by_sector(dictionary):
    '''
    This fuction takes the dictionary which is the returning value of build_dict(reader) 
    to build a dictionary of dictionaries (keys: sectors, values: dictionay with method as key and the 
    corresponding count as value)
    dictionary: the returning value of build_dict(reader)
    Returns: a dictionary of dictionaries 
    '''
    dict_secter = {}
    dict_secter_sorted = {}
    for value in dictionary.values():
        for tup in value:
            dictt = tup[1]
            for value1 in dictt.values():
                if value1[0] not in dict_secter:
                    dict_secter[value1[0]] = dict() 
                if value1[0] in dict_secter:
                    if value1[1] not in dict_secter[value1[0]]:
                        dict_secter[value1[0]][value1[1]] = 0
                    if value1[1] in dict_secter[value1[0]]:
                        dict_secter[value1[0]][value1[1]] += 1
                        
    sortedlist_dict = sorted(dict_secter)
    for element in sortedlist_dict:
        dict_secter_sorted[element] = dict_secter[element]
            
    return dict_secter_sorted
        
def top_rec_lost_plot(names,records):
    ''' Plots a bargraph pertaining to
        the cybersecurity breaches data '''
        
    y_pos = np.arange(len(names))

    plt.bar(y_pos, records, align='center', alpha=0.5,
            color='blue',edgecolor='black')
    plt.xticks(y_pos, names, rotation=90)
    plt.ylabel('#Records lost')
    plt.title('Cybersecurity Breaches',fontsize=20)
    plt.show()
    
def top_methods_by_sector_plot(methods_list):
    ''' Plots the top methods used to compromise
        the security of a sector '''
    methods = [] ; quantities = []
    for tup in methods_list:
        methods.append(tup[0])
        quantities.append(tup[1])
    labels = methods
    sizes = quantities
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

    plt.pie(sizes, labels=labels, colors = colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    
    plt.axis('equal')
    plt.show()
    
def main():
    BANNER = '''
    
                 _,.-------.,_
             ,;~'             '~;, 
           ,;                     ;,
          ;                         ;
         ,'                         ',
        ,;                           ;,
        ; ;      .           .      ; ;
        | ;   ______       ______   ; | 
        |  `/~"     ~" . "~     "~\'  |
        |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
         |   |        }:{        |   | 
         |   l       / | \       !   |
         .~  (__,.--" .^. "--.,__)  ~. 
         |     ---;' / | \ `;---     |  
          \__.       \/^\/       .__/  
           V| \                 / |V  
            | |T~\___!___!___/~T| |  
            | |`IIII_I_I_I_IIII'| |  
            |  \,III I I I III,/  |  
             \   `~~~~~~~~~~'    /
               \   .       .   /
                 \.    ^    ./   
                   ^~~~^~~~^ 
                   
           
           ~~Cybersecurity Breaches~~        
                   @amirootyet    
                
    '''
    
    print(BANNER)
    
    MENU = '''  
[ 1 ] Most records lost by entities
[ 2 ] Records lost by year
[ 3 ] Top methods per sector
[ 4 ] Search stories
[ 5 ] Exit

'''
    print(MENU)
    choice = input("[ ? ] Choice: ")
    if choice == '1' or choice == '2' or choice == '3' or choice == '4':
        message = input("[ ? ] Enter the file name: ")
    while True:
        
        if choice == '1': #Most records lost by entities
            
            fp = open_file(message)
            reader = csv.reader(fp)
            dictionary = build_dict(reader)
            top_entities_list = top_rec_lost_by_entity(dictionary) 
            print("[ + ] Most records lost by entities...")
            rank = 0
            for tup in top_entities_list:
                rank += 1
                print("-"*45)
                print("[ {:2d} ] | {:15.10s} | {:10d}".format(rank, tup[0], tup[1]))
            
            names = []
            records = []
            for tup in top_entities_list:
                names.append(tup[0])
                records.append(tup[1])
            plot = input("[ ? ] Plot (y/n)? ")
            if plot == 'y':
                top_rec_lost_plot(names,records)
                print(MENU)
                choice = input("[ ? ] Choice: ")
            elif plot == 'n':
                print(MENU)
                choice = input("[ ? ] Choice: ")
                
            
        elif choice == '2':   #Records lost by year
            fp = open_file(message)
            reader = csv.reader(fp)
            dictionary = build_dict(reader)
            list_year = records_lost_by_year(dictionary)
            print("[ + ] Most records lost in a year...")
            rank = 0
            for tup in list_year:
                rank += 1
                print("-"*45)
                print("[ {:2d} ] | {:15.10s} | {:10d}".format(rank, str(tup[0]), tup[1]))
            
            years = []
            records = []
            for tup in list_year:
                years.append(tup[0])
                records.append(tup[1])
            plot = input("[ ? ] Plot (y/n)? ")
            if plot == 'y':
                top_rec_lost_plot(years,records)
                print(MENU)
                choice = input("[ ? ] Choice: ")
            elif plot == 'n':
                print(MENU)
                choice = input("[ ? ] Choice: ")
             
            
        elif choice == '3': #Top methods per sector
    
            fp = open_file(message)
            reader = csv.reader(fp)
            dictionary = build_dict(reader)
            methods_dict = top_methods_by_sector(dictionary)
            print("[ + ] Loaded sector data.")
            sector_list = []
            for sector in methods_dict:
                sector_list.append(sector)
            sector_list.sort()
            for sector in sector_list:
                print(sector, end = " ")
            while True:
                secter = input("[ ? ] Sector (case sensitive)? ")
                if secter in methods_dict:
                    break
                else:
                    print("[ - ] Invalid sector name. Try again.")
                    continue
            print("[ + ] Top methods in sector {}".format(secter))
            
            
            methods_list = []
            for method, count in methods_dict[secter].items():
                
                tup_info = method, count
                methods_list.append(tup_info)
                methods_list = sorted(methods_list, key = itemgetter(1), reverse = True)
            rank = 0    
            for tup in  methods_list:
                rank += 1
                print("-"*45)
                print("[ {:2d} ] | {:15.10s} | {:10d}".format(rank, tup[0], tup[1]))
        
        
            plot = input("[ ? ] Plot (y/n)? ")
            if plot == 'y':
                top_methods_by_sector_plot(methods_list)
                print(MENU)
                choice = input("[ ? ] Choice: ")
            elif plot == 'n':
                print(MENU)
                choice = input("[ ? ] Choice: ")
            
            
            
        elif choice == '4':  #Search stories
            fp = open_file(message)
            reader = csv.reader(fp)
            dictionary = build_dict(reader)
            while True:
                entity = input("[ ? ] Name of the entity (case sensitive)? ")
                if entity in dictionary:
                    break
                else:
                    print("[ - ] Entity not found. Try again.")
                    continue
                
            list_story = []
            count_story = 0
            for key, list_info in dictionary.items():
                if key == entity:
                    for tup in list_info:
                        count_story += 1
                        for key, value in tup[0].items():
                            story = value[2]
                        
                            list_story.append(story)
                        
                
            print("[ + ] Found {} stories:".format(count_story))
            rank = 0
            for story in list_story:
                rank +=1
                print("[ + ] Story {}: {:10s}".format(rank, story))
            
            print(MENU)
            choice = input("[ ? ] Choice: ")
        
        #exit the program if the input for choice is '5'    
        elif choice == '5':
            print("[ + ] Done. Exiting now...")
            break
        #display errors if the input is invalid
        else:
            print('[ - ] Incorrect input. Try again.')
            print(MENU)
            choice = input("[ ? ] Choice: ")
    


            
# this was added to make functions to be tested individually on mirmir 
if __name__ == "__main__":
     main()
     
