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


def solution():
    letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']

    numbers = ['0', '1', '2', '3', '4', '5', '6','7', '8', '9']
   
    posssible_solutions = [] 
    for i in range(10**8):
        number = str(i)
        N = len(number)
        if N == 7:
            number = '0' + number
            if len(set(number)) == 8:
                S,E,N,D,M,O,R,Y = number
                if int(S+E+N+D) + int(M+O+R+E)  == int(M+O+N+E+Y):
                    posssible_solutions.append(number)
        elif N == 8:
            if len(set(number)) == 8:
                S,E,N,D,M,O,R,Y = number
                if int(S+E+N+D) + int(M+O+R+E)  == int(M+O+N+E+Y):
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