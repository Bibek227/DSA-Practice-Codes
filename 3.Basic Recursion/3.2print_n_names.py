# def printNames(n):
#     def helper(c=1):
#         if c>n: return
#         print("Bibek",end=' ')
#         helper(c+1)
#     helper(1)
# printNames(3)


# or without helper function

def printNames(n,c=1):
    
    if c>n: return
    print('Bibek',end=' ')
    printNames(n,c+1)
printNames(3)
