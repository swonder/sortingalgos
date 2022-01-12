from random import randint

def create_random_list(size: int) -> list:
    num_list = []

    for i in range(size):
        rand_num = randint(0, size - 1)
        num_list.append(rand_num)

    return num_list

def create_mostly_sorted_list(size: int) -> list:
    num_list = create_random_list(size)

    num_list.sort()
    # Swap the first and last elements to create mostly sorted list
    if size > 0:
        num_list[0], num_list[-1] = num_list[-1], num_list[0]

    return num_list
