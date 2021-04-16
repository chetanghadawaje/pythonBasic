"""
Q) the number of occurrences for each element in list
"""
from collections import Counter
list_item = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
print(Counter(list_item))

"""
Output:
Counter({'blue': 3, 'red': 2, 'yellow': 1})
"""


list_item = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
count_dict = {}
for i in set(list_item):
    count_dict[i] = list_item.count(i)
print(count_dict)
