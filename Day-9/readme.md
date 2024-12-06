# Day-9 Question: Find Duplicate Numbers in a Predefined List

## Write a program that:

    Defines a list of integers.
    Identifies and displays all the duplicate numbers in the list.
    Displays each duplicate number only once, even if it appears multiple times.

Code:
``` python
# Step 1: Define the list of numbers
numbers = [1, 2, 3, 4, 2, 5, 6, 1, 7, 3]

# Step 2: Find duplicate numbers
duplicates = []
for num in numbers:
    if num not in duplicates:
        duplicates.append(num)

# Step 3: Display the duplicate numbers
    print("Duplicate numbers are:", duplicates)
    print("original_list=",numbers)

Expected Output:

If the list is numbers = [1, 2, 3, 4, 2, 5, 6, 1, 7, 3], the output will be:

Duplicate numbers are: [1, 2, 3]
original_list=[1, 2, 3, 4, 2, 5, 6, 1, 7, 3]
