def merge_sort(l: list) -> list:
    if len(l) < 2:
        return l

    result = []
    mid = len(l) // 2

    right = merge_sort(l[:mid])
    left = merge_sort(l[mid:])
    while len(right) > 0 and len(left) > 0:
        if right[0] > left[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    result += right
    result += left

    return result