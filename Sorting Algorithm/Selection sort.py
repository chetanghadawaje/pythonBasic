"""
Selection sort is an in-place sorting algorithm, meaning the sorted items use the same storage as the original elements.
"""


def sort(input_list: list):
    print(f"Given list: {input_list}")

    for i, num in enumerate(input_list):
        for j in range(len(input_list)):
            if num < input_list[j]:
                input_list[i], input_list[j] = input_list[j], input_list[i]

    print(f"Sorted list: {input_list}")


sort([10, 100, 5, 0, -6, 200, 56])
