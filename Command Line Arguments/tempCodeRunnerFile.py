from sys import argv
s1 = argv[1]
s2 = argv[2]
s3 = argv[3]
s1 = s1.split("-")
s2 = s2.split("-")
s3 = s3.split("-")
happiness = 0
for i in s3:
    if i in s1:
        happiness += 1
    elif i in s2:
        happiness -= 1
print(happiness)