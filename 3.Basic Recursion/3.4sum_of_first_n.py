def sumOfSeries(n):
    
    
    if n<1:
        return 0
    return n**3+sumOfSeries(n-1)
    
print(sumOfSeries(5))