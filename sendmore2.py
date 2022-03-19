"""
Algo to implement the first answer i gave to the SEND + MORE = MONEY equ 
although the ans to the que was wrong
Assigns different values from range 0-9 to each variable in sendmory
And checks if the equation is satisfied

PS: I didn't try to make the code simpler yet. 
After many tries, this is just the first stable code that made sense to me

CODE
Go through the letters
Assign a value for each
Check if that same value has been assigned to an earlier variable
Input the variables into the equation

"""


valueList = ''                          # List of all the numbers already assigned to a var
tf = None

def checkEquation():
    """
    Inputs the parameters into the equation and checks if it's satisfied
    """
    global valueList

    s = int(valueList[0])               # Convert string of all the numbers in ValueList to int
    e = int(valueList[1])               # and assign them to the different varialbes
    n = int(valueList[2])
    d = int(valueList[3])
    m = int(valueList[4])
    o = int(valueList[5])
    r = int(valueList[6])
    y = int(valueList[7])

    send = 1000 * s + 100 * e + 10 * n + d
    more = 1000 * m + 100 * o + 10 * r + e
    money = 10000 * m + 1000 * o + 100 * n + 10 * e + y

    if send + more == money:
        print("{} + {} = {}".format(send, more, money))
    # else:
        # valueList = ''

    # print("{} {} {} {} + {} {} {} {} = {} {} {} {} {} ".format(s,e,n,d,m,o,r,e,m,o,n,e,y))

def listAp(letterValue):
    """
    Func to Check if the interger has been assigned to a variable before
    If not it'll then update the valueList with with newly assigned integer
    """
    
    global valueList
    global tf                               # True or False variable

    letterValue = str(letterValue)          # Change var from int to str

    if letterValue in valueList:            # Checks if integer has been assigned to another var before
        tf = False
    else:
        valueList += letterValue            # Update the value list
        tf = True

def iterateLetters():
    """
        Function to scan through the letters and assign an integer to each
    """
    global valueList

    for s in range(0, 10):
        valueList += str(s)
        for e in range(0, 10):
            listAp(e)                      # Check if the integer has been assigned to another variable before
            if tf == True:
                for n in range(0, 10):
                    listAp(n)
                    if tf == True:
                        for d in range(0, 10):
                            listAp(d)
                            if tf == True:
                                for m in range(0, 10):
                                    listAp(m)
                                    if tf == True:
                                        for o in range(0, 10):
                                            listAp(o)
                                            if tf == True:
                                                for r in range(0, 10):
                                                    listAp(r)
                                                    if tf == True:
                                                        for y in range(0, 10):
                                                            listAp(y)
                                                            if tf == True:
                                                                checkEquation()
        print(valueList)
        valueList = ''
                                                                
                                                                # condCheck(s,e,n,d,m,o,r,y)
iterateLetters()