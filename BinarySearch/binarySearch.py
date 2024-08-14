# from util import time_it

# @time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1

# @time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    number_indices = []
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        number_indices.append(mid_index)
        next_index = mid_index + 1
        previous_index = mid_index - 1
        while numbers_list[previous_index] == mid_number:
            number_indices.append(previous_index)
            previous_index = previous_index - 1
        while numbers_list[next_index] == mid_number:
             number_indices.append(next_index)
             next_index = next_index + 1
        return number_indices

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

if __name__ == '__main__':
    numbers_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 34

    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    print(f"Number found at index {index} using binary search")