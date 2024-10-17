"""
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

def string_approch(x):
    new_str = str(x)
    new_str1 = new_str[::1]
    print(new_str  == new_str1)


num = 121
string_approch(num)


def without_string_approch(num):
    temp = num
    t = 0
    while temp > 0:
        r = temp % 10
        t = (t*10)+r
        temp = temp //10
    if num == t:
        print(True)


num = 1221
without_string_approch(num)