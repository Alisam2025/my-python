#This is list of lists
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Accessing elements in a list of lists
print(my_list[0])  # Output: [1, 2, 3]
print(my_list[1])  # Output: [4, 5, 6]
print(my_list[2])  # Output: [7, 8, 9]
print()
print()
# Accessing elements in a nested list
print(my_list[0][0])  # Output: 1
print(my_list[0][1])  # Output: 2
print(my_list[0][2])  # Output: 3
print(my_list[1][0])  # Output: 4
print(my_list[1][1])  # Output: 5
print(my_list[1][2])  # Output: 6
print(my_list[2][0])  # Output: 7
print(my_list[2][1])  # Output: 8
print(my_list[2][2])  # Output: 9
print()
print()
# Modifying elements in a list of lists
my_list[0][0] = 10
my_list[0][1] = 20
my_list[0][2] = 30
print(my_list)  # Output: [[10, 20, 30], [4, 5, 6], [7, 8, 9]]
print()
print()
# Adding elements to a list of lists
my_list.append([10, 11, 12])
print(my_list)  # Output: [[10, 20, 30], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print()
print()
my_list.insert(1, [13, 14, 15])
print(my_list)  # Output: [[13, 14, 15], [10, 20, 30], [4, 5, 6], [7, 8, 9], [10, 11, 12]]