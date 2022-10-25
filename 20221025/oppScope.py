from unicodedata import name


class ScopeClass:

    def __init__(self, var1, var2, var3, var4):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3
        self.__var4 = var4


if __name__ == '__main__':
    scope = ScopeClass(1, 2, 3, 4)
    print(scope.var1)
    print(scope._var2)
    # print(scope.__var3) # Will throw
    # Get around
    scope.__dict__['_ScopeClass__var3']  # or set value
    # scope.__dict__['_ScopeClass__var3'] = 4
    # Must use this naming convention to be used
    print(scope._ScopeClass__var3)
    # https://stackoverflow.com/questions/1641219/does-python-have-private-variables-in-classes
    # https://stackoverflow.com/questions/1301346/what-is-the-meaning-of-single-and-double-underscore-before-an-object-name
