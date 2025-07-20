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
    print("Error: The index is out of range. Please enter a number between 0 and 9.")

except ValueError:
    print("Error: Invalid input. Please enter an integer.")