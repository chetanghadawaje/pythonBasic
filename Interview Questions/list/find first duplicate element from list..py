"""
find first duplicate element from list. [10, 20, 20, 10, 30] Output:20.
"""

def fine_element(list1):
    element_list = []
    for i in list1:
        if i in element_list:
            return i
        element_list.append(i)

print(f"Duplicate element: {fine_element([10, 20, 20, 10, 30])}")

"""
Output:
Duplicate element: 20
"""