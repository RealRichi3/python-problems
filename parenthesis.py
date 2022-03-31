import random

"""
Given a series fo parentheses, check if they are balanced
i.e each open bracket needs to have a matching closed backet 
in the correct order
"""


def checkparen(parenstr, checklist, start, stop, gen = 0): 

    if gen == 1:                         # Generate List of random parenthesis
        parenstr = ''                     
        for _ in range(random.randint(start, stop)):        
            a = random.randint(0, 1)
            parenstr += '(' if a == 0  else ')'
    print(parenstr)

    for i in parenstr:
        if i == "(":
            checklist.append(i)
        elif i == ")":
            if ((len(checklist) > 0) and ("(" == checklist[-1])): 
               checklist.pop() 
            else: 
                return "Unbalanced"

    return "Balanced" if len(checklist) == 0 else "Unbalanced"



paren = "(()(((()()))((()())())"
print(checkparen(paren, [], 5, 24, 1))
