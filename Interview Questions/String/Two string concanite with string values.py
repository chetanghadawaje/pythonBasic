"""
a = ["m", "na", "i", "chi"] b = ["y", "me", "s", "rag"] #output = ["my", "name", "is", "chirag"]
"""
#Way 1
def string_concatenate(list1, list2):
    output_list = []
    for i, value in enumerate(list1):
        output_list.append(value + list2[i])
    return output_list

a = ["m", "na", "i", "chi"]
b = ["y", "me", "s", "rag"]
print(string_concatenate(a, b))

# Way 2
out_put_list_using_zip = [i+j for i, j in zip(a,b)]
print(f"Using zip: {out_put_list_using_zip}")

"""
Output:
['my', 'name', 'is', 'chirag']
Using zip: ['my', 'name', 'is', 'chirag']
"""