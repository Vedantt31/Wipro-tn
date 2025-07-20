# 1. Write a program to create a list of 5 integers and display the list items. Access individual elements through index.
L = [1,2,3,4,5]
print(L)
L[0] = 5
L[1] = 4
L[2] = 3
L[3] = 2
L[4] = 1
print(L)

# 2. Write a program to append a new item to the end of the list.
L = [1,2,3,4,5]
print(L)
L.append(input("Enter a number: "))
print(L)

# 3. Write a program to reverse the order of the items in the list.
L = [1,2,3,4,5,6]
for i in range(len(L)//2):
    L[i],L[len(L)-1-i] = L[len(L)-1-i],L[i]
print(L)

# 4. Write a program to print the number of occurrences of a specified element in a list.
L = [1,2,3,4,3,2,3,4,2,4]
target = int(input("Enter target: "))
count = 0
for i in L:
    if target == i:
        count += 1
print(count)

# 5. Write a program to append the items of list1 to list2 in the front.
List1 = [1,2,3,4,5]
List2 = [6,7,8,9,10]
for i in range(len(List1),len(List1) + len(List2)):
    List2.append(List2[i - len(List1)])
for i in range(len(List1)):
    List2[i] = List1[i]
print(List2)

# 6. Write a program to insert a new item before the second element in an existing list.
L = [1,2,3,4,100,500,62,42]
ele = int(input("Enter element: "))
L.insert(1,ele)
print(L)

# 7. Write a program to remove the item from a specified index in a list.
L = [1,2,3,4,100,500,62,42]
print(L)
target = int(input("Enter target index: "))
for i in range(target,len(L)-1):
    L[i] = L[i+1]
L.pop()
print(L)

# 8. Write a program to remove the first occurrence of a specified element from a list.
L = [1,2,3,4,3,2,3,4,2,4]
print(L)
target = int(input("Enter target: "))
L.remove(target)
print(L)
