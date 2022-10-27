# More info : https://stackoverflow.com/questions/306313/is-operator-behaves-unexpectedly-with-integers


def main():

    # Here True
    x = 256
    y = 256
    print('Value: 256')
    print('x == y is : ', x == y)
    print('x is y is : ', x is y)
    print(f'id of x : {id(x)}')
    print(f'id of y : {id(y)}')

    x = 257
    y = 257
    print('Value: 257')
    print('x == y is : ', x == y)
    print('x is y is : ', x is y)
    print(f'id of x : {id(x)}')
    print(f'id of y : {id(y)}')

    # Here False
    """
    >>> x,y = 256, 256
    >>> x == y
    True
    >>> x is y
    True
    >>> x,y = 257, 257
    >>> x == y
    True
    >>> x is y
    True # Why True??
    >>> x = 257
    >>> y = 257
    >>> x is y
    False # But here False??
    >>> 
    """

# reverse list same id?


if __name__ == '__main__':
    main()
