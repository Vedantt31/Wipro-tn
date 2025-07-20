"""
1. Write a program to add a key and value to a dictionary.   
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30} 
"""
D = {0:10,1:20}
Key = int(input("Enter Key: "))
Value = int(input("Enter value: "))
D[Key] = Value
print(D)

"""
2. Write a program to concatenate the following dictionaries to create a new one.  
Sample Dictionary : 
dic1={1:10, 2:20}  dic2={3:30, 4:40}  dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
dic1={1:10, 2:20}  
dic2={3:30, 4:40}  
dic3={5:50,6:60}
dic4 = {}
for i,j in dic1.items():
    dic4[i] = j
for i,j in dic2.items():
    dic4[i] = j
for i,j in dic3.items():
    dic4[i] = j
print(dic4)

# 3. Write a program to check if a given key already exists in a dictionary.
D = {0:10,1:20,2:30,3:40,4:50}
Key = int(input("Enter a key: "))
if(D.get(Key)):
    print("Key already Present")
else:
    print("Key not present. ")

# 4. Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.
D = {0:10,1:20,2:30,3:40,4:50}
for i in D.keys():
    print(i,end = "\t")
print()
for i in D.values():
    print(i,end = "\t")
print()
for i,j in D.items():
    print(f"{i} : {j}",end = "\t")

# 5. Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of the keys.
D = {}
for i in range(1,16):
    D[i] = i*i
print(D)

# 6. Write a program to sum all the values in a dictionary, considering the values will be of int type.
D = {0:10,1:20,2:30,3:40,4:50}
count = 0
for i in D.values():
    count += i
print(count)
