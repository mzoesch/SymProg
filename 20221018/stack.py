# Example class for doctesting
class Stack():
    """ Basic stack implementation.

    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> stack.push(3)

    >>> stack.peek()
    3
    >>> stack.is_empty()
    False
    >>> stack.size()
    3
    >>> stack.pop()
    3
    >>> stack.pop()
    2
    >>> stack.pop()
    1
    >>> stack.is_empty()
    True

    >>> stack.pop()
    Traceback (most recent call last):
    ...
    IndexError: pop from empty list

    """

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return not bool(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # python3 stack.py -v # Verbose mode or
    # python3 -m doctest -v stack.py
