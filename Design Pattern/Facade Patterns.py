"""
The word Facade means the face of a building or particularly an outer lying interface of a complex system, consists of several sub-systems.
"""


class Washing(object):
    def wash(self):
        print("Washing...")


class Rinsing:

    def rinse(self):
        print("Rinsing...")


class Spinning:

    def spin(self):
        print("Spinning...")


class WashingMachine(object):
    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()

    def startWashing(self):
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spin()


obj = WashingMachine()
obj.startWashing()

"""
Output:
Washing...
Rinsing...
Spinning...
"""