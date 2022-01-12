def shaker_sort(l: list) -> list:
    while True:
        swapped = False
        # Left -> right pass
        for i in range(1, len(l)):
            if l[i - 1] > l[i]:
                l[i - 1], l[i] = l[i], l[i - 1]
                swapped = True
        # No adjacent elements were swapped - list is sorted
        if not swapped:
            break
        swapped = False
        # Right -> left pass
        for j in range(len(l) - 1, 0, -1):
            if l[j] < l[j - 1]:
                l[j - 1], l[j] = l[j], l[j - 1]
                swapped = True
        # No adjacent elements were swapped - list is sorted
        if not swapped:
            break
    return l
