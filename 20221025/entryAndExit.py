from __future__ import with_statement  # Not needed in Python 2.6+


class c(object):

    def __init__(self) -> None:
        super().__init__()
        self.dbcon = self
        pass

    def __enter__(self) -> None:
        # E.g. connect to db
        print('Connected')  # Not printed outside with
        return self.dbcon  # Does not work??
        return 'self.dbcon'  # Vaild

    def __exit__(self, type, value, traceback):
        # E.g. close db connection
        print('valid exit')
        return False

    def __repr__(self) -> str:
        # Printed if no valid return in __enter__??
        return f'In : {self.__class__.__name__}()'


if __name__ == '__main__':
    with c() as c:
        # pass
        print(c)
    print(c)
