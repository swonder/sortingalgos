def bubble_sort(l: list) -> list:
    while True:
        swapped = False
        # Loop through list and swap adjacent elements that are out of order
        for i in range(1, len(l)):
            if l[i - 1] > l[i]:
                l[i - 1], l[i] = l[i], l[i - 1]
                swapped = True
        # No adjacent elements were swapped in the pass - list is sorted
        if not swapped:
            break
    return l
