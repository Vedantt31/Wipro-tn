"""
You had saved the items and their price details in a text file, which you purchased yesterday from a nearby super market. 
You need to know:
1.How many items did you purchase?
2.How many items are free?
3.What is the total amount you had to pay?
4.What is the discount amount?
5.What is the final amount did you pay after the discount?

Help yourself by writing a python code to do this.Include necessary code to handle the possible exceptions.
Note: 
Data is stored in a text file Purchase-1.txt.
Each line contains one item’s details.
Item name and price is separated by a space.
You have to enter the file name during run time.

Sample input1:
Purchase-1.txt
Chocolate 50
Biscuit 35
Icecream 50
(blank line)
Discount  5

Sample output 1:
Enter the file name:Purchase-1
No of items purchased:3
No of free items:0
Amount to pay:135
Discount given:5
Final amount paid: 130

Sample input2:
Purchase-1.txt
Chocolate 50
Biscuit 35
Icecream 50
Rice 100
Chicken 250
(blank line)
Perfume Free
Soup Free
(blank line)
Discount 80

Sample output 2:
Enter the file name:Purchase-1
No of items purchased:5
No of free items:2
Amount to pay:485
Discount given:80
Final amount paid: 405
"""

# Direct script without functions

try:
    filename = input("Enter the file name:") + ".txt"

    with open(filename, "r") as file:
        lines = file.readlines()

    item_count = 0
    free_item_count = 0
    total_amount = 0
    discount = 0
    processing_free_items = False

    for line in lines:
        line = line.strip()
        if not line:
            # Blank line: indicates a section break (start of free items)
            processing_free_items = True
            continue

        parts = line.split()
        if len(parts) < 2:
            continue  # Skip malformed lines

        item_name = parts[0]
        item_value = parts[1]

        if item_name.lower() == "discount":
            try:
                discount = int(item_value)
            except ValueError:
                print(f"Invalid discount value: {item_value}")
                discount = 0
        elif item_value.lower() == "free":
            free_item_count += 1
        else:
            try:
                price = int(item_value)
                if not processing_free_items:
                    item_count += 1
                    total_amount += price
            except ValueError:
                print(f"Invalid price value for item '{item_name}': {item_value}")
                continue

    final_amount = total_amount - discount

    print(f"Enter the file name:{filename[:-4]}")
    print(f"No of items purchased:{item_count}")
    print(f"No of free items:{free_item_count}")
    print(f"Amount to pay:{total_amount}")
    print(f"Discount given:{discount}")
    print(f"Final amount paid: {final_amount}")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
