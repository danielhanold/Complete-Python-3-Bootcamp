lst = [True, True, False, True]
print(all(lst))
print(any(lst))

# Create a list with numbers. Find out if all of them are even.
num_list = [2, 4, 5, 6]
print("Are all numbers in this list even?", num_list)
print(all(map(lambda x: x % 2 == 0, num_list)))
print("Are any numbers in this list even?", num_list)
print(any(map(lambda x: x % 2 == 0, num_list)))
