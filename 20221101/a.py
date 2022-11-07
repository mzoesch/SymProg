# https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods

str = 'Dr. Strangelove is the U.S. President\'s advisor.'


print(str[:25])
str = str[:25 - 3]
str = f'{str}...'
print(str.__len__())
print(str)
