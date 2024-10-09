"""
find first duplicate element from list. [10, 20, 20, 10, 30] Output:20.
"""

from collections import Counter

def fine_element(list1):
    element_list = []
    for i in list1:
        if i in element_list:
            return i
        element_list.append(i)


# def fine_element_1(list1):
#     count_dict = Counter(list1)
#     output = [i for i,j in count_dict.items() if j==2 ]
#     return output

print(f"Duplicate element: {fine_element([10, 20, 20, 10, 30])}")
# print(f"Duplicate element: {fine_element_1([10, 20, 20, 10, 30])}")

"""
Output:
Duplicate element: 20
"""