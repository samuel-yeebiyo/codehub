# Given an array
unsorted_list = [6, 2, 4, 1, 5, 3, 8, 9, 7, 15, 20, 12, 11, 45]


def insertion_sort(unsorted):
    """
    Sort function using insertion sort algorithm
    """
    for i in range(1, len(unsorted)):
        # skip if current number is in correct
        # position relative to left neighbor
        if unsorted[i] >= unsorted[i-1]:
            continue
        elif unsorted[i] < unsorted[i-1]:
            # find best position on left side
            for j in reversed(range(0, i)):
                # swap positions
                if unsorted[j] > unsorted[i]:
                    temp = unsorted[j]
                    unsorted[j] = unsorted[i]
                    unsorted[i] = temp
                    i -= 1  # keep pointer at main num
                else:
                    break

    return unsorted


result = insertion_sort(unsorted_list)
for num in result:
    print(num)

# Analysis
# Best input: an array sorted in ascending order
# Best case: O(n) as it never enters the nested loop if the array is sorted

# Worst input: an array sorted in descending order
# Worst case: O(n^2) the smallest number would needsto be swapped all the way to the front
