# Typ
from distutils.log import ERROR, error
from fileinput import filename


strVar: str = "Hello World"
print(strVar)

# Just some string stuff
s = 'f ln \ns ln'
print(s)
s = r'f ln\nstill f ln'
print(s)
s = """
Multiple lines
"""  # Code rev
escape = '\''
print(escape)
x = 'ö'
y = x.encode('UTF-8')
print(y)
s = 'Just some random string'
print(s)
print(s[0])  # Zero based
print(s[-1])  # Back
print(s[2:10])  # Substring
print(s[:4])  # Substring - Shorthanded
print(s[::-1])  # Back

# Dirs
d = {              # Val is mutable
    'key': 'val',  # Key is immutable and unique
    'quant': 3,
    'color': 'green'
}
d['quant'] += 1
# Unmachable key won't be created - not fechtable
# d['num'] += 1

print(d.get('quant'))
# d.pop('quant')
# del d['quant']  # Equal to pop
print(d.values())
print(d.items())
print(len(d))

# Sets
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(s)
s.add(11)
print(s)
s.remove(11)  # Error if not found
print(s)
s.discard(11)  # No error if not found
print(s)
s.pop()  # First element
print(s)
s.clear()  # Empty set
print(s)

# Statements of control
# Not writing this

x = 'Just some string'
while x:
    print(x)
    x = x[1:]  # Slice

# IO Streams
filename = 'Path/To/File.txt'
try:
    with open(filename, mode='r') as f:
        for line in f:
            print(line)
        f.readline()  # Read one line
        f.readlines()  # Read all lines
        f.read()  # Read all

except FileNotFoundError as e:  # Is just a demo path
    error(e)

# Functions
# Not writing this
# But


def multiply(x, y):
    pass


var = multiply
print(var(2, 3))

# Unittesting - more flexible than doctest
