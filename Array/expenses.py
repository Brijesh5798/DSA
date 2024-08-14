# Let us say your expense for every month are listed below
expenses = [2200, 2350, 2600, 2130, 2190]

# In Feb, how many dollars you spent extra compare to January?
difference = expenses[1] - expenses[0]
if difference > 0:
    print(f"{difference}$ were spent extra in february compare to January")
if difference < 0:
    print(f"{difference}$ were spent less in february compare to January")
if difference == 0:
    print("dollars spent in february and January are same")

# Find out your total expense in first quarter (first three months) of the year.
total = expenses[0] + expenses[1] + expenses[2]
# for i in range(3):
#     total = total + expenses[i]
print(f"total expense in first quarter: {total}")

# Find out if you spent exactly 2000 dollars in any month
if 2000 in expenses:
    print("yes exact match found")
else:
    print("match not found")
    
# June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(1980)
print(f"June month expense added: {expenses}")

# You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
expenses[3] = expenses[3] - 200
print(f'Updated expenses: {expenses}')
