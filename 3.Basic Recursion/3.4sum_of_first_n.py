def sumOfSeries(n):
    
    
    if n<1:
        return 0
    return n**3+sumOfSeries(n-1)
#  return (n * (n + 1) // 2) ** 2      #optimized way
    
print(sumOfSeries(5))