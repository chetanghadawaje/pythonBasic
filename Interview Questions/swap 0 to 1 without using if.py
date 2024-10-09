"""
Swap number without using if condition
"""

list1 = [1,0,1,0,0,0,1,1,1,0]

Str1 = "".join(str(num) for num in list1)

Str1 = Str1.replace("1", "2")
Str1 = Str1.replace("0", "1")
Str1 = Str1.replace("2", "0")

new_list = []
for i in Str1:
	new_list.append(int(i))
print(new_list)


new_list1 = [1 - num for num in list1]
print(new_list1)