list_nums = [44, 55, 22, 1, 66, 101, -1, 44, 100, 89]

left_point = 0
right_point = len(list_nums) - 1
max_num = 0

while left_point < right_point:
    if list_nums[left_point] > list_nums[right_point] and max_num < list_nums[left_point]:
        max_num = list_nums[left_point]
    elif list_nums[left_point] < list_nums[right_point] and max_num < list_nums[right_point]:
        max_num = list_nums[right_point]

    left_point += 1
    right_point -= 1

print(f"MAX: {max_num}")
