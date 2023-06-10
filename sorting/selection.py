# Given an array
unsorted_list = [6, 2, 4, 1, 5, 3, 8, 9, 7, 15, 20, 12, 11, 45]


def selection_sort(unsorted):
    """
    Sort function using selection sort algorithm
    """
    for i in range(0, len(unsorted)):
        # If already at right position do nothing
        if min(unsorted[i:]) == unsorted[i]:
            continue
        else:
            # find index of the minimum value in sub-list and swap with curent position
            minimum = min(unsorted[i:])
            min_idx = unsorted.index(minimum)
            temp = unsorted[min_idx]
            unsorted[min_idx] = unsorted[i]
            unsorted[i] = temp

    return unsorted


result = selection_sort(unsorted_list)
for num in result:
    print(num)

# Analysis
# Best input: an array sorted in ascending order
# Best case: O(n) as it will go through whole list but never swap anything

# Worst input: an array sorted in descending order
# Worst case: O(n^2) as it goes through the loop for each member and again to find the minimum
