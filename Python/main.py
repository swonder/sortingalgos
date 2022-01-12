'''
Implementation of 8 popular sorting algorithms
Includes unit tests for correct output and benchmarks for time complexity
'''

from bubble_sort import bubble_sort
from hash_sort import hash_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort, modified_quick_sort
from random_lists import create_random_list, create_mostly_sorted_list
from selection_sort import selection_sort
from shaker_sort import shaker_sort
from sort_functions import get_sort_function_names

from sys import setrecursionlimit
from collections import OrderedDict
from timeit import default_timer
from tabulate import tabulate

def main():
    # Make sure program can recurse more than 1000 times so mostly
    # sorted quicksort will have enough recursions to run
    setrecursionlimit(4106)
    times_to_repeat_function = 100
    msg = (
        f'Running sorting algorithms and calculating average runtime '
        f'in seconds over {times_to_repeat_function} iterations...'
    )
    print(msg)
    sort_function_names = get_sort_function_names()

    headers = generate_table_headers(sort_function_names)
    data = generate_table_data(sort_function_names, times_to_repeat_function)

    print(tabulate(data, headers=headers))

def generate_table_headers(sort_function_names: OrderedDict) -> list:
    header = ['List Elements']
    for sort_function_name in sort_function_names:
        header.append(sort_function_name)
    return header

def generate_table_data(
    sort_function_names: OrderedDict,
    times_to_repeat_function: int
) -> list:
    test_range = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
    data = []

    for i in test_range:
        rand_list = create_random_list(i)
        # rand_list = create_mostly_sorted_list(i)
        average_runtimes = [i]
        for sort_function_name in sort_function_names:
            repeat = 0
            elapsed_times = []
            while repeat < times_to_repeat_function:
                start_time = default_timer()
                result = sort_function_names[sort_function_name](rand_list)
                elapsed_time = default_timer() - start_time
                elapsed_times.append(elapsed_time)
                repeat += 1
            average_runtime = sum(elapsed_times) / times_to_repeat_function
            average_runtimes.append(average_runtime)
        data.append(average_runtimes)
    return data

if __name__ == '__main__':
    main()
