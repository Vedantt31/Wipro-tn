"""
ispalindrome(name)          Given the user name as input, this function should tell us whether the name is a palindrome or not.
count_the_vowels(name)      Given the user name as input, this function should tell us howmany vowels are present in it.
frequency_of_letters(name)  Given the user name as input, this function should tell us how many times each letter appears in the name.
"""
def ispalindrome(name):
    name = name.replace(" ","")
    name = name.lower()
    return name == name[::-1]

def count_the_vowels(name):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    count = 0
    for i in name:
        if i in vowels:
            count += 1
    return count

def frequency_of_letters(name):
    name = name.replace(" ","")
    D = {}
    s = ""
    for i in name:
        if i in D.keys():
            D[i] += 1
        else:
            D[i] = 1
    for i,j in D.items():
        print(f"{i}-{j}",end = ",")