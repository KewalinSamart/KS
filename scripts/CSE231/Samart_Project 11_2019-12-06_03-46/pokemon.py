#################################################################################################
#  Programming Project #11
#  
#  Class Moves is a Move object composing of name, element, power, accuracy,
#      and attack_type
#
#  Class Pokemon is a Pokemon object composing of name, element1, element2, moves,
#      hp (health), patt (power of attacker), pdef (power of defender), 
#      satt (special strength of attacker),and  sdef (special strength of defender)
#
#################################################################################################

from random import randint


#DO NOT CHANGE THIS!!!
# =============================================================================
is_effective_dictionary = {'bug': {'dark', 'grass', 'psychic'}, 
                           'dark': {'ghost', 'psychic'},
                           'dragon': {'dragon'}, 
                           'electric': {'water', 'flying'}, 
                           'fairy': {'dark', 'dragon', 'fighting'},
                           'fighting': {'dark', 'ice', 'normal', 'rock', 'steel'}, 
                           'fire': {'bug', 'grass', 'ice', 'steel'}, 
                           'flying': {'bug', 'fighting', 'grass'}, 
                           'ghost': {'ghost', 'psychic'}, 
                           'grass': {'water', 'ground', 'rock'}, 
                           'ground': {'electric', 'fire', 'poison', 'rock', 'steel'}, 
                           'ice': {'dragon', 'flying', 'grass', 'ground'}, 
                           'normal': set(), 
                           'poison': {'fairy', 'grass'}, 
                           'psychic': {'fighting', 'poison'}, 
                           'rock': {'bug', 'fire', 'flying', 'ice'},
                           'steel': {'fairy', 'ice', 'rock'},
                           'water': {'fire', 'ground', 'rock'}
                           }

not_effective_dictionary = {'bug': {'fairy', 'flying', 'fighting', 'fire', 'ghost','poison','steel'}, 
                            'dragon': {'steel'}, 
                            'dark': {'dark', 'fairy', 'fighting'},
                            'electric': {'dragon', 'electric', 'grass'},
                            'fairy': {'fire', 'poison', 'steel'},
                            'fighting': {'bug', 'fairy', 'flying', 'poison', 'psychic'}, 
                            'fire': {'dragon', 'fire', 'rock', 'water'}, 
                            'flying': {'electric', 'rock', 'steel'}, 
                            'ghost': {'dark'}, 
                            'grass': {'bug', 'dragon', 'grass', 'fire', 'flying', 'poison', 'steel'}, 
                            'ground': {'bug','grass'}, 
                            'ice': {'fire', 'ice', 'steel', 'water'}, 
                            'normal': {'rock', 'steel'}, 
                            'poison': {'ghost', 'ground', 'poison', 'rock'}, 
                            'psychic': {'psychic', 'steel'}, 
                            'rock': {'fighting', 'ground', 'steel'}, 
                            'steel': {'electric', 'fire', 'steel', 'water'},
                            'water': {'dragon','grass', 'ice'}
                            }

no_effect_dictionary = {'electric': {'ground'}, 
                        'dragon': {'fairy'},
                        'fighting': {'ghost'}, 
                        'ghost': {'normal', 'psychic'}, 
                        'ground': {'flying'}, 
                        'normal': {'ghost'}, 
                        'poison': {'steel'},
                        'psychic': {'dark'}, 
                        
                        'bug': set(), 'dark': set(), 'fairy': set(),'fire': set(), 
                        'flying': set(), 'grass': set(), 'ice': set(), 
                        'rock': set(), 'steel': set(), 'water': set()
                        }

#Dictionaries that determine element advantages and disadvantages
# =============================================================================

class Move(object):
    def __init__(self, name = "", element = "normal", power = 20, accuracy = 80,
                 attack_type = 2):
        """ initializes attributes of the Move object """
        
        self.name = name
        self.element = element
        self.power = power
        
        self.accuracy = accuracy
        self.attack_type = attack_type  #attack_type is 1, 2 or 3 
        # 1 - status moves, 2 - physical attacks, 3 - special attacks
        
    def __str__(self):
            
        '''
            This method displays name of the Move object in string format
            Takes: self
            Returns: a string
        '''        
        return str("{}".format(self.name))

    def __repr__(self):
        '''
            This method takes self and returns self.__str__()
        '''
        return self.__str__()
    
    def get_name(self):
        '''
            This method takes self and returns name of the Move object
        '''
        return self.name
    
    def get_element(self):
        '''
            This method takes self and return element of the Move object
        '''
        return self.element
    
    def get_power(self):
        '''
            This method takes self and returns power of the Move object
        '''
        return self.power
    
    def get_accuracy(self):
        '''
            This method takes self and returns accuracy of the Move object
        '''
        return self.accuracy
    
    def get_attack_type(self):
        '''
            This method takes self and returns attack type of the Move object
        '''
        return self.attack_type

    def __eq__(self,m):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == m.get_name() and self.element == m.get_element() and\
                self.power == m.get_power() and self.accuracy == m.get_accuracy() and\
                self.attack_type == m.get_attack_type()
        
        
