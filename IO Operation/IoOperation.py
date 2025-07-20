# 1. Write a program to read the entire content from a txt file and display it to the user.
f = open("Sample.txt")
print(f.read())
f.close()

# 2. Write a program to read first n lines from a txt file. Get n as user input.
f = open("Sample.txt")
n = int(input("Enter number of line: "))
for i in range(n):
    print(f.readline())
f.close()

# 3. Write a program to accept input from user and append it to a txt file.
f = open("Question3.txt",'a')
Str = input("Enter in File: ")
f.write(Str)
f.close()

# 4. Write a program to read contents from a txt file line by line and store each line into a list.
f = open("Sample.txt",'r')
list_of_lines = f.readlines()
print(list_of_lines)
f.close()

# 5. Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.
big = ""
f = open("Sample.txt",'r')
Content = f.read()
words = Content.split()
for i in words:
    if len(big)<len(i):
        big = i
print(big)
f.close()

# 6. Write a program to count the frequency of a user entered word in a txt file.
f = open("Sample.txt",'r')
Content = f.read()
words = Content.split()
D = {}
for word in words:
    if word in D.keys():
        D[word] += 1
    else:
        D[word] = 1
print(D.items())
f.close()
