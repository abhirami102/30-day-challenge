list1 = [5, 3, 8, 1]
list2 = [7, 2, 6, 4]
merged_list = list1 + list2  # Combine both lists into one
merged_list.sort()  # Sort the merged list in place
largest_number = merged_list[-1]  # The last element in a sorted list is the largest
print("The merged and sorted list is:", merged_list)
print("The largest number in the list is:", largest_number)
