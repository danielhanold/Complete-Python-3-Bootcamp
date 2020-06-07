# Function to convert celcius to fahrenheit.
def fahrenheit(celsius):
    return (9/5)*celsius + 32

temps = [0, 22.5, 40, 100]

# Using a for loop.
f_temps = []
for temp in temps:
    f_temps.append(fahrenheit(temp))
print(f_temps)

# Using a list comprehension.
f_temps = [fahrenheit(temp) for temp in temps]
print(f_temps)

# Using a map.
f_temps = map(fahrenheit, temps)
print(f_temps)
print(list(f_temps))
for temp in f_temps:
    print(temp)

# Using a map with a lambda function.
f_temps = map(lambda x: (9 / 5) * x + 32, temps)
print(list(f_temps))
