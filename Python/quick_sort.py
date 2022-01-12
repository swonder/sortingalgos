def quick_sort(l) -> list:
    quick_sort_recursive(l, 0, len(l) - 1, False)
    return l

def modified_quick_sort(l) -> list:
    quick_sort_recursive(l, 0, len(l) - 1, True)
    return l

def quick_sort_recursive(l, low, high, modified):
    if low < high:
        if modified:
            mid = (low + high) // 2
            l[mid], l[low] = l[low], l[mid]

        leftmost = low + 1
        pivot = l[low]
        for i in range(low + 1,high + 1):
            if l[i] < pivot:
                l[i], l[leftmost] = l[leftmost], l[i]
                leftmost += 1
        pivot = leftmost - 1
        l[pivot], l[low] = l[low], l[pivot]

        quick_sort_recursive(l, low, pivot - 1, modified)
        quick_sort_recursive(l, pivot + 1, high, modified)
