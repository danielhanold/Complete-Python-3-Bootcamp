# one.py
def func():
  print("FUNC() IN ONE.PY")

 def func2():
   print('func 2 in one.py')

print("TOP LEVEL IN ONE.PY")

if __name__ == '__main__':
  # Run the script.
  print('ONE.PY is being run directly!')
else:
  print('ONE.PY has been imported.')
