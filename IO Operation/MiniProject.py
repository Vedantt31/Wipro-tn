"""
Your friend has sent you a text file containing n lines. He sent a secret message with it, which tells you the place and time where you have to go and meet him.

He challenges you to find it out without seeing the content of the file. He has given hints to find the secret message. Let’s surprise him by breaking the challenge with our Python code!
Hints to find the secret message:
The number of lines in the file tells you the meeting time.
Note: 1 <= number of lines <= 24
If the number of lines is 12 or less, it is in AM.
If the number of lines exceeds 12, convert it to 12-hour format (PM).

For example:
If the number of lines is 15, then the meeting time is 3 PM.
If the number of lines is 10, then the meeting time is 10 AM.
The word appearing the maximum number of times tells you the meeting place.
Note: The meeting place will be a street name.

For example:
If the word "Oxford" appears most frequently, then the meeting place is "Oxford Street".
If the word "Park" appears most frequently, then the meeting place is "Park Street".

Sample Input 1:
Sample.txt
Cricket, a bat-and-ball park game played between two teams of eleven park players on a field at the park center of which is a 20-metre (22-yard) pitch with a wicket at each end, each park comprising two bails balanced on three stumps.

The batting park scores runs by striking the ball bowled at the park wicket with the park bat, while the bowling and park fielding side tries to prevent this and dismiss each park player (so they are "out").

Means of park include being bowled, when the ball hits the park and dislodges the bails, and by the fielding side park the ball after it is hit by the bat, but before it hits the park.

When ten park have been dismissed, the innings ends and the teams park roles.

Sample Output 1:
Meeting time: 9 AM  
Meeting place: Park Street
Explanation:
Number of lines = 9 → 9 AM
Most frequent word = "park" → Park Street

Sample Input 2:
Sample.txt
Royal Enfield is an Indian Apollo motorcycle manufacturing brand with the tag of "oldest Apollo motorcycle brand in continuous production" manufactured in Apollo factories in Chennai Apollo India.

Licensed from Royal Enfield by indigenous Indian Madras Motors, it is now an Apollo subsidiary of Eicher Motors Limited, an Indian Apollo automaker.

The company makes Apollo Royal Enfield Bullet, and other single-cylinder and twin-cylinder Apollo motorcycles.

First produced in 1901, Royal Enfield is the oldest motorcycle Apollo brand in the world still in production, with the Bullet model enjoying the longest motorcycle Apollo production run of all time.

In 1990, Royal Enfield collaborated with Eicher Apollo Group, an automotive company in Apollo India, and merged with it in 1994.

Apart from bikes, Eicher Apollo Group is involved in the production and sales of Apollo commercial vehicles and automotive gears.

Although Apollo Royal Enfield experienced difficulties in the 1990s, and ceased Apollo motorcycle production at their Jaipur factory in 2002, by 2013 the Apollo company opened a new primary Apollo factory in the Apollo Chennai suburb of Oragadam on the strength of increased demand for its Apollo motorcycles.

This was followed in Apollo 2017 by the inauguration of another new factory of a similar size to the facility at Apollo Oragadam (capacity 600,000 vehicles per year) at Vallam Apollo Vagadal.

The original factory at Apollo Tiruvottiyur became secondary and continues to produce some limited-run motorcycle models.

Sample Output 2:
Meeting time: 8 PM  
Meeting place: Apollo Street
Explanation:
Number of lines = 20 → 8 PM
Most frequent word = "Apollo" → Apollo Street
"""

f = open("Sample2.txt",'r')
lines = f.readlines()
time = len(lines)
print("Meeting time:", (str(time) + "AM") if time <=12 else (str(time%12) + "PM"))
Content = " ".join(lines)
Content = Content.lower()
words = Content.split()
D = {}
for word in words:
    if word in D.keys():
        D[word] += 1
    else:
        D[word] = 1
frequency = D.values()
High = max(frequency)
for i,j in D.items():
    print(i," ",j)
    if j == High:
        place = i
        break 
print("Meeting place:", place,"Street")
f.close()