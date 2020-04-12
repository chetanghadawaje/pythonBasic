class ClassOne():
    def __init__(self, temp1):
        self.temp1 = temp1

    def FunctionOne(self):
        print("This is Function One")

    def view(self):
        print(self.temp1)


class ClassTwo(ClassOne):
    def __init__(self, temp1, temp2):
        ClassOne.__init__(self, temp1)
        self.temp2 = temp2

    def FunctionTwo(self):
        print("This is Function Two")

    def view(self):
        print(self.temp2)


obj = ClassTwo(10,20)
obj.FunctionOne()
obj.view()