"""It is a way to provide one and only one object of a particular type. It involves only one class to create methods and
 specify the objects"""


class singleTone(object):
    _instance = None

    def __new__(self):
        if not self._instance:
            self._instance = super(singleTone, self).__new__(self)
            self.name = "Single tone"

        return self._instance


if __name__ == '__main__':
    a = singleTone()
    print(a.name)
    b = singleTone()
    print(b.name)
    print(a is b)