from bubble_sort import bubble_sort
from hash_sort import hash_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort, modified_quick_sort
from selection_sort import selection_sort
from shaker_sort import shaker_sort

from collections import OrderedDict

def get_sort_function_names() -> OrderedDict:
    return OrderedDict([
        ("Bubble", bubble_sort),
        ("Shaker", shaker_sort),
        ("Selection", selection_sort),
        ("Quick", quick_sort),
        ("M. Quick", modified_quick_sort),
        #("Merge", merge_sort),
        ("Hash", hash_sort),
        ("Insertion", insertion_sort),
    ])
