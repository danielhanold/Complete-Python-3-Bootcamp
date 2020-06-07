# Create a function to determine if a number is even.
def even_check(num):
    return num % 2 == 0

# For loop.
even_nums = []
for num in range(20):
    if even_check(num):
        even_nums.append(num)
print(even_nums)

# List comprehension.
even_nums = [num for num in range(20) if even_check(num)]
print(even_nums)

# Filter function.
even_nums = filter(even_check, range(20))
print(list(even_nums))

# Filter check with lambda function.
even_nums = filter(lambda num: num % 2 == 0, range(20))
print(list(even_nums))