"""
SEND + MORE = MONEY
"""

def checkDict(mydict):
    pass

word = 'SENDMORNY'
wordDict = {}

for letter in word:             # Append all the letters to the dictionary as Keys and use 0 as the default Value
    wordDict[letter] = 10
    
wordlist = list(wordDict.keys())
count = 0
for key in wordDict.keys():     # Iterate through the keys SENDMORY
    for num in range(0,8):      # Assigns different num from 0 to 8 to each element
        if num not in wordDict.values():    # Check if value is already given to a key
            wordDict[wordlist[num]] = num
        else:
            pass
        count += 1
    print(wordDict)