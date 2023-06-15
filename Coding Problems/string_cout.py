"""
input : aaabbcccdde
output: 3a2b3c2d1e
"""
input_str = "aaabbcccdde"
output_str = ""

for i in input_str:
    if i in output_str:
        find_var = output_str.find(i)-1
        if find_var >= 0:
            inc = int(output_str[find_var])
            inc += 1
            output_str = list(output_str)
            output_str[find_var] = str(inc)
            output_str = "".join(output_str)
    else:
        output_str = output_str + "1" + i

print(output_str)