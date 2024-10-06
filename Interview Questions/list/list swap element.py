"""
Swap element to target to from index and other element is rest of order
"""

def swap_element(input_list, target_index, from_index):
    list1 = input_list[:from_index]
    target_value = input_list[target_index]
    del(input_list[target_index])
    list2 = input_list[target_index-2:]
    new_list = [*list1, target_value, *list2]
    return new_list


def swap_element_1(input_list, target_index, from_index):
    target_value = input_list.pop(target_index)
    input_list.insert(from_index, target_value)
    return input_list


if __name__ == "__main__":
    input_list = ['A', 'B', 'C', 'D', 'E']
    target_index = 3
    from_index = 1
    output = swap_element(input_list, target_index, from_index)
    print(output)

    input_list_1 = ['A', 'B', 'C', 'D', 'E']
    output1 = swap_element_1(input_list_1, target_index, from_index)
    print(output1)
    """
    output:
    ['A', 'D', 'B', 'C', 'E']
    ['A', 'D', 'B', 'C', 'E']
    """

