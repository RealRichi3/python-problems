



solutionlist = []

valueList = []
def listAp(i):
    if i not in valueList:
        valueList.append(i)
        return True
    else:
        return False

def condCheck(s,e,n,d,m,o,r,y):
    send = 1000 * s + 100 * e + 10 * n + d
    more = 1000 * m + 100 * o + 10 * r + e
    money = 10000 * m + 1000 * o + 100 * n + 10 * e + y
    print('{} + {} = {}'.format(send, more, money))

    # if len(set(letters)) == len(letters):
    print("Checking condition")
    if send + more == money:
        print('{} + {} = {}'.format(send, more, money))
        print(valueList)
        valueList = []


def solution():
    for s in range(9, 0, -1):
        if listAp(s) == True:
            for e in range(9, -1, -1):
                if listAp(e) == True:
                    for n in range(9, -1, -1):
                        if listAp(n) == True:
                            for d in range(9, -1, -1):
                                if listAp(d) == True:
                                    for m in range(9, 0, -1):
                                        if listAp(m) == True:
                                            for o in range(9, -1, -1):
                                                if listAp(o) == True:
                                                    for r in range(9, -1, -1):
                                                        if listAp(r) == True:
                                                            for y in range(9, -1, -1):
                                                                if listAp(y) ==True:
                                                                    condCheck(s,e,n,d,m,o,r,y)

letters = list('sendmory')
print(solution())
                                