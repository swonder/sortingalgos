def merge_sort(l: list) -> list:
    a_len = len(l)
    # Make sure the recursive function stops at element size of 1
    if a_len <= 1:
        return

    mid = a_len // 2
    left = l[:mid]
    right = l[mid:]
    # Keep sorting both halves recursively until each list contains just one element
    merge_sort(left)
    merge_sort(right)
    # Merge left and right back into l
    merge(l, left, right)

# Subroutine for taking right and left child sublists and rewriting parent list with sorted values
def merge(l: list, left: list, right: list):
    left_len = len(left)
    right_len = len(right)
    i = 0 # Left list index value
    j = 0 # Right list index value
    k = 0 # Merged list index

    while i < left_len and j < right_len:
        # Left list had the smallest value place left value in merged list
        if left[i] <= right[j]:
            l[k] = left[i]
            i += 1
        # Right list had the smallest value place right value in merged list
        else:
            l[k] = right[j]
            j += 1
        k += 1
    # If left list was longer than the other, place any remaining left values in merge list
    while i < left_len:
        l[k] = left[i]
        i += 1
        k += 1
    # If right list was longer than the other, place any remaining right values in merge list
    while j < right_len:
        l[k] = right[j]
        j += 1
        k += 1
