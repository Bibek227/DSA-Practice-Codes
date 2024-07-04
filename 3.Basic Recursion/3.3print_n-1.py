def printNos(n):
    if n<1: return
    print(n,end=' ')
    printNos(n-1)
printNos(10)