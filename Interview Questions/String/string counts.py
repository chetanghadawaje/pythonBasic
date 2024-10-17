input_string = "abbcccddddaae"
"""a1b2c3d4a2e1"""
temp = input_string[0]
counter = 0
output = ""
for i in range(len(input_string)):
    if temp == input_string[i]:
        counter += 1
    else:
        output = output + f"{temp}{counter}"
        temp = input_string[i]
        counter = 1
output = output + f"{temp}{counter}"
print(output)
