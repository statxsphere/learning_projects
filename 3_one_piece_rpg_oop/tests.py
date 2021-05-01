class A:
    def __init__(self):
        self.__name = 'A'
        self._name = 'a'

    def change_name(self, x):
        self._name = x
        self.__name = x

    def get_name(self):
        return self._name

    def get_names(self):
        return self.__name

class B(A):
    def change_name(self, x):
        self._name = x
        self.__name = x

    def get_name(self):
        return self.__name

a = A()
b = B()

b.change_name('z')
print(b.get_name())
