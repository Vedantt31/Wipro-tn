# MINI PROJECT
# 1.	create a python program that asks the user how far they want to travel. if they want to travel less than three miles tell them to ride Bicycle. if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-cycle. if they want to travel three hundred miles or more tell them to driver Super-Car.
# Sample Output:
# How far would you like to travel in miles? 2500
# I suggest Super-Car to your destination
distance = float(input("How far would you like to travel in miles? "))
lt = ["Bicycle","Motor-cycle","Super-Car"]
if(distance <= 3.0):
    print(f"I suggest {lt[0]} to your destination")
elif(distance <= 300.0):
    print(f"I suggest {lt[1]} to your destination")
else:
    print(f"I suggest {lt[2]} to your destination")

# 2.	Let's assume you are planning to use your python skills to build an App for Mobile.
# You decide to host your application on servers running in the cloud. you pick a hosting provider that charges $0.51 per hour. you will launch your services using one server and want to know how much it will cost to operate per day, per week, per month.
# Write a python program that displays the answers to the following questions:
# How much does it cost to operate one server per day?
# How much does it cost to operate one server per week?
# How much does it cost to operate one server per month?
# How much days can I operate one server with $918?

charges = 0.51  # hourly charge
days = charges * 24 #daily charge
week = days * 7 #Weekly charge
month = days * 30 #monthly charge
money = 918.0  # budget
days_with_amount = int(money / days)

print("Cost to operate one server:")
print(f"Per day: $ {days:.2f}") # How much does it cost to operate one server per day?
print(f"Per week: $ {week:.2f}") # How much does it cost to operate one server per week?
print(f"Per month: $ {month:.2f}") # How much does it cost to operate one server per month?
print(f"{days_with_amount} days we can operate one server with ${money:.2f}.") # How much days can I operate one server with $918?
