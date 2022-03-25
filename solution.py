"""
 SEND
 MORE +
------
MONEY
------

"""

import time


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

def check_equation(word, first_part, second_part, answer, numbers):
    word_dict = dict(zip(word, numbers))
    first_half, second_half, equation_answer = '', '', ''               # Parameters for the equation

    for letter in first_part:
        first_half = int(str(first_half) + word_dict[letter])
    for letter in second_part:
        second_half = int(str(second_half) + word_dict[letter])
    for letter in answer:
        equation_answer = int(str(equation_answer) + word_dict[letter])

    if first_half + second_half == equation_answer:
        return True


def solution():
    letters = 'SWIFNMU'
    first_halfEqu = 'SUN'                   # All the letters should be in uppercase
    second_halfEqu = 'FUN'
    equation_answer = 'SWIM'

    len_letters = len(letters)
   
    posssible_solutions = [] 
    for i in range(10**len_letters):
        number = str(i)
        N = len(number)
        if N == len_letters - 1:
            number = '0' + number
            N += 1
        
        if N == len_letters:
            if len(set(number)) == len_letters:
                if check_equation(letters, first_halfEqu, second_halfEqu, equation_answer, number) == True:
                    posssible_solutions.append(number)
                
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