temp = [[x for x in range(y)] for y in range(6)]

for _ in temp:
    print(_)


"""
Output:-
[]
[0]
[0, 1]
[0, 1, 2]
[0, 1, 2, 3]
[0, 1, 2, 3, 4]
"""