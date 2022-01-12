def hash_sort(l: list) -> list:
    size = len(l)
    f = [0] * size
    k = 0

    for v in l:
        f[v] += 1

    for i in range(len(f)):
        v = f[i]
        for j in range(v):
            l[k] = i
            k += 1

    return l
