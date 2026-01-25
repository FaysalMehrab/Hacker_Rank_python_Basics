#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    
    words = s.split(' ') # we need to preserve spaces
    
    cap_word = [w.capitalize() for w in words]
    
    return ' '.join(cap_word) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
