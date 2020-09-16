###############################################################################
#    Programming Project #7
#
#    Algorithm
#        display header
#        call function to open file
#            prompt for strings (a file name)
#            loop while the input is incorrect
#                reprompt for strings (a file name)
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
#        exit the program if the input for choice in lowercase is '4' 
############################################################################### 

import matplotlib.pyplot as plt #import the module for plotting
import csv                      #import csv module
from operator import itemgetter #import the module for sorting

MIN_YEAR = 2009    #value of minimum year 
MAX_YEAR = 2017    #value of maximum year


def open_file_csv(prompt_str):
    '''
    Open a file (.csv). 
    No parameters
    Returns: the opened file for reading only (fp).
    '''
    #while loop to reprompt for input if it's incorrect
    while True:
        
        try:                           #open the file if successful
            fp = open(prompt_str, "r", encoding="utf-8") 
            break
        except FileNotFoundError:      #display error message if not successful
            print("File not found! Try Again!") 
            prompt_str = input("Enter the travel data file: ")
    return fp

def open_file_txt(prompt_str):
    '''
    Open a file (.txt). 
    No parameters
    Returns: the opened file for reading only (fp).
    '''
    #while loop to reprompt for input if it's incorrect
    while True:
        
        try:                           #open the file if successful
            fp = open(prompt_str, "r", encoding="utf-8") 
            break
        except FileNotFoundError:      #display error message if not successful
            print("File not found! Try Again!") 
            prompt_str = input("Enter the country code file: ")
    return fp


def read_country_code_file(fp):
    ''' 
    This function read through fp the returning value of open_file_txt(prompt_str)
    function and get country code and country name in tuples and add them to a list 
    and get it sorted by country code.
    fp: returning value of open_file_txt(prompt_str) function.
    Returns: a list containing tuples of country code and country name 
    
    '''
    fp.seek(0)       #start reading file at the beginning
    fp.readline()    #skip the first line
    list_country_code = []  #start list containing tuples of code and country with an empty list 
    for line in fp:
        line = line.strip("\n")
        line = line.split("/")
        line = tuple(line)
        list_country_code.append(line)
    return sorted(list_country_code, key=itemgetter(0)) #sort the list by code alphabetically

def read_travel_file(fp):
    ''' 
    This function read through a csv file based on fp returning value of 
    open_file_csv(prompt_str) function and collect data. Then put the wanted data
    into separately lists with different years.
    fp: returning value of open_file_txt(prompt_str) function.
    Returns: a big list containing lists of different years.
    
    '''
    reader = csv.reader(fp) #read through flie as a csv file 
    next(reader, None) #skip reading the first line
    
    #get data for each year separately in different lists
    list_2009 = []
    list_2010 = []
    list_2011 = []
    list_2012 = []
    list_2013 = []
    list_2014 = []
    list_2015 = []
    list_2016 = []
    list_2017 = []
    
    travel_file_list = [] #create travel_file_list of year lists
    
    #so sclicing to get wanted information from the file
    for line in reader:
        year = int(line[0])
        country_name = line[1][:20]
        country_code = line[2]
        num_departures = int(line[3])
        num_arrivals = int(line[4])
        expenditures = float(line[5])
        receipts = float(line[6])
        
        #convert values of wanted info to the required forms preparing for further calculations
        num_departures = num_departures / 1000 
        expenditures = expenditures / 1000000
        num_arrivals = num_arrivals / 1000 
        receipts = receipts / 1000000 
        
        #conditions for average expenditures calculation

        if num_departures == 0:
            avg_expenditures = 0   
        else:
            
            avg_expenditures = round((expenditures/num_departures)*1000, 2)
            
        #conditions for average arrivals calculation   
        
        if num_arrivals == 0:
            avg_arrivals = 0
            
        else:
            
            avg_arrivals = round((receipts/num_arrivals)*1000, 2)
            
        #create tuples of wanted information    
        wanted_info = year, country_name, country_code, num_arrivals, num_departures, expenditures, receipts, avg_expenditures, avg_arrivals
        tuples_info = tuple(wanted_info)
        
        #add those tuples into separately list of different years
        if tuples_info[0] == 2009:
            list_2009.append(tuples_info)
        elif tuples_info[0] == 2010:
            list_2010.append(tuples_info)
        elif tuples_info[0] == 2011:
            list_2011.append(tuples_info)
        elif tuples_info[0] == 2012:
            list_2012.append(tuples_info)
        elif tuples_info[0] == 2013:
            list_2013.append(tuples_info)
        elif tuples_info[0] == 2014:
            list_2014.append(tuples_info)
        elif tuples_info[0] == 2015:
            list_2015.append(tuples_info)
        elif tuples_info[0] == 2016:
            list_2016.append(tuples_info)
        elif tuples_info[0] == 2017:
            list_2017.append(tuples_info)
            
    #sort each list by country name
    travel_file_list.append(sorted(list_2009, key=itemgetter(1)))
    travel_file_list.append(sorted(list_2010, key=itemgetter(1)))
    travel_file_list.append(sorted(list_2011, key=itemgetter(1)))
    travel_file_list.append(sorted(list_2012, key=itemgetter(1)))
    travel_file_list.append(sorted(list_2013, key=itemgetter(1)))
    travel_file_list.append(sorted(list_2014, key=itemgetter(1)))
    travel_file_list.append(sorted(list_2015, key=itemgetter(1)))
    travel_file_list.append(sorted(list_2016, key=itemgetter(1)))
    travel_file_list.append(sorted(list_2017, key=itemgetter(1)))
    
    return travel_file_list
            
            
