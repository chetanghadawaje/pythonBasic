"""
Maintain references to object from earlier scopes.
"""


def outerFun(a):
    def innerFun(b):
        return a + b
    return innerFun


tempobj = outerFun(2)
_ = tempobj(8)
print(_)

"""
Output:- 10
"""