##############################################################################
#Programing Project #3
#
#Algorithm
#    display welcome statement
#    loop while to repeat 
#    prompt for a string input
#    input a string
#    if and elif conditions
#        prompt for a string input
#        input a string
#        loop while to check incorrect input
#            incorrect input: display an error message
#            correct input: continue the program
#        if and elif conditions (whether to prompt for further input or not)
#            prompt for a positve integer
#            input a positive integer
#            loop while to check incorrect input
#                incorrect input: display an error message
#                correct input: continue the program
#            if and elif conditions
#            calculations
#    output and display the result 
#    prompt for a string input (repeat program?)
#    input a string input
#    if and else conditions whether to continue the program 
#############################################################################

#display welcome statement
print("2019 MSU Undergraduate Tuition Calculator.\n")
#loop while to repeat
while True:
    ASMSU_tax = 21     #ASMSU tax for all undergrads 
    FM_Radio_tax = 3   #FM Radio tax for all undergrads
    fee = 0            #initial fee 
    tuition = 0        #initial tuition
    State_news_tax = 0 #initial state news tax
    
    ######## Resident ########
    resident = (input("Resident (yes/no): " )).lower() #Is the student a resident?
    if resident == 'yes':  
        level = input("Level—freshman, sophomore, junior, senior: ").lower()    #for a resident, ask for year.
        while level!='freshman'and level!='sophomore'and level!='junior'and level!='senior': #while loop for incorrect year input.
            print("Invalid input. Try again.")
            level = input("Level—freshman, sophomore, junior, senior: ").lower()
        #Resident Freshman Sophomore conditions    
        if level == 'freshman' or level == 'sophomore':
            Engineer = input("Are you admitted to the College of Engineering (yes/no): ").lower()  #admitted to Engineering? 
            #engineering student conditions
            if Engineer == 'yes':
                credit1 = input("Credits: ") #ask for credits.
                while credit1.isdigit() == False or credit1 == '0': #while loop for incorrect credits input
                    print("Invalid input. Try again.")
                    credit1 = (input("Credits: "))
                credit = int(credit1) #change the string input into an integer.
                #engineering fee conditions
                if credit <= 4 and credit > 0: 
                    fee = fee + 402
                elif credit > 4:
                    fee = fee + 670
                #state news tax condition    
                if credit > 6:   
                    State_news_tax = State_news_tax+5
                #credits charge conditions    
                if credit >= 1 and credit <= 11: 
                    if level == 'freshman':
                        tuition = 482 * credit
                    elif level == 'sophomore':
                        tuition = 494 * credit
                elif credit >= 12 and credit <= 18:
                    if level == 'freshman':
                        tuition = 7230
                    elif level == 'sophomore':
                        tuition = 7410
                elif credit > 18:
                    if level == 'freshman':
                        tuition = 7230 + (482*(credit-18))
                    elif level == 'sophomore':
                        tuition = 7410 + (494*(credit-18))
                        
            #conditions for non-engineering students
            else: 
                Jamesma = input("Are you in the James Madison College (yes/no): ").lower() #in James Madison College?
                if Jamesma == 'yes':   #Jame Madison College fee
                    fee = fee + 7.5        
                credit1 = input("Credits: ") #ask for credits.
                while credit1.isdigit() == False or credit1 == '0': #while loop for incorrect credits input
                    print("Invalid input. Try again.")
                    credit1 = (input("Credits: "))
                credit = int(credit1) #change the string input into an integer.
                #state news tax condition  
                if credit > 6:
                    State_news_tax = State_news_tax+5
                #credits charge conditions 
                if credit >= 1 and credit <= 11:
                    if level == 'freshman':
                        tuition = 482 * credit
                    elif level == 'sophomore':
                        tuition = 494 * credit
                elif credit >= 12 and credit <= 18:
                    if level == 'freshman':
                        tuition = 7230
                    elif level == 'sophomore':
                        tuition = 7410
                elif credit > 18:
                    if level == 'freshman':
                        tuition = 7230 + (482*(credit-18))
                    elif level == 'sophomore':
                        tuition = 7410 + (494*(credit-18))
                                          
        #Resident Junior Senior Condition
        elif level == 'junior' or 'senior':
            college = input("Enter college as business, engineering, health, sciences, or none: ").lower() #ask for college.
            cmse = input("Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ").lower() #majoring in CMSE?
            #college conditions
            if college == 'business' or college == "engineering" or college == 'health' or college == 'sciences':
                credit1 = input("Credits: ") #ask for credits
                while credit1.isdigit() == False or credit1 == '0':  #while loop for incorrect credits input
                    print("Invalid input. Try again.")
                    credit1 = (input("Credits: "))
                credit = int(credit1) #change the string input into an integer.
                #state news tax condition    
                if credit > 6:
                    State_news_tax = State_news_tax+5
                #CMSE fee conditions    
                if cmse == 'yes':
                    if credit <= 4 and credit > 0: 
                        fee = fee + 402
                    elif credit > 4:
                        fee = fee + 670 
                #college fee conditions        
                if credit <= 4 and credit > 0:
                    if college == 'business':
                        fee = fee + 113
                    elif college == 'health'or college == 'sciences':
                        fee = fee + 50
                elif credit > 4:
                    if college == 'business':
                        fee = fee + 226
                    elif college == 'health'or college == 'sciences':
                        fee = fee + 100
                #engineering fee conditions    
                if college == 'engineering':  #
                    if credit <= 4 and credit > 0: 
                        fee = fee + 402
                    elif credit > 4:
                        fee = fee + 670
                #credits charge conditions   
                if credit >=1 and credit <=11:  
                    if college != 'engineering'and college != 'business':
                        tuition = 555 * credit
                    elif college == 'engineering' or college == 'business':
                        tuition = 573 * credit
                elif credit >=12 and credit <=18:
                    if college != 'engineering'and college != 'business':
                        tuition = 8325
                    elif college == 'engineering' or college == 'business':
                        tuition = 8595
                elif credit > 18:
                    if college != 'engineering'and college != 'business':
                        tuition = 8325 + ((credit-18)*555)
                    elif college == 'engineering' or college == 'business':
                        tuition = 8595 + ((credit-18)*573)          
            #conditions for other colleges besides engineering, business, health, and sciences.
            else:
                Jamesma = input("Are you in the James Madison College (yes/no): ").lower() #in James Madison College?
                if Jamesma == 'yes':  #James Madison fee condition
                    fee = fee + 7.5        
                credit1 = input("Credits: ") #ask for credits
                while credit1.isdigit() == False or credit1 == '0': #while loop for incorrect credits input
                    print("Invalid input. Try again.")
                    credit1 = (input("Credits: "))
                credit = int(credit1) #change the string input into an integer.
                #state news tax condition
                if credit > 6:
                    State_news_tax = State_news_tax+5
                #CMSE fee conditions 
                if credit <= 4 and credit > 0: 
                    fee = fee + 402
                elif credit > 4:
                    fee = fee + 670 
                #engineering fee conditions 
                if college == 'engineering':
                    if credit <= 4 and credit > 0: 
                        fee = fee + 402
                    elif credit > 4:
                        fee = fee + 670
                #credits charge conditions  
                if credit >=1 and credit <=11: 
                    if college != 'engineering'and college != 'business':
                        tuition = 555 * credit
                    elif college == 'engineering' or college == 'business':
                        tuition = 573 * credit
                elif credit >=12 and credit <=18:
                    if college != 'engineering'and college != 'business':
                        tuition = 8325
                    elif college == 'engineering' or college == 'business':
                        tuition = 8595
                elif credit > 18:
                    if college != 'engineering'and college != 'business':
                        tuition = 8325 + ((credit-18)*555)
                    elif college == 'engineering' or college == 'business':
                        tuition = 8595 + ((credit-18)*573)    
                               
    ####### International # & # Non-resident #######                       
    else: 
        inter = input("International (yes/no): ").lower() #Is the student international student?
        level = input("Level—freshman, sophomore, junior, senior: ").lower() #ask for year.
        while level!='freshman'and level!='sophomore'and level!='junior'and level!='senior': #while loop for incorrect year input
            print("Invalid input. Try again.")
            level = input("Level—freshman, sophomore, junior, senior: ").lower()
        #Inter or non-resident Freshman Sophomore conditions
        if level == 'freshman' or level == 'sophomore': 
            Engineer = input("Are you admitted to the College of Engineering (yes/no): ").lower() #admitted to engineering college?
            #Engineering student conditions
            if Engineer == 'yes': 
                credit1 = input("Credits: ") #ask for credits
                while credit1.isdigit() == False or credit1 == '0': #while loop for incorrect credits input
                    print("Invalid input. Try again.")
                    credit1 = (input("Credits: "))
                credit = int(credit1) #change the string input into an integer.
                #engineering fee conditions 
                if credit <= 4 and credit > 0:  
                    fee = fee + 402
                elif credit > 4:
                    fee = fee + 670
                #state news tax condition
                if credit > 6:
                    State_news_tax = State_news_tax+5
                #international fee conditions   
                if inter == 'yes': 
                    if credit <= 4 and credit > 0:  
                        fee = fee + 375
                    elif credit > 4:
                        fee = fee + 750
                #credits charge conditions    
                if credit >= 1 and credit <= 11:   
                    tuition = 1325.50 * credit    
                elif credit >= 12 and credit <= 18:
                    tuition = 19883    
                elif credit > 18:
                    tuition = 19883 + (1325.50*(credit-18))
            #conditions for not in engineering college            
            else: 
                Jamesma = input("Are you in the James Madison College (yes/no): ").lower()
                if Jamesma == 'yes':
                    tution = tuition + 7.5
                credit1 = input("Credits: ") #ask for cedits
                while credit1.isdigit() == False or credit1 == '0':  #while loop for incorrect credits input
                    print("Invalid input. Try again.")
                    credit1 = (input("Credits: "))
                credit = int(credit1) #change the string input into an integer.
                #state news tax condition
                if credit > 6:
                    State_news_tax = State_news_tax+5
                #international fee conditions    
                if inter == 'yes': 
                    if credit <= 4 and credit > 0:  
                        fee = fee + 375
                    elif credit > 4:
                        fee = fee + 750
                #credits charge conditions         
                if credit >= 1 and credit <= 11: 
                    tuition = 1325.50 * credit    
                elif credit >= 12 and credit <= 18:
                    tuition = 19883 * credit   
                elif credit > 18:
                    tuition = 19883 + (1325.50*(credit-18)) 
                        
        #Inter or non-resident Junior Senior Conditions            
        elif level == 'junior' or 'senior':     
            college = input("Enter college as business, engineering, health, sciences, or none: ").lower() #ask for college.
            cmse = input("Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ").lower() #majoring in CMSE?
            #college conditions
            if college == 'business' or college == "engineering" or college == 'health' or college == 'sciences': 
                credit1 = input("Credits: ") #ask for credits
                while credit1.isdigit() == False or credit1 == '0': #while loop for incorrect credits input
                    print("Invalid input. Try again.")
                    credit1 = (input("Credits: "))
                credit = int(credit1) #change the string input into an integer.
                #state news tax condition
                if credit > 6:
                    State_news_tax = State_news_tax + 5
                #CMSE fee conditions 
                if cmse == 'yes':
                    if credit <= 4 and credit > 0:  
                        fee = fee + 402 
                    elif credit > 4:
                        fee = fee + 670
                #college fee conditions               
                if credit <= 4 and credit > 0:   
                    if college == 'business':
                        fee = fee + 113
                    elif college == 'health'or college == 'sciences':
                        fee = fee + 50
                elif credit > 4:
                    if college == 'business':
                        fee = fee + 226
                    elif college == 'health'or college == 'sciences':
                        fee = fee + 100
                #engineering fee conditions     
                if college == 'engineering': 
                    if credit <= 4 and credit > 0:
                        fee = fee + 402
                    elif credit > 4:
                        fee = fee + 670
                #international fee conditions    
                if inter == 'yes': 
                    if credit <= 4 and credit > 0:  
                        fee = fee + 375
                    elif credit > 4:
                        fee = fee + 750
                #credits charge conditions         
                if credit >=1 and credit <=11: 
                    if college != 'engineering'and college != 'business':
                        tuition = 1366.75
                    elif college == 'engineering' or college == 'business':
                        tuition = 1385.75
                elif credit >=12 and credit <=18:
                    if college != 'engineering'and college != 'business':
                        tution = 20501
                    elif college == 'engineering' or college == 'business':
                        tuition = 20786
                elif credit > 18:
                    if college != 'engineering'and college != 'business':
                        tuition = 20501 + ((credit-18)*1366.75)
                    elif college == 'engineering' or college == 'business':
                        tuition = 20786 + ((credit-18)*1385.75)
            #conditions for other colleges besides engineering, business, health, and sciences.
            else:
                Jamesma = input("Are you in the James Madison College (yes/no): ").lower() #in James Madison College?
                if Jamesma == 'yes':  #James Madison fee condition
                    fee = fee + 7.5
                credit1 = input("Credits: ") #ask for credits
                while credit1.isdigit() == False or credit1 == '0': #while loop for incorrect credits input
                    print("Invalid input. Try again.")
                    credit1 = (input("Credits: "))
                credit = int(credit1) #change the string input into an integer. 
                #state news tax condition
                if credit > 6:
                    State_news_tax = State_news_tax + 5
                #CMSE fee condiotions
                if credit <= 4 and credit > 0:  
                    fee = fee + 402 
                elif credit > 4:
                    fee = fee + 670
                #engineering fee conditions
                if college == 'engineering': 
                    if credit <= 4 and credit > 0:
                        fee = fee + 402
                    elif credit > 4:
                        fee = fee + 670
                #international fee conditions
                if inter == 'yes': 
                    if credit <= 4 and credit > 0:  
                        fee = fee + 375
                    elif credit > 4:
                        fee = fee + 750
                #credits charge conditions   
                if credit >=1 and credit <=11: 
                    if college != 'engineering'and college != 'business':
                        tuition = 1366.75
                    elif college == 'engineering' or college == 'business':
                        tuition = 1385.75
                elif credit >=12 and credit <=18:
                    if college != 'engineering'and college != 'business':
                        tution = 20501
                    elif college == 'engineering' or college == 'business':
                        tuition = 20786
                elif credit > 18:
                    if college != 'engineering'and college != 'business':
                        tuition = 20501 + ((credit-18)*1366.75)
                    elif college == 'engineering' or college == 'business':
                        tuition = 20786 + ((credit-18)*1385.75)        
            
    #output                
    tuition_fee = tuition + fee + ASMSU_tax + FM_Radio_tax + State_news_tax  #tuition & fees calculation         
    print("Tuition is $"'{:,.2f}'".".format(tuition_fee))  #display the result
    ask_repeat = input("Do you want to do another calculation (yes/no): ").lower() #ask to repeat the program. 
    if ask_repeat == 'yes':
        continue
    else:
        break
        
       
                



