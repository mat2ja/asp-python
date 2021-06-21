from selection import selection_sort
from bubble import bubble_sort, bubble_sort_optimized, bubble_sort_2
from insertion import insertion_sort
from shell_sort import shell_sort

from random import randint
from time import time

a = [randint(1, 31) for i in range(10)]
print(f"Unsorted  : {a}\n")
print(f"Selection : {selection_sort(a)}")
print(f"Bubble    : {bubble_sort(a)}")
print(f"Bubble n  : {bubble_sort_2(a)}")
print(f"Insertion : {insertion_sort(a)}")
print(f"Shell     : {shell_sort(a)}")


# b = [randint(1, 200) for i in range(1000)]
# sstart = time()
# selection_sort(b)
# send = time()
# bstart = time()
# bubble_sort(b)
# bend = time()
# istart = time()
# insertion_sort(b)
# iend = time()
# print(f"Selection sort took {send-sstart} ms")
# print(f"Bubble sort took {bend-bstart} ms")
# print(f"Insertion sort took {iend-istart} ms")
