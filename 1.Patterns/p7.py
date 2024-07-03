for i in range(0,7):
    for j in range(0,7-i-1):
        print(" ",end="")
    for k in range(0,2*i+1):
        print("*",end="")
    for l in range(0,7-i-1):
        print(" ",end="")
    print()


#       *      
#      ***
#     *****
#    *******
#   *********
#  ***********
# *************