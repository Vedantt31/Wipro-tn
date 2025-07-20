"""
1. Write a function to return the sum of all numbers in a list.  
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
"""
def Sum(n):
    add = 0
    for i in n:
        add += i
    return add
List = [8,2,3,0,7]
print("Sum: ",Sum(List))

"""
2. Write a function to return the reverse of a string.  
Sample String : "1234abcd"
Expected Output : "dcba4321"
"""
def Reverse(Str):
    return Str[::-1]
s = input("Enter a String: ")
print(s," reversed : ",Reverse(s))

# 3. Write a function to calculate and return the factorial of a number (a non-negative integer).
def Fact(n):
    if n < 0:
        return -1
    elif n <= 1:
        return 1
    else:
        return n * Fact(n-1)
n = int(input("Enter a number: "))
print(f"{n}! = {Fact(n)}")

# 4. Write a function that accepts a string and prints the number of upper case letters and lower case letters in it. 
def Upper(s):
    count = 0
    for i in s:
        if i.isupper():
            count += 1
    return count

def Lower(s):
    count = 0
    for i in s:
        if i.islower():
            count += 1
    return count

s = input("Enter a string: ")
print(f"Upper Character = {Upper(s)}, Lower character = {Lower(s)}")

"""
5. Write a function to print the even numbers from a given list. List is passed to the function as an argument. 
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
"""
def Even(List):
    num = []
    for i in List:
        if i % 2 == 0:
            num.append(i)
    return num
List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(Even(List))

# 6. Write a function that takes a number as a parameter and checks whether the number is prime or not.
def Prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
n = int(input("Enter a number: "))
print("Prime number" if Prime(n) else "Not Prime")