def get_country_code_data(country_code, data_list): 
    '''
    This function create a list of data for a country based on the input of 
    country_code.
    country_code: three upper case letters refering to a country name (str)
    data_list: returning value of read_travel_file(fp) function
    Returns: list of data for a country or None
    
    '''
    country_code_list = []       
    for lists in data_list:
        for tup in lists:
            if country_code in tup:
                country_code_list.append(tup)
            else:
                continue
    try:
        country_code_list != []
        return country_code_list
    except:
        return None

def display_country_data(country_list):
    '''
    This function displays data for a country.
    country_list: returning value of get_country_code_data(country_code, data_list) function
    Returns: None
    
    '''
    sum_depart = 0
    sum_arrivals = 0
    sum_ex = 0
    sum_rec = 0
    for tup in country_list:
        sum_depart += tup[4]
        sum_arrivals += tup[3]
        sum_ex += tup[5]
        sum_rec += tup[6] 
        print("{:<6d} {:>15,.2f} {:>15,.2f} {:>15,.2f} {:>15,.2f}".format(tup[0],tup[4],tup[3], tup[5],tup[6]))
    print("\n{:<6s} {:>15,.2f} {:>15,.2f} {:>15,.2f} {:>15,.2f}".format("Total",sum_depart,sum_arrivals,sum_ex,sum_rec))     



def create_year_list(year_input, data_list):
    '''
    This function create list of yearly data.
    year_input: year (int)
    data_list: returning value of read_travel_file(fp) function
    Returns: a list of data for a year 
    '''
    year_list = []       
    for lists in data_list:
        for tup in lists:
            if year_input == tup[0]:
                year_list.append(tup)
            else:
                continue
    return year_list  
            

def display_year_data(year_list):
    '''
    This function display data for a year from year_list plus sum for every data
    at the bottom line.
    year_list: returning value of create_year_list(year_input, data_list) function.
    Returns: None 
    '''
    sum_depart = 0
    sum_arrivals = 0
    sum_ex = 0
    sum_rec = 0
    for tup in year_list:
        sum_depart += tup[4]
        sum_arrivals += tup[3]
        sum_ex += tup[5]
        sum_rec += tup[6]
        print("{:<20s} {:>15,.2f} {:>15,.2f} {:>15,.2f} {:>15,.2f}".format(tup[1],tup[4],tup[3], tup[5],tup[6]))
    print("\n{:<20s} {:>15,.2f} {:>15,.2f} {:>15,.2f} {:>15,.2f}".format("Total",sum_depart,sum_arrivals,sum_ex,sum_rec))
    
