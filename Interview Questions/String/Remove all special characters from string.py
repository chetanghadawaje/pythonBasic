"""
Q) Remove all special characters from string
"""

string = "Hi i am @Python Dev. !!"
output = ''.join(e for e in string if e.isalnum() or e.isspace())
print(output)

"""
Output:
Hi i am Python Dev 
"""


import re
string = "hey th~!ere"
output = re.sub('[^a-zA-Z0-9 \n\.]', '', string)
print(output)

"""
Output:
hey there
"""