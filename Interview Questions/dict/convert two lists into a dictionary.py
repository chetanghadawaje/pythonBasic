"""
Q)convert two list into a dictionary
"""

list_one = ['name', "programing language", "version"]
list_two = ["chetan", "python", "3.x"]

output_dict = dict(zip(list_one, list_two))
print(output_dict)
"""
Output:
{'name': 'chetan', 'programing language': 'python', 'version': '3.x'}
"""


output_dict = {}
for i in range(len(list_one)):
    output_dict[list_one[i]] = list_two[i]
print(output_dict)
"""
Output:
{'name': 'chetan', 'programing language': 'python', 'version': '3.x'}
"""