# 1. Write a program to print the 4th element from first and 4th element from last in a tuple.
tup = (1,2,3,4,5,6,7,8,9,10)
print("4th element from first: ",tup[3])
print("4th element from end: ",tup[-4])

# 2. Write a program to check whether an element exists in a tuple or not.
tup = (1,2,3,4,5,6,7,8,9,10)
ele = int(input("Enter an element: "))
if ele not in tup:
    print(f"{ele} not in tuple")
else:
    print(f"{ele} in tuple")

# 3. Write a program to convert a list into a tuple.
List = [1,2,3,4,5,6,7,8,9,10]
tup = tuple(List)
print(type(tup))

# 4. Write a program to find the index of an item in a tuple.
tup = (1,2,3,4,5,6,7,8,9,10)
ele = int(input("Enter element: "))
print(tup.index(ele))

"""5. Write a program to replace last value of tuples in a list to 100.  
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]"""
List = [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
for i in range(len(List)):
    List[i] = list(List[i])
    List[i][-1] = 100
    List[i] = tuple(List[i])
print(List)
