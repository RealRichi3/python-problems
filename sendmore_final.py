"""
SEND + MORE == MONEY

Assigns different values from range 0-9 to each variable in sendmory
And checks if the equation is satisfied

CODE
Assign random number to each letter
Check if the combination has been used before
Input parameters to equation

dict with letters
randomly add dict key - check first if it exists
check equation.
"""
import random



def create_dict():
    """
        Add intial letters as keys to the Dictionary    
    """
    global num_dict
    num_dict = {}
    
    for letters in 'sendmory':                                  
        num_dict[letters] = None

def rand_add(dict_x):
    """
        Set unique random numbers as values to the letters(keys in the dict) 
    """

    for letters in dict_x.keys():
        num = random.randint(0,9)                               # Assign random number to num
        while True:
            if num not in dict_x.values():                      # Check if number is already assiged to a key in the dictionay
                dict_x[letters] = num
                break
            else:
                num = random.randint(0,9)                       # If number is  already assigned, choose a new random number
    return dict_x

def check_equation(dict_y):
    # for i

