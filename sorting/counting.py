# Given an array
unsorted_list = [6, 2, 4, 1, 5, 3, 8, 9, 7, 15, 12, 11]


def counting_sort(unsorted):
    """
    Sort function using counting sort algorithm
    """

   # find max
    max_num = max(unsorted)
    # initialize array
    arr = [0]*(max_num+1)
    for num in unsorted:
        arr[num] += 1

    # another array
    sorted_arr = []
    for i in range(len(arr)):
        if arr[i] > 0:
            sorted_arr.extend([i]*arr[i])

    return sorted_arr


result = counting_sort(unsorted_list)
print(result)

# Analysis
# Best input:
# Best case:

# Worst input:
# Worst case:
