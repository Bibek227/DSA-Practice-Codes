x,y=map(int,input().split())
# gcd=0
# for i in range(1,min(x,y)+1):
#     if x%i==0 and y%i==0:
#         gcd=i
# print(gcd)
# lcm=x*y/(gcd)
# print(lcm)


# optimised way(Euclidean algorithm)
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
gcd=gcd(x,y)
lcm=(x*y)//gcd
print(lcm,gcd)