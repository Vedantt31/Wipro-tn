#  Write a LC program to create an output dictionary which contains only the odd numbers that are present in the input list = [1,2,3,4,5,6,7] as keys and their cubes as values
D = {x:x**3 for x in range(10) if x%2!=0}
print(D)


#  Make a dictionary of the 26 english alphabets mapping each with the corresponding integer
D = {x-63: chr(x+1) for x in range(64, 90)}
print(D)

