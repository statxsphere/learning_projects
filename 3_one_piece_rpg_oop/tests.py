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
    def called(self):
        print('B')

a = ""
b = B()
if not a:
    print(b.get_name())
# print(b.get_names())
# b.change_name('z')
# print(b.get_names())
