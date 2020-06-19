import re

fo = open("PyChallenge3","r")
searchedString = fo.read()

test = re.findall("[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]", searchedString)

print(test)
for tupNum in range(len(test)):
    currentTuple = test[tupNum]
    print(currentTuple[4], end = "")

fo.close()


    



