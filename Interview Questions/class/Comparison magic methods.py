"""
__eq__(self, other): Defines behavior for the equality operator, ==.
__ne__(self, other): Defines behavior for the inequality operator, !=.
__lt__(self, other): Defines behavior for the less-than operator, <.
__gt__(self, other): Defines behavior for the greater-than operator, >.
__le__(self, other): Defines behavior for the less-than-or-equal-to operator, <=.
__ge__(self, other): Defines behavior for the greater-than-or-equal-to operator, >=.
"""


class NumberClass():
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def additional(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number1 - self.number2 if self.number1 > self.number2 else self.number2 - self.number1

    def __gt__(self, obj1):
        print("Call greater method")
        return True if self.additional() > obj1.additional() else False


object1 = NumberClass(10, 20)
object2 = NumberClass(20, 15)

print("Object 1 Add call: ", object1.additional())
print("Object 2 Add call: ", object2.additional())
print("Object 1 Sub call: ", object1.subtract())
print("Object 2 Sub call: ", object2.subtract())
print("Greater method call: ", object1 > object2)

"""
Output:
Object 1 Add call:  30
Object 2 Add call:  35
Object 1 Sub call:  10
Object 2 Sub call:  5
Call greater method
Greater method call:  False
"""
