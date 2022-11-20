# Homework Assignment #9
# Author: Emily Shull

# Set up an experiment to test the run-time differences between various searching (sequential and binary)
# and sorting (selection, insertion, mergesort, and quicksort) algorithms on a list of random numbers.
# The program should:
#     -Ask the user which test they want to run (searching or sorting). If searching, also ask the user for
#        the number to search for.
#     -Generate a list of 50,000 random integers between 1 and 100.
#     -Print out the elapse time to search for the item (for both linear and binary search) or the elapse time for
#        each sorting algorithm.
# Additional professor comment: for the longer operations, provide some form of user experience to show that the
# program is still "thinking"

import random
import time
from apscheduler.schedulers.background import BackgroundScheduler


def displayWelcome():
    print('Hi there! This program will time how long different search and sort operations take.')


def startTime():
    start_time = time.time()
    return start_time


def stopTime():
    end_time = time.time()
    return end_time


def time_convert(seconds):
    if seconds > 1:
        return format(seconds, '.8f') + ' seconds'
    else:
        milliseconds = seconds * 1000
        return format(milliseconds, '.8f') + ' milliseconds'


def pingingSymbol():
    print('.', end='')


def initData():
    dataset_size = input('How large of a dataset would you like to search against? Enter a number: ')
    while not dataset_size.isdigit():
        dataset_size = input('Please enter a number: ')

    # generate dataset
    dataset = []
    for i in range(0, int(dataset_size)):
        rand_num = random.randint(1, 101)
        dataset.append(rand_num)

    return dataset


def performSearch(dataset, feeling_lucky):
    search_type = ''
    if not feeling_lucky:
        print('Would you like to do a sequential search, a binary search, or both?')
        search_type = input('Type "s" for sequential or "b" for binary or "all": ')
        while search_type not in ('s', 'b', 'all'):
            search_type = input('Please type "s" for sequential or "b" for binary or "all": ')

    search_num = input('What number would you like to search for? Enter a number: ')
    while not search_num.isdigit():
        search_num = input('Please enter a number: ')

    if search_type == 's':
        performSeqSearch(dataset.copy(), int(search_num))
    elif search_type == 'b':
        performBinarySearch(dataset.copy(), int(search_num))
    else:
        performSeqSearch(dataset.copy(), int(search_num))
        performBinarySearch(dataset.copy(), int(search_num))


# Source: w3resource
def performSeqSearch(dataset, search_val):
    stime = startTime()

    pos = 0
    found = False

    while pos < len(dataset) and not found:
        if dataset[pos] == search_val:
            found = True
        else:
            pos = pos + 1

    if found:
        print('\n', search_val, 'was found in the dataset')
    else:
        print('\n', search_val, 'was NOT found in the dataset')

    etime = stopTime()
    print('Sequential search took:', time_convert(etime - stime))


# Source: GeeksforGeeks
def performBinarySearch(dataset, search_val):
    stime = startTime()

    dataset.sort()
    low = 0
    high = len(dataset) - 1
    found = False

    while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if dataset[mid] < search_val:
            low = mid + 1
        # If x is smaller, ignore right half
        elif dataset[mid] > search_val:
            high = mid - 1
        # means x is present at mid
        else:
            found = True
            break

    if found:
        print('\n', search_val, 'was found in the dataset')
    else:
        print('\n', search_val, 'was NOT found in the dataset')

    etime = stopTime()
    print('Binary search took:', time_convert(etime - stime))


def performSort(dataset, feeling_lucky):
    sort_type = ''
    if not feeling_lucky:
        print('Would you like to do a selection sort, insertion sort, mergesort, quicksort, or all?')
        sort_type = input('Type "s" for selection, "i" for insertion, "m" for mergesort, "q" for quicksort, or "all": ')
        while sort_type not in ('s', 'i', 'm', 'q', 'all'):
            sort_type = input('Please type "s" for selection, "i" for insertion, "m" for mergesort, "q" for quicksort, '
                              'or "all": ')

    schedule.start()
    schedule.add_job(pingingSymbol, 'interval', seconds=5)

    if sort_type == 's':
        performSelectionSort(dataset.copy())
    elif sort_type == 'i':
        performInsertionSort(dataset.copy())
    elif sort_type == 'm':
        performMergeSort(dataset.copy())
    elif sort_type == 'q':
        performQuickSort(dataset.copy())
    else:
        performMergeSort(dataset.copy())
        performQuickSort(dataset.copy())
        performSelectionSort(dataset.copy())
        performInsertionSort(dataset.copy())
        schedule.shutdown()


# Source: GeeksforGeeks
def performSelectionSort(dataset):
    size = len(dataset)
    stime = startTime()

    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if dataset[j] < dataset[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (dataset[ind], dataset[min_index]) = (dataset[min_index], dataset[ind])
    etime = stopTime()
    print('\nSelection sort took:', time_convert(etime - stime))


# Source: GeeksforGeeks
def performInsertionSort(dataset):
    stime = startTime()

    # Traverse through 1 to len(arr)
    for i in range(1, len(dataset)):
        key = dataset[i]
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < dataset[j]:
            dataset[j + 1] = dataset[j]
            j -= 1
        dataset[j + 1] = key
    etime = stopTime()
    print('\nInsertion sort took:', time_convert(etime - stime))


# Merges two subarrays of arr[].
# First subarray is arr[l...m]
# Second subarray is arr[m+1...r]
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    temp_l = [0] * n1
    temp_r = [0] * n2

    # Copy data to temp arrays temp_l[] and temp_r[]
    for i in range(0, n1):
        temp_l[i] = arr[l + i]

    for j in range(0, n2):
        temp_r[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if temp_l[i] <= temp_r[j]:
            arr[k] = temp_l[i]
            i += 1
        else:
            arr[k] = temp_r[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = temp_l[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = temp_r[j]
        j += 1
        k += 1


# Source: GeeksforGeeks
def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


def performMergeSort(dataset):
    stime = startTime()

    mergeSort(dataset, 0, len(dataset) - 1)

    etime = stopTime()
    print('\nMergesort took:', time_convert(etime - stime))


# Source: GeeksforGeeks
# Function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


# Source: GeeksforGeeks
# function to perform quicksort
def quickSort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)


def performQuickSort(dataset):
    stime = startTime()

    quickSort(dataset, 0, len(dataset) - 1)

    etime = stopTime()
    print('\nQuicksort took:', time_convert(etime - stime))


# ---- main
schedule = BackgroundScheduler()
displayWelcome()
# I'm feeling lucky runs all the operations for both searching and sorting
search_or_sort = input('Would you like to search or sort? Type "search" or "sort" or "I\'m feeling lucky": ')

while search_or_sort not in ('search', 'sort', 'I\'m feeling lucky'):
    search_or_sort = input('Please type "search" or "sort" or "I\'m feeling lucky": ')

raw_dataset = initData()

if search_or_sort == 'search':
    # do search things
    performSearch(raw_dataset, False)
elif search_or_sort == 'sort':
    # do sort things
    performSort(raw_dataset, False)
else:
    # do all the things
    performSearch(raw_dataset, True)
    performSort(raw_dataset, True)
