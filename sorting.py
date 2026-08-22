# Insertion sort
def insertion_sort(data: list[int]) -> list[int]:
    for i in range(1, len(data)):
        curr_elem = data[i]
        prev_index = i-1

        while prev_index >= 0 and data[prev_index] > curr_elem:
            data[prev_index+1] = data[prev_index]
            prev_index -= 1
        data[prev_index+1] = curr_elem
    return data
