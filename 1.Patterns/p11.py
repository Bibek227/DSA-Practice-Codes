for i in range(0,7):
    start=1
    if i%2==0:
        start=1
    else:
        start=0
    for j in range(0,i):
        print(start,end="")
        start=1-start
    print()