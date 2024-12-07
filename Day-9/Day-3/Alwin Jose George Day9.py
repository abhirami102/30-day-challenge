numbers = [1, 2, 3, 4, 2, 5, 6, 1, 7, 3]
duplicates = []
for num in numbers:
    if num not in duplicates:
        duplicates.append(num)
      print("Duplicate numbers are:", duplicates)
    print("original_list=",numbers)
