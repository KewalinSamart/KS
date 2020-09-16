#############################################################################################
#    Programming Project #10
#
#    Algorithm
#        display options
#        display stock, tableau, and foundation
#        prompt for a string (an option)
#        loop while the input is incorrect
#            reprompt for a string (a valid option)
#        display the output coresponding to the input for a choice
#        keep asking for a choice until the player wins the game.
#        exit the game if the input for option is 'Q' or 'q' 
############################################################################################ 


import cards  #import the Class Cards

RULES = '''
Aces High Card Game:
     Tableau columns are numbered 1,2,3,4.
     Only the card at the bottom of a Tableau column can be moved.
     A card can be moved to the Foundation only if a higher ranked card 
        of the same suit is at the bottom of another Tableau column.
     To win, all cards except aces must be in the Foundation.'''

MENU = '''     
Input options:
    D: Deal to the Tableau (one card on each column).
    F x: Move card from Tableau column x to the Foundation.
    T x y: Move card from Tableau column x to empty Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''

def init_game():
    
    '''
    This function creates and initialize stock, tableau, and foundation
    No parameters
    Returns: tuple of stock (a deck class object), tableau (a list of lists, each containing 
    one of the dealt cards.), and foundation (an empty list)
    '''
    stock = cards.Deck()
    foundation = []
    tableau = [[],[],[],[]]
    for i in range(4):
        tableau[i].append(stock.deal())
    return (stock,tableau,foundation)  # stub so that the skeleton compiles; delete 
                               # and replace it with your code
    
def deal_to_tableau( stock, tableau ):
        
    '''
    This function will deal a class from the stock to each column of the tableau.
    It will always deal four cards to fill out every column in the tableau.
    stock: a deck class object
    tableau: a list of lists, each containing one of the dealt cards.
    '''
    for i in range(4):
        tableau[i].append(stock.deal())

def display( stock, tableau, foundation ):
    '''Display the stock, tableau, and foundation.'''
    
    print("\n{:<8s}{:^13s}{:s}".format( "stock", "tableau", "  foundation"))
    
    # determine the number of rows to be printed -- determined by the most
    #           cards in any tableau column
    max_rows = 0
    for col in tableau:
        if len(col) > max_rows:
            max_rows = len(col)

    for i in range(max_rows):
        # display stock (only in first row)
        if i == 0:
            display_char = "" if stock.is_empty() else "XX"
            print("{:<8s}".format(display_char),end='')
        else:
            print("{:<8s}".format(""),end='')

        # display tableau
        for col in tableau:
            if len(col) <= i:
                print("{:4s}".format(''), end='')
            else:
                print("{:4s}".format( str(col[i]) ), end='' )

        # display foundation (only in first row)
        if i == 0:
            if len(foundation) != 0:
                print("    {}".format(foundation[-1]), end='')

        print()

def get_option():
    
    '''
    This function prompt for an option and return a list containing the option.
    No parameters
    Returns: a list containing the option or None if the option is invalid
    '''
    option = input("\nInput an option (DFTRHQ): ")
    option_list = list(option)
    
    for element in option_list:
        if element == ' ':
            option_list.remove(element)
            
    if len(option_list) == 1:
        if option_list[0].upper() == 'D':
            return ['D']
        elif option_list[0].upper() == 'R':
            return ['R']
        elif option_list[0].upper() == 'H':
            return ['H']
        elif option_list[0].upper() == 'Q':
            return ['Q']
        else:
            print("Error in option: {}".format(option))
            print("Invalid option")
            return None
            
    elif len(option_list) == 2:
        if option_list[0].upper() == 'F':
            try:
                x = int(option_list[1])
                if x in range(1,5):
                    return ['F', x]
                else: 
                    print("Error in option: {}".format(option))
                    print("Invalid option.")
                    return None
            except ValueError:
                print("Error in option: {}".format(option))
                print("Invalid option.")
                return None
        else:
            print("Error in option: {}".format(option))
            print("Invalid option.")
            return None
            
            
    elif len(option_list) == 3:
        if option_list[0].upper() == 'T':
            try:
        
                x = int(option_list[1]) 
                y = int(option_list[2])

                if x in range(1,5) and y in range(1,5):
                    if x != y:
                        return ['T', x, y]
                    else:
                        print("Error in option: {}".format(option))
                        print("Invalid option")
                        return None
                else:
                    print("Error in option: {}".format(option))
                    print("Invalid option")
                    return None
                                         
            except ValueError:
                print("Error in option: {}".format(option))
                print("Invalid option")
                return None
        else:
            print("Error in option: {}".format(option))
            print("Invalid option")
            return None
        
    elif len(option_list) > 3:  #length not 1 or 2 or 3
        print("Error in option: {}".format(option))
        print("Invalid option")
        return None
            
def validate_move_to_foundation( tableau, from_col ):
    
    '''
    This function validates a move to foundation.
    tableau: a list of lists, each containing one of the dealt cards.
    from_col: a number of the column that the user want to move the top card on it 
    to foundation.
    Returns: a boolean
    '''
            
    if from_col in range(1,5) and tableau[from_col-1] != []:
        
        card_col = tableau[from_col-1][-1]
        if card_col.rank() == 1:
            card_col_value = 14
        else:
            card_col_value = card_col.value()
            
        list_suit = []
        for i in range(4):
            if tableau[i] != []:
                card = tableau[i][-1]
                if card_col.suit() == card.suit():
                    if card_col != card:
                        list_suit.append(card)
                
        if list_suit == []:
            return False
        
        less_count = 0
        for card in list_suit: 
            if card.rank() == 1:
                card_value = 14
            else:
                card_value = card.value()
                
            if card_col_value > card_value:
                less_count += 1
            
            elif card_col_value < card_value:
                return True
           
        if less_count == len(list_suit):
            return False
        else:
            return True
            
    else:
        print("Invalid index.")
        return False
    
    if tableau[from_col-1] == []:
        print("Error, empty column: {}".format(from_col))
        return False
     
    
def move_to_foundation( tableau, foundation, from_col ):
    
    '''
    This function moves a top card on the from_col column within tableau to foundation. 
    tableau: a list of lists, each containing one of the dealt cards.
    foundation: an empty list 
    from_col: an int in range 1-4 indicating a column in the taleau    
    '''
    if validate_move_to_foundation( tableau, from_col ):
        moved_card = tableau[from_col-1].pop(-1)
        foundation.append(moved_card)
    else:
        print("Error, cannot move {}.".format(tableau[from_col-1][-1]))
   
    

def validate_move_within_tableau( tableau, from_col, to_col ):
    
    '''
    This function validates a move of a card within the tableau.
    tableau: a list of lists, each containing one of the dealt cards.
    from_card: an int in range 1-4 indicating a column in the taleau   
    to_col: an int in range 1-4 indicating a column in the taleau 
    Returns: a boolean
    '''
    if from_col in range(1,5) and to_col in range(1,5):
        if tableau[from_col-1] != [] and tableau[to_col-1] == []:
            return True
        else:
            
            return False
            
    else:
        
        return False  # stub; delete and replace it with your code

def move_within_tableau( tableau, from_col, to_col ):
    
    '''
    This function makes a move of a card within the tableau.
    tableau: a list of lists, each containing one of the dealt cards.
    from_card: an int in range 1-4 indicating a column in the taleau   
    to_col: an int in range 1-4 indicating a column in the taleau 
    '''
    if validate_move_within_tableau( tableau, from_col, to_col ):
        moved_card = tableau[from_col-1].pop(-1)
        tableau[to_col-1].append(moved_card)
    else:
        print("Invalid move")

    

def check_for_win( stock, tableau ):
    
    '''
    This function checks for win. The only way to win this game is to 
    have an empty stock with only aces left in the tableau.
    stock: a deck class object.
    tableau: a list of lists, each containing one of the dealt cards.
    Return: a boolean
    '''
    
    if stock.is_empty():
        not_ace = 0
        for i in range(4):
            
            for card in tableau[i]:
                if card.rank() != 1:
                    not_ace += 1
                    
        if not_ace > 0:
            return False
        if not_ace == 0:
            return True
    else:
        return False
        
def main():
        
    '''
    This function control the move of the game using all the functions above. 
    No parameters
    No returns
    '''
    
    stock, tableau, foundation = init_game() #get stock, tableau, and foundation from the init_game() function.
    print( MENU )     #display the MENU
    
    display( stock, tableau, foundation )  #display the initial stock, tableau, and foundation.
    
    while True:   #While loop to continue asking for an option after every move has been made.
        
        option = get_option() 
        
        if option == None:  #if the option is None, then display the previous result
            display( stock, tableau, foundation )
            continue
        elif option[0] == 'D':  #deal more cards
            deal_to_tableau( stock, tableau )
        elif option[0] == 'F':  #move a caed to foundation
            from_col = option[1]
            validate_move_to_foundation( tableau, from_col )
            move_to_foundation( tableau, foundation, from_col )
        elif option[0] == 'T': #move a card within the tableau
            from_col = option[1]
            to_col = option[2]
            validate_move_within_tableau( tableau, from_col, to_col )
            move_within_tableau( tableau, from_col, to_col )
        elif option[0] == 'R': #restart the game
            print("=========== Restarting: new game ============")
            print(RULES)
            print( MENU )
            stock, tableau, foundation = init_game()   
        elif option[0] == 'H': #display the MENU
            print( MENU )
        elif option[0] == 'Q': #exit the game
            print("You have chosen to quit.")
            break
        else:
            continue 
        if check_for_win( stock, tableau ): #check for win
            print("You won!")
            break   #exit the game if the user won the game
          
        display( stock, tableau, foundation ) #display the game panel
        
        
        
# this was added to make functions to be tested individually on mirmir 
if __name__ == "__main__":
    main()