# cubes every number in the given list  list_1 = [1,2,3,4,5,6,7,8,9]
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = []
for i in list1:
    list2.append((lambda x: x**3)(i))
print(list2)

