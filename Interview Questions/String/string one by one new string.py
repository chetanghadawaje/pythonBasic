"""
i/p = bmaunmdbraai
o/p = bandra, Mumbai
"""

def string_manipulation(str1):
    new_str1, new_str2 = "", ""
    for i in range(0, len(str1)-1, 2):
        new_str1 = new_str1 + str1[i]
        new_str2 = new_str2 + str1[i+1]
    return new_str1, new_str2

print(string_manipulation("bmaunmdbraai"))

"""
Output:
('bandra', 'mumbai')
"""