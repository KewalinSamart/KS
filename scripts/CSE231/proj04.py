##################################################################################
#Programming Project #4
#
#Algorithm
#    display options
#    while loop to replay the program
#        prompt for a string (an alphabet)
#        input a string (an alphabet)
#            display an error statement if the input is not one of the options
#            display closing message and exit the loop if the input is 'x'
#        call a function corresponding to the output
#            prompt for an input (type depends on the function)
#            display an error statement if the input is not in the correct type
#            do calculation through the function
#        display the result        
##################################################################################

import math  #import math function 
EPSILON = 1.0e-7  #Epsilon constant 

def display_options():
    '''
    This function displays the menu of options
    '''
    
    MENU = '''Please choose one of the options below:
             A. Display the value of the sum of the first N natural numbers. 
             B. Display the approximate value of e.
             C. Display the approximate value of the hyperbolic sine of X.
             D. Display the approximate value of the hyperbolic cosine of X.
             M. Display the menu of options.
             X. Exit from the program.'''
    print("\n"+MENU)


def sum_natural(N):
    ''' 
        This function calculates the sum of the first N natural numbers. 
        N: The N to be processed (int greater than zero)
        Returns: the sum of the first N natural numbers (int)  
    '''
    try: 
        N = int(N)    #test if the input N can be converted to integer
        if N != 0:    #continue the condition if N is not zero
            n = N + 1 
            sum_n = 0
            for i in range(n):
                sum_n += i
            return sum_n  #returns sum of the first natural number N
        else:
            return None  #returns None if N is zero  
    except:
        return None #returns None if N can't be converted to int
   

def approximate_euler():
    ''' 
        This function approximates the Euler number (The irrational number e 
        that is the base of the natural logarithm). 
        No parameters
        Returns: The estimated value of the Euler number (float)  
    '''
    e = 0  #initial value of e is zero
    n = 0  #initial value of n is zero
    term = 1 #initial value of term is zero
    while abs(term) > EPSILON: #continue the loop until absolute value of term/
                               #less than Epsilon constant
        e += term
        n += 1
        term = 1/(math.factorial(n)) #formula of the Euler no. approximation
    return round(e,10)  #return the estimated value of the Euler number


def approximate_sinh(x):
    ''' 
        This function approximates sinh(x). 
        x: The x to be processed (string)
        Returns: The estimated value of sinh(x) (float)  
    '''
    
    sinh = 0  #initial value of sinh is zero
    n = 0     #initial value of n is zero
    try:
        term = float(x)  #initial value of term is x in float
        x = float(x)     #test if the input x can be converted to float
        while abs(term) > EPSILON: #continue the loop until absolute value of term/
                                   #less than Epsilon constant
            sinh += term
            n += 1
            term = (x**(2*n+1))/(math.factorial(2*n+1)) #fomular of sinh approximation
        return round(sinh,10)  #returns the estimated value of sinh(x) rounded to 10 decimal places
    except:
        return None #returns None if x can't be converted to float      
    
def approximate_cosh(x):
    ''' 
        This function approximates cosh(x) 
        x: The x to be processed (string)
        Returns: The estimated value of cosh(x) (float)  
    '''
    cosh = 0 #initial value of cosh is zero
    n = 0    #initial value of n is zero
    term = 1 #initial value of term is one
    try:
        x = float(x)  #test if the input x can be converted to float
        while abs(term) > EPSILON: #continue the loop until absolute value of term/
                                   #less than Epsilon constant
            cosh += term
            n += 1
            term = (x**(2*n))/(math.factorial(2*n)) #formula of cosh approximation
        return round(cosh,10) #returns the estimated value of cosh(x) rounded to 10 decimal places
    except:
        return None #returns None if x can't be converted to float
         

