######################################################################################
#  Programming Project #11
#
#  Algorithm
#    prompt for a string (asking whether to continue or not)
#        enter while loop to reprompt for a string if the input is invalid
#    Player1's turn: prompt for a string (a pokemon's name) or an integer 
#    (a valid number for indexing a pokemon's name) 
#        enter while loop to reprompt for a name or a number if the input is invalid
#    display the player1's pokemon information
#    Player2's turn: prompt for strings (a pokemon's name) or an integer 
#        (a valid number for indexing a pokemon's name) 
#        enter while loop to reprompt for a name or a number if the input is invalid
#    display the player2's pokemon information
#    Player1's move: prompt for an integer or a string 
#        (selecting a move (1-4) or pick to quit ('q') )
#    display Player1's attacking effects on Player2's health
#    Player2's move: prompt for an integer or a string 
#        (selecting a move (1-4) or pick to quit ('q') )
#    display Player2's attacking effects on Player1's health
#    continue switching turns between Player1 and 2 until one of them win the game
#    display the result of the game
#    prompt for a string (asking whether to continue or not)
#        enter while loop to reprompt for a string if the input is invalid
######################################################################################


import csv
from random import randint
from random import seed
from copy import deepcopy

from pokemon import Pokemon #import Pokemon class from pokemon.py
from pokemon import Move    #import Move class from pokemon.py

seed(1) #Set the seed so that the same events always happen


#DO NOT CHANGE THIS!!!
# =============================================================================
element_id_list = [None, "normal", "fighting", "flying", "poison", "ground", "rock", 
                   "bug", "ghost", "steel", "fire", "water", "grass", "electric", 
                   "psychic", "ice", "dragon", "dark", "fairy"]

#Element list to work specifically with the moves.csv file.
#   The element column from the moves.csv files gives the elements as integers.
#   This list returns the actual element when given an index
# =============================================================================
    
def read_file_moves(fp):  
    '''
    This function reads through moves.csv file to get Move objects and append to 
    a list of move.
    fp: a file pointer of moves.csv file
    Returns: a list containing Move objects
    '''
    reader = csv.reader(fp)
    next(reader,None)
    moves_list = []
    
    for line in reader:
        name = line[1]
        type_id = int(line[3])
        try:
            element = element_id_list[type_id]
        except IndexError:
            continue
        
        attack_type = line[9]
        
        if attack_type != '1':
            attack_type = int(attack_type)
        else:
            continue
        
        gen_id = line[2]
        if gen_id == '1':
            gen_id = int(gen_id)
        else:
            continue
        power = line[4]
        if power != "":
            power = int(power)
        else:
            continue
        accuracy = line[6]
        if accuracy != "":
            accuracy = int(accuracy)
        else:
            continue
            
        move = Move(name, element, power, accuracy, attack_type)
        moves_list.append(move)
    
    return moves_list
        

def read_file_pokemon(fp):
    '''
    This function reads through pokemon.csv file to get Pokemon objects and append to 
    a list of move.
    fp: a file pointer of pokemon.csv file
    Returns: a list containing Pokemon objects
    '''
    reader = csv.reader(fp)
    next(reader,None)
    ID_list = list()
    pokemon_list = list()
    
    for line in reader:
        gen = line[11]
        if gen != '1':
            continue
        ID = line[0]
        if ID not in ID_list:
            ID_list.append(ID)
        else:
            continue
        element1 = line[2].lower()
        element2 = line[3].lower()
        name = line[1].lower()
        hp = int(line[5])
        patt = int(line[6])
        pdef = int(line[7])
        satt = int(line[8])
        sdef = int(line[9])
        
        pokemon = Pokemon(name, element1, element2, None, hp, patt, pdef, satt, sdef)
        pokemon_list.append(pokemon)
    
    return pokemon_list
        
        
def choose_pokemon(choice,pokemon_list):
    '''
    This function takes a choice to pick a pokemon from the list containing Pokemon objects
    choice: an integer (for indexing a pokemon) or a string (a pokemon's name)
    pokemon_list: a list containing Pokemon objects (returning value of read_file_pokemon(fp) function)
    Returns: a deepcopy of the chosen pokemon object or None
    '''
    try:
        choice = int(choice)
        
        if  1 <= choice < len(pokemon_list):
            return deepcopy(pokemon_list[choice-1])
        else:
            return None
    
    except ValueError:
        choice = choice.lower()
        name_list = []
        
        for pokemon in pokemon_list:
            name = pokemon.get_name()
            name_list.append(name)
            
        if choice in name_list:
            index = name_list.index(choice)
            return deepcopy(pokemon_list[index])
        else:
            return None
                
                
