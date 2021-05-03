def Main():
    arrChar = ['A', 'B', 'C']
    k = 3
    n = len(arrChar)
    #PrintAllResult(arrChar, "", n, k)
    PrintAllResultDistinct(arrChar, "", n, k, 1)


def PrintAllResult(set, prefix, n, k):
    if k == 0:
        print(prefix)
        return

    for index in range(n):
        newPrefix = prefix + set[index]
        PrintAllResult(set, newPrefix, n, k - 1)

def PrintAllResultDistinct(set, prefix, n, k, validCount):
    if k == 0:
        print(prefix)
        return

    for index in range(validCount):
        newPrefix = prefix + set[index]
        
        newValidCount = validCount + 1 if ((index == (validCount - 1)) & (validCount < n)) else validCount

        PrintAllResultDistinct(set, newPrefix, n, k - 1, newValidCount)


Main()