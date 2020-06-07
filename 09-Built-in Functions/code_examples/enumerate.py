# Enumerate returns a tuple containing a count and a value.
lst = ['a', 'b', 'c', 'd', 'e']

for number, item in enumerate(lst):
    print('Number {number} in this list is {item}.'.format(number=number, item=item))

# Print the first 3 items.
for count, item in enumerate(lst):
    if count >= 2:
        break
    else:
        print(item)

# Enumerate takes an option "start" argument.
months = ['March', 'April', 'May', 'June']
print(list(enumerate(months, start=3)))