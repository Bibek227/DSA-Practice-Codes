# factorial using recursion
def factorial(n):
    if n==0: return 1
    return n*factorial(n-1)
print(factorial(5))


# n=5
# fact=1
# result=[]
# for i in range(1,n+1):
#         fact=fact*i
#         if fact<n:
#             result.append(fact)
# print(result)


# n=5
# i=1
# fact=1
# result=[]
# while i<=n:
#     fact=fact*i
#     i+=1
#     if fact<n:
#         result.append(fact)
# print(result)


