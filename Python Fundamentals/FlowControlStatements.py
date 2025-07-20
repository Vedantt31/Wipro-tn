# 1. Write a program to check if a given number is Positive, Negative, or Zero.
num = int(input("Enter a number: "))
if num == 0:
    print(num," is Zero")
elif num > 0:
    print(num, " is positive.")
else:
    print(num, "is negative")

# 2. Write a program to check if a given number is odd or even.
num = int(input("Enter a number: "))
print(f"{num} is even" if num % 2 == 0 else f"{num} is odd")

"""3. Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.
# lastDigit(7, 17) → true                                                
# lastDigit(6, 17) → false
# lastDigit(3, 113) → true"""
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
print("True" if num1 % 10 == num2 % 10 else "False")

# 4. Write a program to print numbers from 1 to 10 in a single row with one tab space.
for i in range(1,11):
    print(i, end ="\t")

# 5. Write a program to print even numbers between 23 and 57. Each number should be printed in a separate row.
for i in range(23,57):
    if(i % 2 == 0):
        print(i)

# 6. Write a program to check if a given number is prime or not.

num = int(input("Enter a number: "))
Flag = False
if num >= 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            Flag = False
            break
        Flag = True
print(Flag)

# 7. Write a program to print prime numbers between 10 and 99.
def Prime(num):
    Flag = False
    if num >= 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                Flag = False
                return
        return True
    return False
for i in range(10, 100):
    if Prime(i):
        print(i)

"""8. Write a program to print the sum of all the digits of a given number.
Example:
I/P:1234
O/P:10"""
num = abs(int(input("Enter a number: ")))
sum = 0
while num != 0:
    sum += num%10
    num //= 10
print(sum)

"""9. Write a program to reverse a given number and print.

Example:1
I/P: 1234
O/P:4321

Example:2
I/P:1004
O/P:4001"""
num1 = abs(int(input("Enter a number: ")))
num2 = 0
while num1 != 0:
    num2 = (num2*10) + (num1%10)
    num1 //= 10
print(num2)

"""10. Write a program to find if the given number is palindrome or not

Example:1
I/P:110011
O/P: 110011 is a palindrome.

Example:2
I/P:1234
O/P: 1234 is not a palindrome."""
def Palindrome(num1):
    num2,num3 = 0,num1
    while num1 != 0:
        num2 = (num2*10) + (num1%10)
        num1 //= 10
    return num2==num3

num = abs(int(input("Enter a number: ")))
if num >=1:
   print(Palindrome(num))
else: 
    print("False")
