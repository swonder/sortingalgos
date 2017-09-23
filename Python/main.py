#################################################
# Implementation of 8 popular sorting algorithms#
# stdout includes # compares and # swaps        #
# Shawn Wonder                                  #
# 2/12/2015                                     #
#################################################

import random
import math
import sys
from collections import OrderedDict
 
#Creates a randomly populated list that has 'size' number of elements in it 
def create_random_list(size):
    num_list = []
    for i in range(size):
        rand_num = random.randint(0, size-1)
        num_list.append(rand_num)
    return num_list

#Creates a list that is mostly sorted
def create_mostly_sorted_list(size):
    num_list = create_random_list(size)
    num_list.sort()
    #Swap the first and last elements
    if size > 0:
        num_list[0], num_list[-1] = num_list[-1], num_list[0]
    return num_list

#Formats a value to have five digits total with two of those values right of the decimal
def format_val(x):
    if x!=0:
        x = math.log(x)/math.log(2)
        x = "%5.2f" % x
        return x
    return 0
     
def bubble_sort(l, counts):
    while True:
        swapped = False
        #Loop through list and swap adjacent elements that are out of order
        for i in range(1, len(l)):
            counts[0]+=1
            if l[i-1] > l[i]:
                counts[1]+=1
                l[i-1], l[i] = l[i], l[i-1]
                swapped = True
        #No adjacent elements were swapped in the pass - list is sorted
        if not swapped:
            break
        
def shaker_sort(l, counts): #counts[0] is compares, counts[1] is swaps
    while True:
        swapped = False
        #Left->right pass
        for i in range(1, len(l)):
            counts[0]+=0
            if l[i-1] > l[i]:
                counts[1]+=1
                l[i-1], l[i] = l[i], l[i-1]
                swapped = True
        #No adjacent elements were swapped - list is sorted
        if not swapped:
            break
        swapped = False
        #Right->left pass
        for j in range(len(l)-1, 0,-1):
            counts[0]+=1
            if l[j] < l[j-1]:
                counts[1]+=1
                l[j-1], l[j] = l[j], l[j-1]
                swapped = True
        #No adjacent elements were swapped - list is sorted
        if not swapped:
            break

def selection_sort(l, counts):
    min_index = 0;
    #Advance the index of the first comparison number by 1
    for i in range(0, len(l)):
        min_index = i
        #Find smallest element after the first element
        for j in range(i+1, len(l)):
            counts[0]+=1
            if l[j] < l[min_index]:
                min_index = j
        #Swap first element with the lowest subsequent element found
        counts[1]+=1
        l[i], l[min_index] = l[min_index], l[i]

def quick_sort(l, counts):
    quick_sort_recursive(l, 0, len(l)-1, False, counts)
    
def modified_quick_sort(l, counts):
    quick_sort_recursive(l, 0, len(l)-1, True, counts)
    
def quick_sort_recursive(A, low, high, modified, counts):
    if low < high:
        if modified:
            mid = (low+high)/2
            counts[1]+=1
            A[mid], A[low] = A[low], A[mid]
            
        leftmost = low+1
        pivot = A[low]
        for i in range(low+1,high+1):
            counts[0]+=1
            if A[i] < pivot:
                counts[1]+=1
                A[i], A[leftmost] = A[leftmost], A[i]
                leftmost += 1
        pivot = leftmost-1
        counts[1]+=1
        A[pivot], A[low] = A[low], A[pivot]
        quick_sort_recursive(A, low, pivot-1, modified, counts)
        quick_sort_recursive(A, pivot+1, high, modified, counts)
        
#1 swap = 3 copies
def merge_sort(A, counts):
    local_copy = 0
    a_len = len(A)
    #Make sure the recursive function stops at element size of 1
    if a_len <= 1:
        return
    #Cut list A into two pieces
    mid = a_len/2
    left = A[:mid]
    local_copy += len(A)/3 #Copy is only 1/3 as much work as a swap
    right = A[mid:]
    local_copy += len(A)/3
    #Keep sorting both halves recursively until each list contains just one element
    merge_sort(left, counts)
    merge_sort(right, counts)
    #Merge left and right back into A 
    merge(A, left, right, counts)

    counts[1] += local_copy

