# normal method

# number
# a=123
# old=a
# new=0
# while a>0:
#     r=a%10
#     new=new*10+r
#     a//=10
# if old==new:
#     print('it is palindrome',new)
# else:
#     print('It is not palindrome',new)

# string
# str='abac'
# s=str.lower()
# for i in range(len(s)//2):
#     if s[i]!=s[len(s)-i-1]:
#         print('not palindrome')
#     else:
#         print('palindrome')


def isPalindrome(s):
    s=s.replace(" ","").lower()
    return s==s[::-1]
string=''
if isPalindrome(string):
    print(f'"{string}" is a palindrome')
else:
    print(f'"{string}" is not a palindrome')