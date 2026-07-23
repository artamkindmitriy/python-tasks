list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merge_sorted_lists = list1 + list2
merged = list(set(merge_sorted_lists))
print(merged)