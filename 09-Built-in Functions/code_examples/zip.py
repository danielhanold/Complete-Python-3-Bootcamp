# Zip two lists together.
x = [1, 2, 3]
y = [4, 5, 6]
result = zip(x, y)
print(result)
print(list(result))

# Zip two lists of different lengths.
x = [1, 2, 3]
y = [4, 5, 6, 7, 8]
print(list(zip(x, y)))

# Zip can be used on dictionaries as well.
d1 = {'a': 1, 'b': 2}
d2 = {'c': 4, 'd': 5}
zipped_keys = zip(d1, d2)
zipped_values = zip(d1.values(), d2.values())
print(list(zipped_keys))
print(list(zipped_values))
