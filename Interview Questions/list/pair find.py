"""
Write program find pair list element and pair not presetnt that elemet print all not find element.
"""
from collections import Counter

def find_pair(input1):
        element_count = Counter(input1)
        unpaired_elements = [element for element, count in element_count.items() if count % 2 != 0]
        print("Unpaired elements:", unpaired_elements)

find_pair([7,7,5])
