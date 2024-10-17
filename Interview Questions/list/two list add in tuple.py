"""
input:['a','b','c'],[1,2,3]

output: [(‘a’, 1), (‘b’, 2), (‘c’, 3)]
"""

def p1(list1, list2):
    out_put = []
    for i,j in zip(list1, list2):
        out_put.append((i,j))
    print(out_put)

p1(['a','b','c'],[1,2,3])


def p2(x, y):
    return x, y

print(list(map(p2, ['a','b','c'],[1,2,3])))