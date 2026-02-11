import bisect

my_list = [10, 20, 30, 40, 50]

# Find insertion point for 25 (bisect_left)
index_left = bisect.bisect_left(my_list, 30)
print(f"Insertion point for 25 (left): {index_left}") # Output: 2

# Find insertion point for 25 (bisect_right)
index_right = bisect.bisect_right(my_list, 30)
print(f"Insertion point for 25 (right): {index_right}") # Output: 2

# Insert 25 using insort_left
bisect.insort_left(my_list, 30)
print(f"List after insort_left(25): {my_list}") # Output: [10, 20, 25, 30, 40, 50]

# Insert 30 again using insort_right
bisect.insort_right(my_list, 30)
print(f"List after insort_right(30): {my_list}") # Output: [10, 20, 25, 30, 30, 40, 50]