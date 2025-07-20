# 1. Write a program to remove a given item from the set.
Set = {1,2,3,4,5,6,7,8,9,10}
ele = int(input("Enter an element: "))
print(Set)
Set.remove(ele)
print(Set)
# 2. Write a program to create an intersection of sets.
S1 = {1,2,3,4,5}
S2 = {4,5,6,7,8,9,10}
print(S1.intersection(S2))

# 3. Write a program to create an union of sets.
S1 = {1,2,3,4,5}
S2 = {4,5,6,7,8,9,10}
print(S1.union(S2))

# 4. Write a program to find the maximum and minimum value in a set.
Set = {1,3,4,53,22,34,21,43}
print(max(Set))