"""
 SEND
 MORE +
------
MONEY
------

"""

from distutils.command.build_scripts import first_line_re
import time

from more_itertools import first


def getUniqueLetters(input_string):
    """
     get and return all unique letters
    """
    pass

    # return ['Y', 'M', 'D', 'S', 'R', 'N', 'E', 'O']
    # ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']
    # result = []
    # index = 0
    # input_length = len(input_string)
    # while index < input_length:
        
    #     if input_string[index] not in result:
    #         result.append(input_string[index])

    #     index += 1

    # return list(set(input_string))

def check_equation(word, x, y, z, numbers):
    word_dict = dict(zip(word, numbers))
    first_half, second_half, equation_answer = '', '', ''               # Parameters for the equation

    # Convert str values correspos
    for letter in x:
        first_half = int(str(first_half) + word_dict[letter])
    for letter in y:
        second_half = int(str(second_half) + word_dict[letter])
    for letter in z:
        equation_answer = int(str(equation_answer) + word_dict[letter])
    # first_half,second_half, equation_answer = int(first_half), int(second_half), int(equation_answer) 

    if first_half + second_half == equation_answer:
        return True

    # print(letters_dict)
    # print("{} + {} = {}".format(first_half, second_half, equation_answer))

def solution():
    letters = 'SENDMORY'
    first_halfEqu = 'SEND'
    second_halfEqu = 'MORE'
    equation_answer = 'MONEY'

    len_letters = len(letters)

    # numbers = ['0', '1', '2', '3', '4', '5', '6','7', '8', '9']
   
    posssible_solutions = [] 
    for i in range(10**len_letters):
        number = str(i)
        N = len(number)
        if N == len_letters - 1:
            number = '0' + number
            N += 1
        
        if N == 8:
            if len(set(number)) == len_letters:
                # a = check_equation(letters, first_halfEqu, second_halfEqu, equation_answer, number)
                if check_equation(letters, first_halfEqu, second_halfEqu, equation_answer, number) == True:
                    posssible_solutions.append(number)
                    # break
                # S,E,N,D,M,O,R,Y = number
                # if int(S+E+N+D) + int(M+O+R+E)  == int(M+O+N+E+Y):
                #     posssible_solutions.append(number)

    print(len(posssible_solutions))
    return posssible_solutions


if __name__ == "__main__":
    start = time.time()
    result = solution()
    # result = None
    # for i in range(1_000_000):
    #     result = getUniqueLetters("SENDMOREMONEY")
    total_time = time.time() - start
    print(result, total_time)