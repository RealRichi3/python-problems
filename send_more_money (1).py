def solution():

    
    size = len(letters)
    used_numbers = set()
    possible_values = []
    current_value = ['-1'] * size # mapped to the letters in this order ['s', 'e','n','d','m','o','r','y']
    
    assign(size, used_numbers, current_value, possible_values)

    print(len(possible_values), possible_values)



def assign(letter, used_numbers, current_value, possible_values):

    if letter == 0:
        S,E,N,D,M,O,R,Y = current_value
        if int(S+E+N+D) + int(M+O+R+E) == int(M+O+N+E+Y):
            possible_values.append("".join(current_value))
        return

    for num in "0123456789":
        if num not in used_numbers:
            used_numbers.add(num)
            current_value[letter - 1] = num
            assign(letter - 1, used_numbers, current_value, possible_values)
            used_numbers.remove(num)
            current_value[letter - 1] = '-1'
        
if __name__ == "__main__":
    letters = list('sendmory')
    solution()
