myDict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32, 'akshay': 21}

"""Using predefined function with key sort"""
sort_loop = dict()
for i in sorted(myDict.keys()):
    sort_loop[i] = myDict[i]
print(sort_loop)

sort_dict = sorted(myDict.items(), key=lambda x: x[0])
print(dict(sort_dict))

"""Using own logic"""
out_dict = dict()
keys_of_list = list(myDict.keys())    # or you can use values()
for i in range(0, len(keys_of_list)):
    for j in range(i, len(keys_of_list)-1):
        if keys_of_list[i] < keys_of_list[j]:
            out_dict[keys_of_list[i]] = myDict[keys_of_list[i]]
print(out_dict)
