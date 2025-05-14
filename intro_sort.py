import math

def insertion_sort(A, left=0, right=None):
    if right is None:
        right = len(A) - 1
    for i in range(left + 1, right + 1):
        key = A[i]
        j = i - 1
        while j >= left and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

def heapify(A, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and A[l] > A[largest]:
        largest = l
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, n, largest)

def heapsort(A, left=0, right=None):
    if right is None:
        right = len(A) - 1
    n = right - left + 1
    for i in range(n // 2 - 1, -1, -1):
        heapify(A[left:right+1], n, i)
    for i in range(n - 1, 0, -1):
        A[left], A[left + i] = A[left + i], A[left]
        heapify(A[left:left+i], i, 0)

def partition(A, low, high):
    pivot = A[high]
    i = low - 1
    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[high] = A[high], A[i + 1]
    return i + 1

def introsort_util(A, start, end, maxdepth):
    size = end - start + 1
    if size < 16:
        insertion_sort(A, start, end)
        return
    if maxdepth == 0:
        heapsort(A, start, end)
        return
    p = partition(A, start, end)
    introsort_util(A, start, p - 1, maxdepth - 1)
    introsort_util(A, p + 1, end, maxdepth - 1)

def intro_sort(A):
    maxdepth = int(2 * math.log2(len(A))) if len(A) > 0 else 0
    introsort_util(A, 0, len(A) - 1, maxdepth)
    return A

def intro_sort_interativo_wapper(A):
    return intro_sort(A)