#Subroutine for taking right and left child sublists and rewriting parent list with sorted values
def merge(A, left, right, counts):
    left_len = len(left)
    right_len = len(right)
    i=0 #Left list index value
    j=0 #Right list index value
    k=0 #Merged list index
    
    while i < left_len and j < right_len:
        #Left list had the smallest value place left value in merged list
        counts[0]+=1
        if left[i] <= right[j]:
            A[k] = left[i]
            i+=1
        #Right list had the smallest value place right value in merged list
        else:
            A[k] = right[j]
            j+=1
        k+=1
    #If left list was longer than the other, place any remaining left values in merge list
    while i < left_len:
        counts[0]+=1
        A[k] = left[i]
        i+=1
        k+=1
    #If right list was longer than the other, place any remaining right values in merge list
    while j < right_len:
        counts[0]+=1
        A[k] = right[j]
        j+=1
        k+=1

def hash_sort(l, counts):
    size = len(l)
    #Frequency Array
    f = [0]*size 
    for v in l:
        f[v] +=1
    k=0
    for i in range(len(f)):
        v = f[i]
        for j in range(v):
            l[k] = i
            k+=1
    counts[0] = size
    counts[1] = size

def insertion_sort(l, counts):
    if len(l) == 0:
        return []
    srt = []
    srt.append(l.pop()) #Take the last element and put it into the sorted list
    while len(l) > 0:
        last = l.pop() #Pop the last element off the unsorted list
        for i in range(0, len(srt)):
            if len(srt) == 1: #This is the first and only element
                counts[0] += 1
                if last > srt[i]:
		    srt.append(last)
                    counts[1] += 1
		else:
                    srt.insert(0, last)
                    counts[1] += 1 
            else: #More than one element
                if i < len(srt)-1:
                    counts[0] += 1
                    if i == 0 and last <= srt[i]:
                        counts[0] += 1
                        srt.insert(0, last)
                        counts[1] += 1
                    elif last > srt[i] and last <= srt[i+1]:
                        counts[0] += 1
                        srt.insert(i+1, last)
                        counts[1] += 1
                else:
                    srt.append(last)
    return srt


            
def main():
    test_range = [0, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
    sys.setrecursionlimit(4106) # Make sure program can recurse more than 1000 times so mostly sorted quicksort will have enough recursions to run  
    counts = [0,0] #0 is number of compares and 1 is number of swaps 
    function_names = OrderedDict([("Bubble", bubble_sort), ("Shaker", shaker_sort), ("Selection", selection_sort), \
                                  ("Quick", quick_sort), ("M. Quick", modified_quick_sort), ("Merge", merge_sort), \
                                  ("Hash", hash_sort), ("Insertion", insertion_sort)])
    n = 0
    k = 2
    for i in test_range:
        #Print the column showing which power of 2 program is on
        if k >= 3:
            print k, "\t",
        else:
            print "\t",
        #rand_list_master = create_random_list(i)
        mostly_sorted_list_master = create_mostly_sorted_list(i)
        for func_name in function_names:
            counts = [0,0]
            #Make a copy of the list so when the function is called it doesn't overwrite the original random list
            #rand_list = list(rand_list_master)
            rand_list = list(mostly_sorted_list_master)
            #Print out function name headers
            if i == 0:
                print func_name, "\t", 
            #print out function data
            else:
                function_names[func_name](rand_list, counts)
                #counts[0] = format_val(counts[0])
                counts[1] = format_val(counts[1])
		#Display number of compares		
		#print counts[0], "\t",
                #Display number of swaps           
		print counts[1], "\t",
            n+=1
        #Insert a new line when at the end of a row
        if n % len(function_names) == 0 and n > 0:
            print  ""
        k+=1
      
main()



                
