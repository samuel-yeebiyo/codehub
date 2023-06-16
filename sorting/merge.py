# Given an array
unsorted_list = [6, 2, 4, 1, 5, 3, 8, 9, 7, 15, 20, 12, 11, 45]


def merge_lists(list1, list2):
    """
    Merge lists together in a sorted manner
    """
    new_list = []
    i, j = 0, 0

    while len(new_list) != len(list1)+len(list2):
        # Other side should be sorted so appending rest should be good
        if i > len(list1)-1:
            new_list.extend(list2[j:])
            break
        elif j > len(list2)-1:
            new_list.extend(list1[i:])
            break
        # compare lists
        if list1[i] < list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1

    return new_list


def merge_sort(unsorted):
    """
    Sort function using merge sort algorithm
    """
    # split list
    size = len(unsorted)
    if size > 1:
        left = unsorted[:int(size/2)]
        right = unsorted[int(size/2):]
        val_left = merge_sort(left)
        val_right = merge_sort(right)
    else:
        return unsorted

    merged = merge_lists(val_left, val_right)

    return merged


result = merge_sort(unsorted_list)
for num in result:
    print(num)

# Analysis
# Best input:
# Best case:

# Worst input:
# Worst case:
