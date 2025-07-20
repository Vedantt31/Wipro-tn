#1.  Write a program to count the number of upper and lower case letters in a String.
Str = input("Enter a String: ")
up = low = 0
for i in range(len(Str)):
    if  Str[i].isupper():
        up += 1
    elif Str[i].islower():
        low += 1
print(f"Number of Upper Character = {up}\n Number of Lower Character = {low}")
#2.  Write a program that will check whether a given String is Palindrome or not.
s = input("Enter String: ")
s = s.lower()
print("Palindrom" if s == s[::-1] else "Not Palindrome" )
"""
3.  Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string. The string length will be >=2. 
If input is "Wipro" then output should be "WiWiWiWiWi".
"""
s = input("Enter String: ")
print(s[0:2] * len(s))

#4.  Given a string, if the first or last character is 'x', return the string without those 'x' character, else return the string unchanged. If the input is "xHix", then output is "Hi".
def Demo(s):
    if s[0] == s[-1] == "x":
        return s[1:len(s)-1]
    elif s[0] == "x":
        return s[1:]
    elif s[-1] == "x":
        return s[:-1]
    else:
        return s
s = input("Enter String: ")
print(Demo(s))

#5.  Given a string and an integer n, return a string made of n repetitions of the last n characters of the string. You may assume that n is between 0 and the length of the string inclusive. For example if the inputs are “Wipro” and 3, then the output should be “propropro”.
s = input("Enter a String: ")
num = int(input("Enter integer: "))
print(s[-num:]*num)
