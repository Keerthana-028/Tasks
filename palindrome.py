def ispalindrome(a):
    return a==a[::-1]
a=input("enter the string:")
output=ispalindrome(a)
if output:
    print('The given string is a palindrome')
else:
    print('It is not a palindrome')

