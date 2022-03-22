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
import time

def create_dict():
    """
        Add intial letters as keys to the Dictionary    
    """
    global num_dict
    num_dict = {}
    
    for letters in 'sendmory':                                  
        num_dict[letters] = None

    return num_dict
   
def rand_add(dict_x):
    """
        Set unique random numbers as values to the letters(keys in the dict) 
    """
    while True:
        for letters in dict_x.keys():
            num = random.randint(0,9)                               # Assign random number to num
            while True:
                if num not in dict_x.values():                      # Check if number is already assiged to a key in the dictionay
                    dict_x[letters] = num
                    break
                else:
                    num = random.randint(0,9)                       # If number is  already assigned, choose a new random number
        if list(dict_x.values()) not in tested_values:              # Check if this combination of numbers has been used 
            break
        else:
            dict_x = create_dict()

    return dict_x

def check_equation(dict_y):
    """
        Function to test check if the parameters satisfy the equation
    """
    global tested_values
    global true_or_false
    
    valueList = list(dict_y.values())
    
    s = int(valueList[0])               # Convert string of all the numbers in ValueList to int
    e = int(valueList[1])               # and assign them to the different varialbes
    n = int(valueList[2])
    d = int(valueList[3])
    m = int(valueList[4])
    o = int(valueList[5])
    r = int(valueList[6])
    y = int(valueList[7])

    send = int(str("{}{}{}{}".format(s,e,n,d)))
    more = int(str("{}{}{}{}".format(m,o,r,e)))
    money = int(str("{}{}{}{}{}".format(m,o,n,e,y)))

    if send + more == money:
        print("{} + {} = {}".format(send, more, money))
        true_or_false = False
    else:
        tested_values.append(list(dict_y.values()))     # Adds the combination of values to the list of tested values



tested_values = []
true_or_false = True

start_time = time.time()

while true_or_false == True:
    num_dict = create_dict()
    num_dict = rand_add(num_dict)
    check_equation(num_dict)
   
   
print(num_dict)
print(">>>>>>>>>>>>>>>>>>>>>>>>> Time spent: {} ".format(time.time() - start_time))
