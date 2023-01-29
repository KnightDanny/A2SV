#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    start = arr[0]
    final = arr[n - 1]
    
    for x in range(n - 2, -1, -1):
        
        if arr[x] > final:
            arr[x + 1] = arr[x]
            
            for y in arr:
                print(y, end = " ")
                
            print()

            if arr[x] == start:
                arr[0] = final
                
                for y in arr:
                    print(y, end=" ")
        else:
            arr[x + 1] = final
            
            for y in arr:
                print(y, end = " ")
            break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