def add_moves(pokemon,moves_list):
    '''
    This function adds moves to the chosen pokemon object to 4 moves in total by 
    randomly selected for the first one and the other three by randomly selected with
    checking validity of moves. 
    pokemon: a Pokemon object
    moves_list: the returning list of read_file_moves(fp) function
    Returns: a boolean
    '''
    
    #first move addition
    random_index1 = randint(0,len(moves_list)-1)
    
    move = moves_list[random_index1]
    pokemon.add_move(move)
    
    # second third and fourth move addition
    attempt_count = 0
    while len(pokemon.get_moves()) < 4:
        attempt_count += 1
        if attempt_count > 200:
            return False
        
        random_index234 = randint(0,len(moves_list)-1)
        
        move = moves_list[random_index234]
        move_ele = move.get_element()
        
        if move_ele == pokemon.get_element1() or move_ele == pokemon.get_element2():
            if move not in pokemon.get_moves():
                pokemon.add_move(move)
    
    if len(pokemon.get_moves()) == 4:
        return True
    
   
def turn(player_num, player_pokemon, opponent_pokemon):
    '''
    This function controls turns of two players. It displays info and control the flow 
    of the game.
    player_num: an integer (either 1 or 2)
    player_pogemon: a Pokemon object (player aka attacker)
    opponent_pokemon: a Pokemon object (opponent)
    Returns: a booleans 
    '''
    print("Player {}'s turn".format(player_num))
    
    #define player's and opponent's number
    if player_num == 1:
        opponent_num = 2
    elif player_num == 2:
        opponent_num = 1
        
    
    print("{} {} {} {} {} {}".format(player_pokemon.get_name(), player_pokemon.get_hp(), \
             player_pokemon.get_patt(), player_pokemon.get_pdef(), player_pokemon.get_satt(), \
             player_pokemon.get_sdef() ))
        
    #print element 1 & 2 of the pokemon1
    if player_pokemon.get_element2() != "":
        print("{} {}".format(player_pokemon.get_element1(), player_pokemon.get_element2()))
    else:
        print("{}".format(player_pokemon.get_element1()))
    
    #create moves_list (a list containing names of all the moves)    
    moves_list = []
    for move in player_pokemon.get_moves():
        moves_list.append(move)
    
    #print moves in moves_list
    identifiers = ["{:15}".format(move.get_name()) for move in moves_list]
    print(''.join(identifiers))
    
    
    
    while True:
        print("Show options: 'show ele', 'show pow', 'show acc'")
        choice_input = input("Select an attack between 1 and 4 or show option or 'q': ")
    
        list_of_moves = player_pokemon.get_moves()
        
        if choice_input == 'q':
            print("Player {} quits, Player {} has won the pokemon battle!".format(player_num, opponent_num ))
            return False
        
        if choice_input == 'show ele':
            for moves in list_of_moves:
                print(moves.get_element(), end = " ")
            
        elif choice_input == 'show pow':
            for moves in list_of_moves:
                print(moves.get_power(), end = " ")
            
        elif choice_input == 'show acc':
            for moves in list_of_moves:
                print(moves.get_accuracy(), end = " ")
    
        elif int(choice_input) in range(1,5):
        
            move = player_pokemon.get_moves()[int(choice_input)-1]
            print("selected move: {}".format(move.get_name()))
            #print oponent's health
            print("{} hp before:{}".format(opponent_pokemon.get_name(), opponent_pokemon.get_hp() ))
        
            #attack
            player_pokemon.attack(move, opponent_pokemon)
            
            #hp after the attack
            print("{} hp after:{}".format(opponent_pokemon.get_name(), opponent_pokemon.get_hp()))
            
            break
        
        #evaluate the result
    
    if opponent_pokemon.get_hp() <= 0:
        print("Player {}'s pokemon fainted, Player {} has won the pokemon battle!".format(opponent_num, player_num ))
        return False
    else:
        
        return True
        
    


