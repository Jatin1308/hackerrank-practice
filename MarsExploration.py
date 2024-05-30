from itertools import *
import itertools
import time
def marsExploration(s):
    required = 'SOS'*(len(s)//3)

    i = 0
    c = 0
    while i < len(s):
        if s[i] == required[i]:
            i+=1
        else:
            i+=1
            c+=1
    return c        
        

print(marsExploration('SOSSPSSQSSOR'))