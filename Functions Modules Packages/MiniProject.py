"""
Sort the Color
Write a Python functionthat accepts a hyphen-separated sequence of colors as input and returns the colors in a hyphen-separated sequence after sorting them alphabetically.
Constraint:All the colors will be completely in either lower case or upper case.
Sample input1:green-red-yellow-black-white
Sample output1:black-green-red-white-yellow
Sample input2:PINK-BLUE-TAN-PURPLE
Sample output2:BLUE-PINK-PURPLE-TAN
"""
def Sort(Colors):
    return "-".join(sorted(Colors))
Colors = input("Enter Colours: ")
Colors = Colors.split("-")
print(Sort(Colors))

"""
Playing with Names
Create a Python module with the following functions:
Function Name                            Task
ispalindrome(name)          Given the user name as input, this function should tell us whether the name is a palindrome or not.
count_the_vowels(name)      Given the user name as input, this function should tell us howmany vowels are present in it.
frequency_of_letters(name)  Given the user name as input, this function should tell us how many times each letter appears in the name.

Note:name will be completely in either lower case or upper case. Import the module in another python script and test the functions by passing appropriate inputs.
Sample input1:bob
Sample output 1:Yes it is a palindrome.
No of vowels: 1
Frequency of letters: b-2, o-1
Sample input2:marcelbentok tanaka
Sample output 2:No it is not a palindrome.
No of vowels: 7
Frequency of letters: m-1, a-4, r-1, c-1, e-2, l-1, b-1, n-2, t-2, o-1,k-2
"""
import MiniProject2 as mp
name = input("Enter Name: ")
print("Yes it is a palindrome." if mp.ispalindrome(name) else "No it is not a palindrome.")
print("No of vowels: ", mp.count_the_vowels(name))
print("Frequency of letters: ", end =" ")
mp.frequency_of_letters(name)