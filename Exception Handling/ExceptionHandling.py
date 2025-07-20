# 1. Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    print(num1/num2)
except ZeroDivisionError:
    print("Division BY Zero Not Allowed")
except Exception as e:
    print(e)

# 2. Write a program to accept a number from the user and check whether it’s prime or not. If user enters anything other than number, handle the exception and print an error message.
def Prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
try:
    num = int(input("Enter a number: "))
    print("Prime" if Prime(num) else "Not Prime.")

except ValueError:
    print("Value Error")


# 3. Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.
try:
    with open("Sample.txt", 'r') as file:
        contents = file.read()
        title = contents.title()
        print(title)
except FileNotFoundError:
    file = open("Sample.txt",'x')
    print("The file does not exist.")
    file.close()
except Exception as e:
    print(e)

# 4. Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.
numbers = [-4,-3,-2,-1,0,1,2,3,4,5]
try:
    index = int(input("Enter an index (0-9): "))
    number = numbers[index]
    if number > 0:
        print(f"The number at index {index} is positive.")
    elif number < 0:
        print(f"The number at index {index} is negative.")
    else:
        print(f"The number at index {index} is zero.")

except IndexError:
    print("Index Error")

except ValueError:
    print("Invalid input")
