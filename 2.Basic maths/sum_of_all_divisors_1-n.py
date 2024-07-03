n=int(input("enter a number "))

# suma=0
# for i in range(1,n+1):
#     sumi=0
#     for j in range(1,i+1):
#         if i%j==0:
#             sumi=sumi+j
#     suma=suma+sumi
# print(suma)


# Optimized way

total_sum=0
for i in range(1,n+1):
    total_sum+=i*(n//i)
print(total_sum)
