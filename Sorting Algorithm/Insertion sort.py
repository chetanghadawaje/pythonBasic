"""
Insertion sort builds the final array one item at a time.
"""


def sort(input_list: list):
    print(f"Given list: {input_list}")

    for i in range(1, len(input_list)):
        key = input_list[i]
        j = i - 1

        while j >= 0 and key < input_list[j]:
            input_list[j + 1] = input_list[j]
            j = j - 1

        input_list[j + 1] = key
    print(f"Sort list: {input_list}")


sort([10, 100, 5, 0, -6, 200, 56])
