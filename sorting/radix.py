# Given an array
unsorted_list = [6, 2, 4, 1, 5, 3, 8, 9, 7,
                 15, 12, 11, 123, 32, 12, 32, 11, 23, 342]


def get_place(num, index):
    return num // 10**index % 10


def counting_sort(unsorted, index, max_digit):
    """
    Sort function using counting sort algorithm
    """

    if index == max_digit:
        return unsorted

   # find max
    max_num = float('-inf')
    for num in unsorted:
        place = get_place(num, index)
        if get_place(num, index) > max_num:
            max_num = place

    # initialize multidimensional array
    # manually populating array to avoid referencing the same array
    arr = []
    for i in range(max_num+1):
        arr.append([])

    for num in unsorted:
        place = get_place(num, index)
        arr[place].append(num)

    # another array
    sorted_arr = []
    for i in range(len(arr)):
        if len(arr[i]) != 0:
            sorted_arr.extend(arr[i])

    counting_sort(sorted_arr, index+1, max_digit)


def radix_sort(unsorted):
    """
    Sort function using radix sort algorithm
    """

    max_digit = float('-inf')
    for num in unsorted:
        if len(str(num)) > max_digit:
            max_digit = len(str(num))

    counting_sort(unsorted, 0, max_digit)


result = radix_sort(unsorted_list)
print(result)

# Analysis
# Best input:
# Best case:

# Worst input:
# Worst case:
