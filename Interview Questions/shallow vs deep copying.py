import copy

list_a = [1, 2, 3, 4, 5, 6]
list_b = [11, 12, 13, 14, [15, 16, 17], 18]
print(f"list_a: {list_a} \nlist_b: {list_b}")


"""
Python, we use = operator to create a copy of an object. You may think that this creates a new object; it doesn't. It only creates a new 
variable that shares the reference of the original object.
"""
print("-->Asinine<--")
list_a1 = list_a
list_b1 = list_b
print(f"list_a1: {list_a1} \nlist_b1: {list_b1}")

list_a1[1] = 99
print(f"list_a: {list_a} \nlist_a1: {list_a1}")

list_b1[1] = 999
print(f"list_b: {list_b} \nlist_b1: {list_b1}")
list_b1[4][1] = 88
print(f"list_b: {list_b} \nlist_b1: {list_b1}")


"""
A shallow copy creates a new object which stores the reference of the original elements.
"""
print("-->Shallow Copy<--")
list_a2 = copy.copy(list_a)
list_b2 = copy.copy(list_b)
print(f"list_a2: {list_a2} \nlist_b1: {list_b2}")

list_a1[1] = 8888
print(f"list_a: {list_a} \nlist_a2: {list_a2}")

list_b1[1] = 7777
print(f"list_b: {list_b} \nlist_b1: {list_b2}")
list_b1[4][1] = 6666
print(f"list_b: {list_b} \nlist_b1: {list_b2}")


"""
A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.
"""
print("-->Deep Copy<--")
list_a2 = copy.deepcopy(list_a)
list_b2 = copy.deepcopy(list_b)
print(f"list_a2: {list_a2} \nlist_b1: {list_b2}")

list_a1[1] = 4000
print(f"list_a: {list_a} \nlist_a2: {list_a2}")

list_b1[1] = 5000
print(f"list_b: {list_b} \nlist_b1: {list_b2}")
list_b1[4][1] = 6000
print(f"list_b: {list_b} \nlist_b1: {list_b2}")
