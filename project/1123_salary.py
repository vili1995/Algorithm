def listToInt(myList):
    myInt = int(''.join(myList))
    return myInt

def intToList(myInt):
    strInt = str(myInt)
    myList = list(strInt)
    return myList

def cal(strInput): #calculate
    if (len(strInput) == 1):
        return int(strInput)

    intOldSalary = int(strInput)
    listNum = list(strInput)

    f1 = list (listNum[:int(len(listNum)/2)]) #list half 1
    f2 = list(listNum[int(len(listNum) / 2)]) # list half 2
    boolHasEdge = bool(len(listNum)%2 != 0)

    if boolHasEdge:
        strEdge = f2.pop(0)

    if listToInt(f2)> int(str(listToInt(f1))[::-1]):
        if boolHasEdge:
            if strEdge != "9":
                strEdge = str(int(strEdge)+1)
                strTempList = str(listToInt(f1))
            else:
                strEdge = "0"
                intTempList = listToInt(f1)
                intTempList += 1
                strTempList = str(intTempList)
            intResult = int(strTempList+strEdge+strTempList[::-1])
        else:
            strTempList = str(listToInt(f1)+1)
            intResult = int(strTempList+strTempList[::-1])
    else:
        if boolHasEdge:
            intResult = int(str(listToInt(f1)) + strEdge + str(listToInt(f1))[::-1])
        else:
            intResult = int(str(listToInt(f1)) + str(listToInt(f1))[::-1])
    return intResult

strInput = input()
print(cal(strInput))