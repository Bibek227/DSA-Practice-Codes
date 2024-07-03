# Without loop

def PrintNos(N,c=1):
    
    if c>N: return
    print(c,end=' ')
    PrintNos(N,c+1)
PrintNos(9)