list = [ [ ] ] * 5
print(list)

list[0].append(10)
print(list)

list[1].append(20)
print(list)

list.append(30)
print(list)

"""
Output:
[[], [], [], [], []]
[[10], [10], [10], [10], [10]]
[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]
"""