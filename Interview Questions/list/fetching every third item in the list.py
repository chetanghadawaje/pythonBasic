"""
Q) fetching every third item in the list.
"""

list_items = ["apple", "mango", "greps", "kiwi", "banana", "orange"]
output_list = []
for i in range(0, len(list_items), 3):
    output_list.append(list_items[i])

print(output_list)

"""
Output:
['apple', 'kiwi']
"""

output_list = list_items[::3]
print(output_list)
"""
Output:
['apple', 'kiwi']
"""

