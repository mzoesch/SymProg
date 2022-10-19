import re

x = re.search('Hello', 'Hello World')
print(x)

y = re.search('M[ae][iy]er', 'Mayer')
print(y)

z = re.search('M[^0-9]y', 'May')  # Not
print(z)

a = re.search('M[\s]a', 'M a')  # Space
print(a)

# etc.
