# In Hacker_Rank This is for python 2.
import re

t = int(input())

for _ in range(t):
    regex = raw_input()
    try:  
       re.compile(regex)
       print('True')
    except re.error:
        print('False')
