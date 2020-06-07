from functools import reduce

lst = [47, 11, 113, 42, 13]

output = reduce(lambda x, y: x + y, lst)
print(output)

# Another reduce example:
# Find the maximum in a sequence, i.e. a replica of the max() function.
max_find = lambda a, b: a if (a > b) else b
max_number = reduce(max_find, lst)
print("Max number is:", max_number)