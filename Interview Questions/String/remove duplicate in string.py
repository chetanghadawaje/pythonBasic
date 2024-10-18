str1 = "Programming"
temp = {}
output = ""
output2 = ""

for i in str1:
    if i not in temp.keys():
        temp[i] = 1
    else:
        temp[i] += 1

for i, j in temp.items():
    if j == 1:
        output = output + i
    else:
        output2 = output2 + i

print(output)


""" Perform slicing"""
print(str1[3:7])