class Pokemon(object):
    def __init__(self, name = "", element1 = "normal", element2 = "", moves = None,
                 hp = 100, patt = 10, pdef = 10, satt = 10, sdef = 10):
        ''' initializes attributes of the Pokemon object '''
        
        self.name = name
        self.element1 = element1
        self.element2 = element2
        
        self.hp = hp
        self.patt = patt
        self.pdef = pdef
        self.satt = satt
        self.sdef = sdef
        
        self.moves = moves
        
        try:
            if len(moves) > 4:
                self.moves = moves[:4]
                
        except TypeError: #For Nonetype
            self.moves = list()

    def __eq__(self,p):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == p.name and \
            self.element1 == p.element1 and \
            self.element2 == p.element2 and \
            self.hp == p.hp and \
            self.patt == p.patt and \
            self.pdef == p.pdef and \
            self.satt == p.satt and \
            self.sdef == p.sdef and \
            self.moves == p.moves

    def __str__(self):
        '''
            This method takes self and returns diplaying of name, health, power of attacker, power of defender,
            special power of attacker, special power of defender, element1, element2 of the Pokemon object, and also 
            name of the moves in the list of moves of the Pokemon object
        '''
        line1 = str("{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}\n".format(self.name, self.hp, self.patt, self.pdef, self.satt, self.sdef))
        line2 = str("{:<15}{:<15}\n".format(self.element1, self.element2))
        line3 = ["{:<15s}".format(move.get_name()) for move in self.moves]
        return  line1 + line2 + ''.join(line3)
                

    def __repr__(self):
        '''
            This method takes self and returns power of __str__(self)
        '''
        return self.__str__()


    def get_name(self):
        '''
            This method takes self and returns name of the Pokemon object
        '''
        return self.name
    
    def get_element1(self):
        '''
            This method takes self and returns element1 of the Pokemon object
        '''
        return self.element1
    
    def get_element2(self):
        '''
            This method takes self and returns element2 of the Pokemon object
        '''
        return self.element2
    
    def get_hp(self):
        '''
             This method takes self and returns health of the Pokemon object
        '''
        return self.hp
    
    def get_patt(self):
        '''
             This method takes self and returns power of attacker of the Pokemon object
        '''
        return self.patt

    def get_pdef(self):
        '''
             This method takes self and returns power of defender of the Pokemon object
        '''
        return self.pdef

    def get_satt(self):
        '''
             This method takes self and returns special power of attacker of the Pokemon object
        '''
        return self.satt

    def get_sdef(self):
        '''
             This method takes self and returns special power of defender of the Pokemon object
        '''
        return self.sdef
    
    def get_moves(self):
        '''
             This method takes self and returns moves of the Pokemon object
        '''
        return self.moves

    def get_number_moves(self):
        '''
             This method takes self and returns number of moves of the Pokemon object
        '''
        return len(self.moves)

    def choose(self,index):
        '''
             This method takes self and index (an integer). If the index causes index error,
             then return None. If not, returns the move that correspond to the index.
        '''
        try:
            self.moves[index]
            return self.moves[index]
        
        except IndexError:
            return None
            
        
    def show_move_elements(self):
        '''
            This method takes self and returns elements of the move in string format.
        '''
        for moves in Pokemon.get_moves(self):
            move_ele = Move.get_element(self)
            print("{:<15}".format(move_ele), end = " ")


    def show_move_power(self):
        '''
            This method takes self and returns power of the moves in string format
        '''
        for moves in Pokemon.get_moves(self):
            print("{:<15}".format(Move.get_power(self)), end = " ")

    def show_move_accuracy(self):
        '''
            This method takes self and returns accuracy of the move in string format
        '''
        for moves in Pokemon.get_moves(self):
            print("{:<15}".format(Move.get_accuracy(self)), end = " ")
        
        
    def add_move(self, move):
        '''
            This method adds move to the list of moves until there are 4 moves total in the list.
            It takes self and move (Move object).
        '''
        number_moves = Pokemon.get_number_moves(self)
        if number_moves <= 3:
            Pokemon.get_moves(self).append(move)
             
        
    def attack(self, move, opponent):
        '''
            This method takes self, move (Move object), and opponent (Pokemon object).
            It creates variables to calculate damage before and after being attacked by
            an attacker of an opponent. It returns None or nothing depending on the following 
            conditions inside the method.
        '''
        mp = move.get_power()
        
        attack_type_op = move.get_attack_type()
        
        if attack_type_op == 2:
            A = Pokemon.get_patt(self)
            D = Pokemon.get_pdef(opponent)
        elif attack_type_op == 3:
            A = Pokemon.get_satt(self)
            D = Pokemon.get_sdef(opponent)
        else:
            print("Invalid attack_type, turn skipped.")
            return None
            
        accuracy_random = randint(1,100)
        accuracy_self = move.get_accuracy()
        
        # condition for the calculation of modifier
        modifier = 1.0
        if opponent.get_element1() in is_effective_dictionary[move.get_element()]:
            modifier = modifier * 2
        if opponent.get_element1() in not_effective_dictionary[move.get_element()]:
            modifier = modifier / 2
        if opponent.get_element1() in no_effect_dictionary[move.get_element()]:
            modifier = modifier * 0
            
        if opponent.get_element2() in is_effective_dictionary[move.get_element()]:
            modifier = modifier * 2
        if opponent.get_element2() in not_effective_dictionary[move.get_element()]:
            modifier = modifier / 2
        if opponent.get_element2() in no_effect_dictionary[move.get_element()]:
            modifier = modifier * 0
        
        if move.get_element() == self.get_element1() or move.get_element() == self.get_element2():
            modifier = modifier * 1.5
        
        if accuracy_random > accuracy_self:
            print("Move missed!")
            modifier = modifier * 0
            return None
        
        if modifier > 1.5:
            print("It's super effective!!!!")
        elif 0 < modifier < 1:
            print("Not very effective...")
        elif modifier == 0:
            print("No effect!")
        
        
        damage = (((mp * (A/D) *20) / 50) + 2) * modifier
        damage = int(damage)
      
        opponent.subtract_hp(damage) 
        
        
    def subtract_hp(self,damage):
        '''
            This method takes self and damage (an integer) and subtracts damage from
            health (hp). The value after subtraction would be zero if the result turns out to be 
            less than or equal to 0.
        '''
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
        

