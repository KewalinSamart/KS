#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:36:10 2019

@author: ks.mammie
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 18:24:40 2019

@author: ks.mammie
"""
###########################################################
#Programing Project #2
#
#Algorithm
#    display welcome statement
#    loop while to repeat 
#    prompt for an upper string
#    input an upper string
#    if and elif condition whether to continue or not
#    prompt for an upper string
#    input an upper string
#    loop while to check incorrect input
#        incorrect input: display an error message
#        correct input: continue the program
#    prompt for an integer
#    input an integer
#    prompt for an integer
#    input an integer
#    prompt for an integer
#    input an integer
#    if and elif conditions
#        calculations
#    calculation
#    display info summary
#    output the calculations 
###########################################################

# display welcome statemant and all the prompts
print("\nWelcome to car rentals.") 
print("\nAt the prompts, please enter the following:")
print("\tCustomer's classification code (a character: BDW)")
print("\tNumber of days the vehicle was rented (int)")
print("\tOdometer reading at the start of the rental period (int)")
print("\tOdometer reading at the end of the rental period (int)")

#loop while to repeat the program until the input gets to ending condition
while True:
    input_str = input("Would you like to continue (Y/N)? ") #input to continue or end the program
    if input_str == 'N':   #answer N is to end the program
        print("Thank you for your loyalty.") #display thankful statement
        break     #end the program
    elif input_str == 'Y':  #answer Y is to end the program
        customer_code = str(input("\nCustomer code (BDW): ")) #input a customer code
        while customer_code != 'B' and customer_code != 'D'and customer_code != 'W': #not 'BDW': loop cont. 
            print("\n\t*** Invalid customer code. Try again. ***") #display an error message to customer
            customer_code = str(input("Customer code (BDW): "))    #input a customer code again
        days_num = int(input("\nNumber of days: "))  #input an integer for number of days of rent
        miles_start = int(input("Odometer reading at the start: ")) #input an integer for initial miles
        miles_end = int(input("Odometer reading at the end: ")) #input an integer for final miles

        #conditions for total driven miles
        if miles_start < miles_end:   #condition when initial miles less than final miles
            driven_miles = (miles_end - miles_start) / 10
        elif miles_start > miles_end: #condition when initial miles greater than final miles
            driven_miles = ((miles_end + 1000000) - miles_start) / 10    
        driven_num_per_day = (driven_miles / days_num) #calculation for average driven miles per day
        
        #conditions for number of weeks
        if days_num % 7 == 0:  #condition for number of days is a 7 multiple
            weeks_num = (days_num / 7)
        else:   #condition for number of days is not a 7 multiple
            weeks_num = int(days_num / 7) + 1 #number of weeks would be round to the next integer
        driven_num_per_week = (driven_miles / weeks_num) #calculation for the average driven miles per week

        #conditions for amount due 
        if customer_code == 'B':   #budget customer conditions
            base_charge = 40 * days_num  #base charge = $40 per day
            mileage_charge = driven_miles * 0.25 #mileage charge = $0.25 per driven mile
        elif customer_code == 'D': #day customer conditions
            base_charge = 60 * days_num   #base charge = $60 per day
            if driven_num_per_day <= 100: #avg miles per day less than 100
                mileage_charge = 0
            elif driven_num_per_day > 100: #avg miles per day greater than 100
                mileage_charge = (driven_miles - (days_num * 100)) * 0.25     
        elif customer_code == 'W':  #weekly customer conditions
            base_charge = 190 * weeks_num #base charge = $190 per week 
            if driven_num_per_week <= 900: #avg miles per week less than or equals 900
                mileage_charge = 0
            elif 900 < driven_num_per_week <= 1500: #avg miles per week less than or equals 1500
                mileage_charge = 100 * weeks_num  
            elif driven_num_per_week > 1500: #avg miles per week exceeds 1500
                mileage_charge = (200 * weeks_num) + ((driven_miles - (weeks_num * 1500)) * 0.25)
        amount_due = float(base_charge + mileage_charge) #amout due is sum of base and mileage charge

        #display info summary and calculations
        print("\nCustomer summary:") #into to the displays
        print("\tclassification code:", customer_code) #display customer code
        print("\trental period (days):", days_num) #display rental period in days
        print("\todometer reading at start:", miles_start) #display initial miles
        print("\todometer reading at end: ", miles_end) #display final miles
        print("\tnumber of miles driven: ", (round(driven_miles,1))) #display total miles driven rounded to 1 place	  
        print("\tamount due: $", (round(amount_due,2))) #display amount due rounded to 2 places

        
    
    