def main():
    ''' 
        This function is the main function that is executed automatically
        while the program is running.
        no parameters
        Returns: the result depends on the loop and conditions within 
        the function.  
    '''
    
    usr_inp = input("Would you like to have a pokemon battle? ").lower()
    
    while True:
        while usr_inp != 'n' and usr_inp != 'q' and usr_inp != 'y':
            usr_inp = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q: ").lower()
        
        if usr_inp != 'y':
            print("Well that's a shame, goodbye")
            break
    
        else:
        #player1
            fp = open("moves.csv", "r")
            moves_list = read_file_moves(fp)
        
            fp = open("pokemon.csv", "r")
            pokemon_list = read_file_pokemon(fp)
        
            while True:
                pokemon1 = input("Player 1, choose a pokemon by name or index: ")
            
                chosen_pokemon1 = choose_pokemon(pokemon1, pokemon_list)
            
            
                if isinstance(chosen_pokemon1,Pokemon):
            
                #check valid 4 moves by add_moves() func.
                    if add_moves(chosen_pokemon1, moves_list) == False: #number of moves less than 4
                        print("Insufficient moves; choose a different pokemon.")
                        continue
                    else:
                        break
            
        
        #display on screen  #player1 info               
            print("pokemon1:")
            print("{} {} {} {} {} {}".format(chosen_pokemon1.get_name(), chosen_pokemon1.get_hp(), \
              chosen_pokemon1.get_patt(), chosen_pokemon1.get_pdef(), chosen_pokemon1.get_satt(), \
              chosen_pokemon1.get_sdef() ))
        
        #print element 1 & 2 of the pokemon1
            if chosen_pokemon1.get_element2() != "":
                print("{} {}".format(chosen_pokemon1.get_element1(), chosen_pokemon1.get_element2()))
            else:
                print("{}".format(chosen_pokemon1.get_element1()))
            
    ######################################################################################################
    
        #player2
            fp = open("moves.csv", "r")
            moves_list = read_file_moves(fp)
        #print(moves_list)
            fp = open("pokemon.csv", "r")
            pokemon_list = read_file_pokemon(fp)
        
            while True:
                pokemon2 = input("Player 2, choose a pokemon by name or index: ")
            
                chosen_pokemon2 = choose_pokemon(pokemon2, pokemon_list)
            
            
                if isinstance(chosen_pokemon2,Pokemon):
            
                #check valid 4 moves by add_moves() func.
                    if add_moves(chosen_pokemon2, moves_list) == False: #number of moves less than 4
                        print("Insufficient moves; choose a different pokemon.")
                        continue
                    else:
                        break
            
        
        #display on screen  #player2 info               
            print("pokemon2:")
            print("{} {} {} {} {} {}".format(chosen_pokemon2.get_name(), chosen_pokemon2.get_hp(), \
              chosen_pokemon2.get_patt(), chosen_pokemon2.get_pdef(), chosen_pokemon2.get_satt(), \
              chosen_pokemon2.get_sdef() ))
        
        #print element 2 & 2 of the pokemon2
            if chosen_pokemon2.get_element2() != "":
                print("{} {}".format(chosen_pokemon2.get_element1(), chosen_pokemon2.get_element2()))
            else:
                print("{}".format(chosen_pokemon2.get_element1()))
       
    ######################################################################################################    
        
        #turn
            turn1 = turn(1, chosen_pokemon1, chosen_pokemon2)
            
            if turn1 == True:
                turn2 = turn(2, chosen_pokemon2, chosen_pokemon1)

            while turn1 == True and turn2 == True:
                print("Player 1 hp after: {}".format(chosen_pokemon1.get_hp() ))
                print("Player 2 hp after: {}".format(chosen_pokemon2.get_hp() ))
                turn1 = turn(1, chosen_pokemon1, chosen_pokemon2)
                if turn1 == True:
                    turn(2, chosen_pokemon2, chosen_pokemon1)
                
            usr_inp = input("Battle over, would you like to have another? ").lower()
            if usr_inp == 'n':
                print("Well that's a shame, goodbye")
                break
            elif usr_inp == 'y':
                continue
            
        
# this was added to make functions to be tested individually on mirmir         
if __name__ == "__main__":
    main()