def prepare_bar_plot(year_list):
    '''
    This function prepares data for bar plotting.
    year_list: returning value of create_year_list(year_input, data_list) function.
    Returns: average expenditures list and average reciepts list sorted by average expenditures
    and average reciepts in descending order.
    '''
    list_avg_ex = []
    count = 0
    year_list = sorted(year_list, key = lambda tup: tup[7], reverse = True)
    
    for tup in year_list:
       
            country_name = tup[1]
            avg_ex = tup[7]
            info_avg_ex = country_name, avg_ex
            tuple_avg_ex = tuple(info_avg_ex)
            list_avg_ex.append(tuple_avg_ex)
            count += 1
            if count == 20:
                break
    
    list_avg_ex = sorted(list_avg_ex, key = itemgetter(1), reverse = True)
    
    list_avg_rec = []
    count = 0
    year_list = sorted(year_list, key = lambda tup: tup[8], reverse = True)
    
    for tup in year_list:
       
            country_name = tup[1]
            avg_rec = tup[8]
            info_avg_rec = country_name, avg_rec
            tuple_avg_rec = tuple(info_avg_rec)
            list_avg_rec.append(tuple_avg_rec)
            count += 1
            if count == 20:
                break
    
    list_avg_rec = sorted(list_avg_rec, key = itemgetter(1), reverse = True)
    
    return list_avg_ex, list_avg_rec 

def prepare_line_plot(country_list):
    '''
    This function prepares data for line plotting.
    country_list: returning value of get_country_code_data(country_code, data_list) function.
    Returns: average expenditures list and average reciepts list
    '''
    
    list_avg_ex = []
    list_avg_rec = []
    for tup in country_list:
        avg_ex = tup[7]
        list_avg_ex.append(avg_ex)
        avg_rec = tup[8]
        list_avg_rec.append(avg_rec)  
    
    
    return list_avg_ex, list_avg_rec

def plot_bar_data(expend_list, receipt_list, year):
    '''
        This function plots the the top 20 countries with the highest average
        expenditures and the top 20 countries with the highest receipts.
        
        Returns: None
    
    '''

    # prepare the columns
    countries_expend = [elem[0] for elem in expend_list]
    values_expend = [elem[1] for elem in expend_list]
    
    countries_receipt = [elem[0] for elem in receipt_list]
    values_receipt = [elem[1] for elem in receipt_list]
    
    # Average expenditures
    
    x = range(20) # top 20 countries are to be plotted.

    fig, axs = plt.subplots(2, 1,figsize=(7,10))
    title = "Top 20 countries with highest average expenditures {:4d}".format(year)
    axs[0].set_title(title)
    axs[0].bar(x, values_expend, width=0.4, color='b')
    axs[0].set_ylabel("Avg. Expenditures (US dollar)")
    axs[0].set_xticks(x)
    axs[0].set_xticklabels(countries_expend , rotation='90')
    
    # Average receipt
    title = "Top 20 countries with highest average receipt  {:4d}".format(year)
    axs[1].set_title(title)
    axs[1].set_ylabel("Avg. Receipts (US dollar)")
    axs[1].bar(x, values_receipt, width=0.4, color='b')
    axs[1].set_xticks(x)
    axs[1].set_xticklabels(countries_receipt , rotation='90')
    fig.tight_layout()
    plt.show()
    
    ##comment the previous line and uncomment the following two lines when trying to pass Test 4
#    fig.savefig('avg_expense_receipts.png',dpi=100)
#    fig.clf()
def plot_line_data(country_code, expend_list, receipt_list):
    '''
        Plot the line plot for the expenditures and receipts for the
        country between 2009 and 2017
        
        Returns: None
    '''
    
    
    title = "Average expenditures and receipts for {} between 2009 and 2017".format(country_code)
    years = range(MIN_YEAR, MAX_YEAR+1)
    fig, axs = plt.subplots(figsize=(7,5))
    axs.set_title(title)
    axs.set_ylabel("Cost (US dollar)")
    axs.plot(years, expend_list, years, receipt_list)
    axs.legend(['Expenditures','Receipt'])

    plt.show()
    
    ##comment the previous line and uncomment the following two lines when trying to pass Test 4
#    fig.savefig('line.png',dpi=100)
#    fig.clf()





