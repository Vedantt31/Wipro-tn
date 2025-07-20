from sys import argv
# 1. Write a program to accept two numbers as command line arguments and display their sum.
num1 = int(argv[1])
num2 = int(argv[2])
print(num1+num2)
# 2. Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.
from sys import argv
Message = argv[1]
print(Message," ",argv[0])

# 3. Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.
from sys import argv
def Prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
Sum = 0
for i in range(1,11):
    if Prime(int(argv[i])):
        Sum += int(argv[i])
print(Sum)
