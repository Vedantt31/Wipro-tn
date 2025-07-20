"""1. Create a dictionary that contains a list of people and one interesting fact about each of them. Display each person and his or her interesting fact to the screen. Next, change a fact about one of the people. Also add an additional person and corresponding fact. Display the new list of people and facts. Run the program multiple times and notice if the order changes.

Sample output:
Jeff: is afraid of Dogs.
David: Plays the plano.
Jason: Can fly an airplane.

Jeff: is afraid of heights.
David: Plays the piano.
Jason: Can fly an airplane.
Jill: Can hula dance.
"""
def Insert():
   for i, j in zip(Key, Value):
        if i not in D:
            D[i] = j


def Print():
    for i, j in D.items():
        print(f"{i}: {j}")
    print()

D = {}
Key = ["Jeff","David","Jason"]
Value = ["is afraid of Dogs.","Plays the plano.","Can fly an airplane."]
Insert()
Print()
Key.append("Jill")
Value.append("Can hula Dance.")
Insert()
Print()

"""2. Given the participant’sscore sheet for your University Sports Day, you are required to find the runner-up score. You have scores. Store them in a list and find the score of the runner-up.
Sample input:[2, 3, 6, 6, 5]
Sample output:5
Explanation:Given list is [2, 3, 6, 6, 5]. 
The maximum score is 6, second maximum is 5. Hence, we print 5as the runner-up score."""

Scores = []
num = int(input("Enter number of Scores: "))
for i in range(num):
    Scores.append(int(input("Enter Score:")))
New = set(Scores)
Scores = list(New)
sorted(Scores)
print("Runner Up: ",Scores[-2])

"""
3. You have a record of n students. Each record contains the student's name, and their percent marks in Math, Physics and Chemistry. The marks can be floating values.You are required to save the record in a dictionary data type.Student’s name is the key. Marks stored in a list is the value. The userenters a student's name. Output the average percentage marks obtained by that student.
Formula:(sum of marks) / (no of subjects)
Sample input:{ “Krishna” : [67,68,69],“Arjun” :[70,98,63],“Malika” : [52,56,60] }
Sample output:Enter a name: Malika
Average percentage mark: 56 
Explanation:Marks for Malika are [52, 56, 60] whose average is(52 + 56 + 60)/3 => 56
"""

D = { "Krishna" : [67,68,69], "Arjun" :[70,98,63], "Malika" : [52,56,60] }
Str = input("Enter a name: ")
Mark = D[Str]
sum = 0
for marks in Mark:
    sum += marks
print("Average percentage mark: ", sum/len(Mark))

"""
4. Given a string of n words, help Alex to find out how many times his name appears in the string. 
Constraint:1 <= n <= 200
Sample input:Hi Alex WelcomeAlex Bye Alex.
Sample output:3
Explanation:Alex name appears 3 times in the string. Hi AlexWelcomeAlexBye Alex.
"""
Str = input("Enter a String: ")
name = "Alex"
Str = Str.lower()
name = name.lower()
count = 0 
Str = Str.split()
for i in Str:
    if name in i:
        count += 1
print(count)