def main():
    ''' 
        This function is the main function that is executed automatically
        while the program is running.
        no parameters
        Returns: the result depends on the loop and conditions within 
        the function.  
    '''
    BANNER = "\nInternational Travel Data Viewer\
\n\nThis program reads and displays departures, arrivals, expenditures, "\
"and receipts for international travels made between 2009 and 2017."
    OPTION = "\nMenu\
\n\t1: Display data by year\
\n\t2: Display data by country\
\n\t3: Display country codes\
\n\t4: Stop the Program\
\n\n\tEnter option number: "
    
    print(BANNER)
    
    file_name_travel = input("Enter the travel data file: ")
    fp = open_file_csv(file_name_travel)    #open csv file
    data_list = read_travel_file(fp)
    
    
    file_name_cc = input("Enter the country code file: ") #open txt file
    fp = open_file_txt(file_name_cc)
    list_country_code = read_country_code_file(fp)
    
    choice = input(OPTION)  #input a choice
    
    
    #while loop to reprompt for a choice number
    while choice.lower() != '4':    #end the program when input is '6'
        
        #conditions for choice #1: Top sites by country
        if choice == '1':
            year_input = int(input("Enter year: "))
            li_year = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
            while True:
                if year_input not in li_year: 
                    print("Year needs to be between 2009 and 2017. Try Again!")
                    year_input = int(input("Enter year: "))
                    continue
                    
                elif year_input in li_year: 
                    break
                    
            year_list = create_year_list(year_input, data_list)
            print("\t\t\t\tTravel Data for", year_input)
            print("{:<20s} {:>15s} {:>15s} {:>15s} {:>15s}".format("Country Name","Departures","Arrivals","Expenditures","Receipts"))        
            print("{:<20s} {:>15s} {:>15s} {:>15s} {:>15s}".format(" ","(thousands)","(thousands)","(millions)","(millions)"))      
            display_year_data(year_list)
            
            
            #ask users for plotting
            plot = input("Do you want to plot (yes/no)?").lower() 
            if plot == 'yes':
                expend_list, receipt_list = prepare_bar_plot(year_list)
                year = year_input
                plot_bar_data(expend_list, receipt_list, year)
                choice = input(OPTION) 
            elif plot == 'no':
                choice = input(OPTION) 
                
         
        #conditions for choice #2: Display data by country   
        elif choice == '2':
            code_list = []
           
            for lists in data_list:
                for tup in lists:
                    cc = tup[2]
                    code_list.append(cc)
          
            country_code = input("Enter country code: ").upper()
                    
                        
            if country_code not in code_list:
                print("Country code is not found! Try Again!")
                continue
            
            elif country_code in code_list:
                country_list = get_country_code_data(country_code, data_list)
                
            #get country name for header            
            country_code_list = read_country_code_file(fp) 
            country_name = " "
            for tup in country_code_list:
                if tup[0] == country_code:
                    country_name = tup[1]
                    break
            
            
            print("\t\t\t   Travel Data for", country_name)
            print("{:<6s} {:>15s} {:>15s} {:>15s} {:>15s}".format("Year","Departures","Arrivals","Expenditures","Receipts"))        
            print("{:<6s} {:>15s} {:>15s} {:>15s} {:>15s}".format(" ","(thousands)","(thousands)","(millions)","(millions)"))      
            
                        
            display_country_data(country_list)
            
            
            #ask users for plotting
            plot = input("Do you want to plot (yes/no)?").lower()
            if plot == 'yes':
                prepare_line_plot(country_list)
                expend_list_forline, receipt_list_forline = prepare_line_plot(country_list)  
                plot_line_data(country_code, expend_list_forline, receipt_list_forline)
                
                choice = input(OPTION)
                
            elif plot == 'no':
                choice = input(OPTION)
                
        
        
    
        #conditions for choice #3: Display country codes
        elif choice == '3':
            print("\nCountry Code Reference")
            print("{:15s}{:25s}".format("Country Code", "Country Name"))
            for tup in list_country_code:
                print("{:15s}{:25s}".format(tup[0], tup[1]))
                
        
            
            choice = input(OPTION)
        
        
        #display error message for invalid input choice number
        #reprompt for a choice number
        else:
            print("Invalid option. Try Again!")
            choice = input(OPTION)
            
    #quit the program if the lowercase of the choice is '4'       
    if choice.lower() == '4': 
        print("\nThanks for using this program!")
        
            
    
# this was added to make functions to be tested individually on mirmir 
if __name__ == "__main__": 
    main() 
    
