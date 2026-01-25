#!/bin/python3

import math
import os
import random
import re
import sys

def weird(n):
    if n % 2 != 0:
        return 'Weird'
    elif n % 2 == 0 and 2 <= n <=5:
        return 'Not Weird'
    elif n % 2 == 0 and 6 <= n <=20:
        return 'Weird'
    else:
        return 'Not Weird'
    
    
    

if __name__ == '__main__':
    n = int(input().strip())
    print(weird(n))