def main():
    ''' 
        This function is the main function that is executed automatically
        while the program is running.
        no parameters
        Returns: the result depends on the loop and conditions within 
        the function.  
    '''

    display_options()  #call the display options function
    input_option = input("\n\tEnter option: ") #input an alphabet in string for picking an option
   
    while input_option.lower() != 'x': #exist the loop if the input is 'x'
        
        #conditions for option a
        if input_option.lower() == 'a': 
            N = input("\nEnter N: ")    #input a natural number
            if N.isdigit() == False or N == '0': #if the input is not an integer greater than zero
                print("\n\tError: N was not a valid natural number. [{}]".format(N)) #display an error message
                pass
            else:        #if the input is an integer greater than zero
                print("\n\tThe sum: {} ".format(sum_natural(N))) #display the sum of the first natural no. N 
            input_option = input("\n\tEnter option: ") #ask user to pick an option again
        
        #conditions for option b
        elif input_option.lower() == 'b': 
            print("\n\tApproximation: {:.10f}".format(approximate_euler())) #display the estimated value of Euler no.
            print("\tMath module:   {:.10f}".format(math.e)) #display the actual value of Euler no.
            mathe = round(math.e,10) #round the actual e to 10 decimal places 
            euler = round(approximate_euler(),10) #round the estimated e to 10 decimal places
            diffe = abs(euler - mathe) #absolute difference between the estimated e and the actual e
            print("\tdifference:    {:.10f}".format(diffe)) #display the absolute difference 
            input_option = input("\n\tEnter option: ") #ask user to pick an option again
        
        #conditions for option c
        elif input_option.lower() == 'c': 
            x = input("\n\tEnter X: ")  #input a string x
            try:
                x = float(x) #check if x can be converted to float
                print("\n\tApproximation: {:.10f}".format(approximate_sinh(x))) #display the estimated value of sinh(x).
                print("\tMath module:   {:.10f}".format(math.sinh(x))) #display the actual value of sinh(x).
                mathsinh = round(math.sinh(x),10) #round the actual sinh(x) to 10 decimal places
                sinh = round(approximate_sinh(x),10) #round the estimated sinh(x) to 10 decimal places
                diffe = mathsinh - sinh #absolute difference between the estimated sinh() and the actual sinh(x)
                print("\tdifference:    {:.10f}".format(abs(diffe))) #display the absolute difference
            except:
                print("\n\tError: X was not a valid float. [{}]".format(x)) #display an erroe message if x can't be 
                                                                            #converted to float
            finally:    
                input_option = input("\n\tEnter option: ") #ask user to pick an option again
            
        #conditions for option d
        elif input_option.lower() == 'd': 
            x = input("\n\tEnter X: ") #input a string x
            try:
                x = float(x) #check if x can be converted to float
                print("\n\tApproximation: {:.10f}".format(approximate_cosh(x))) #display the estimated value of cosh(x).
                print("\tMath module:   {:.10f}".format(math.cosh(x))) #display the actual value of cosh(x).
                mathcosh = round(math.cosh(x),10) #round the actual cosh(x) to 10 decimal places
                cosh = round(approximate_cosh(x),10) #round the estimated cosh(x) to 10 decimal places
                diffe = mathcosh - cosh #absolute difference between the estimated cosh() and the actual cosh(x)
                print("\tdifference:    {:.10f}".format(abs(diffe))) #display the absolute difference
            except:
                print("\n\tError: X was not a valid float. [{}]".format(x)) #display an erroe message if x can't be 
                                                                            #converted to float
            finally: 
                input_option = input("\n\tEnter option: ") #ask user to pick an option again
            
        #conditions for option m
        elif input_option.lower() == 'm':
            display_options() #display the options
            input_option = input("\n\tEnter option: ") #ask user to pick an option
        else:
            print("\nError:  unrecognized option [{}]".format(input_option.upper())) #display an error message if 
                                                                                     #the input option is incorrect
            pass
            display_options()   #display the options again
            input_option = input("\n\tEnter option: ") #ask user to pick an option again
            
        
        if input_option.lower() == 'x':  #the input is 'x' then end the program
            print("Hope to see you again.")  #display closing message
 
# this was added to make functions to be tested individually on mirmir        
if __name__ == "__main__": 
    main()    
        
        
            
            
    
