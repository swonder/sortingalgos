def selection_sort(l) -> list:
    min_index = 0
    # Advance the index of the first comparison number by 1
    for i in range(0, len(l)):
        min_index = i
        # Find smallest element after the first element
        for j in range(i + 1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        # Swap first element with the lowest subsequent element found
        l[i], l[min_index] = l[min_index], l[i]

    return l
